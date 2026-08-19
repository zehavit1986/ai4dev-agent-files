# Anthropic Python SDK - Part 1

Small examples for using the Anthropic Python SDK with Claude, including:

- message-based chat
- system prompts
- temperature tuning
- streaming responses

## Prerequisites

- Python 3.10+
- An Anthropic API key

## Setup

1. Install dependencies:

    ```bash
    pip install anthropic python-dotenv
    ```

2. Add your API key to `.env` in the project root:

    ```env
    ANTHROPIC_API_KEY=your-key-here
    ```

## Example Scripts

- **10-messages.py**  
   Basic multi-turn conversation using a `messages` list and helper functions.

- **20-system-prompt.py**  
   Adds a `system` prompt to shape model behavior (math tutor style).

- **30-temperature.py**  
   Compares low vs high `temperature` outputs for the same prompt.

- **40-stream.py**  
   Streams output token-by-token using `client.messages.stream(...)`.

Run any script from the project root:

```bash
python 10-messages.py
python 20-system-prompt.py
python 30-temperature.py
python 40-stream.py
```


## Notes

- Model name in the scripts is currently set to `claude-haiku-4-5`.
