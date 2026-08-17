from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-haiku-4-5"

messages = [
    {"role": "user", "content": "Define quantum computing"}
]

with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        # Send each chunk to the client (e.g. via websocket)
        print(text, end="", flush=True)

    # Get the complete message for database storage
    final_message = stream.get_final_message()

print()