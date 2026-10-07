from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-haiku-4-5"

# Helper
# Helper functions to manage the conversation history

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text


# Start with an empty message list
messages = []

userText1 = "Define quantum computing in one sentence"
userText2 = "Write another sentence"

# Add the initial user question
add_user_message(messages, userText1)

# Get Claude's response
answer = chat(messages)

print("-- The LLM first reponse:")
print(answer)

# Add Claude's response to the conversation history
add_assistant_message(messages, answer)

# Add a follow-up question
add_user_message(messages, userText2)

# Get the follow-up response with full context
final_answer = chat(messages)

add_assistant_message(messages, final_answer)


print("-- The LLM second reponse:")
print(final_answer)

# print("Messages:")
# print(messages)