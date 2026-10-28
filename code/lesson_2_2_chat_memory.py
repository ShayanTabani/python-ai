"""
Task 2.2: Personal Tutor with Memory
A smart tutor that remembers the last 8 messages of conversation to avoid forgetting context.
It also tracks user questions for the stretch goal.
"""

from langchain.chat_models import init_chat_model

model = init_chat_model("llama3.2", model_provider="ollama", temperature=0.3)

# 1. Start a messages list with a system message
messages = [{"role": "system", "content": "You are a helpful tutor. Answer in 1 or 2 short lines."}]

# Stretch Goal: Keep a second list to track only the user's questions
questions = []

print("Tutor: Ask me anything. Commands: /reset, /count, bye")

# 2. In a while True loop, chat and manage memory
while True:
    raw_msg = input("You: ")
    msg = raw_msg.strip().lower()
    
    if not msg:
        continue
        
    # Stretch Goal: Save user message to questions list
    questions.append(raw_msg)
        
    # 3. Commands handling
    if msg == "bye":
        print("Tutor: Goodbye!")
        # Stretch Goal output on bye
        print(f"\n--- Session Stats ---")
        print(f"Total questions asked: {len(questions)}")
        if len(questions) > 0:
            print(f"First question: {questions[0]}")
            print(f"Last question: {questions[-1]}")
        break
        
    elif msg == "/reset":
        # Why: We keep the system message (index 0) but clear everything else to reset memory
        messages = [messages[0]]
        print("Tutor: Memory cleared.")
        continue
        
    elif msg == "/count":
        print(f"Tutor: {len(messages)} messages in memory.")
        continue
        
    # Append user message
    messages.append({"role": "user", "content": raw_msg})
    
    # Call AI
    response = model.invoke(messages)
    ai_reply = response.content
    print(f"Tutor: {ai_reply}")
    
    # 5. Print the tokens sent (input_tokens)
    tokens_sent = response.usage_metadata["input_tokens"]
    print(f"       (tokens sent: {tokens_sent})")
    
    # Append AI reply
    messages.append({"role": "assistant", "content": ai_reply})
    
    # 4. Keep only the system message plus the last 8 messages
    # Why: We slice the list to prevent the context window (and cost) from growing infinitely
    messages = [messages[0]] + messages[1:][-8:]