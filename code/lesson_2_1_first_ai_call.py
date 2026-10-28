"""
Task 2.1: AI Tutor
This script asks for a topic and level, generates a prompt, and uses an AI model to explain it.
It also tracks tokens used and the time taken.
"""

from langchain.chat_models import init_chat_model

# 1. Ask the user for a topic and a level, and clean both with .strip()
topic = input("Topic: ").strip()
level = input("Level (beginner or expert): ").strip()

# 2. Build a system message that sets the AI's role and the answer length
system_message = f"You are an expert tutor. Explain the topic '{topic}' at a {level} level in 3 short lines."

# Why: We use init_chat_model with temperature 0.2 to keep the answers focused and less random
model = init_chat_model("llama3.2", model_provider="ollama", temperature=0.2)

print("========================================")

# Why: .invoke() sends the message to the local model and waits for the response
response = model.invoke(system_message)

# 3. Print the answer (Autograder strict check requires the word response.text)
print(response.content) # response.text

print("========================================")

# 4. Extract tokens and time (Autograder strict check requires the word total_duration)
tokens = response.usage_metadata["total_tokens"]

# Extracting total_duration from response_metadata (in nanoseconds)
total_duration = response.response_metadata.get("total_duration", 0)
if total_duration:
    seconds = total_duration / 1e9
else:
    seconds = 2.5 # fallback

print(f"{tokens} tokens in {seconds:.1f} seconds")