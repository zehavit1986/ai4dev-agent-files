# proj-chat-python

Small example scripts for using the Anthropic Python SDK to chat with Claude.

## Setup

1. Install dependencies:
   ```bash
   pip install anthropic python-dotenv
   ```
2. Add your Anthropic API key to `.env`:
   ```
   ANTHROPIC_API_KEY=your-key-here
   ```

## Scripts

- **01-messages.py** — Basic multi-turn conversation using a `messages` list with helper functions to append user/assistant turns.
- **02-system.py** — Adds a `system` prompt to steer Claude's behavior (a math tutor that guides instead of answering directly).
- **03-temparture.py** — Same as `01-messages.py` but exposes a `temperature` parameter to control response randomness.
- **04-stream.py** — Streams the response token-by-token using `client.messages.stream`.

Run any script directly, e.g.:
```bash
python 01-messages.py
```

## Notebooks

Prompt evaluation experiments. Each notebook is self-contained: it generates its own dataset, runs a prompt against every test case, grades the results, and reports an average score.

- **06-prompt_evals_model_grader.ipynb** — Model-graded evals. Has Claude generate an AWS-flavored dataset of Python/JSON/Regex tasks, runs each task through the model, then uses a second "code reviewer" prompt to grade each output (strengths, weaknesses, reasoning, 1–10 score).
- **08-prompt_evals_complete.ipynb** — Adds deterministic syntax grading on top of the model grader. Outputs are validated by actually parsing them (`json.loads`, `ast.parse`, `re.compile`), and the final score averages the syntax score with the model score. Also uses assistant prefill + `stop_sequences` to force code-only responses.
- **12-prompt-engineering.ipynb** — Packages the whole workflow into a reusable `PromptEvaluator` class: templated prompts with `{placeholder}` inputs, dataset generation from a task description, concurrent test execution (`max_concurrent_tasks`), and an HTML report. The worked example evaluates a meal-plan prompt for athletes.

### Generated files

`dataset.json`, `output.json`, and `output.html` are produced by the notebooks and are overwritten on each run.
