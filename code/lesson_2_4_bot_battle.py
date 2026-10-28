"""
Task 2.4 Stretch: Bot Battle
Tests hardcoded rules against the AI model with 6 questions to see who performs better.
"""
from langchain.chat_models import init_chat_model

questions = [
    "What are your hours?",
    "How much is an xray?",
    "Do you offer free checkups?",
    "My leg hurts, what should I do?",
    "I want to make a complaint!",
    "Where is the clinic?"
]

model = init_chat_model("llama3.2", model_provider="ollama", temperature=0.1)
unanswered_by_rules = 0

for q in questions:
    print(f"\nQ: {q}")
    msg = q.lower()
    
    # --- Rule Bot Logic ---
    rule_reply = ""
    if "hours" in msg:
        rule_reply = "We are open 9am to 10pm."
    elif "xray" in msg:
        rule_reply = "Xray is 3500 PKR."
    elif "complaint" in msg:
        rule_reply = "Connecting to human..."
    elif "where" in msg:
        rule_reply = "Main Boulevard, Lahore."
    else:
        rule_reply = "I don't know."
        unanswered_by_rules += 1
        
    print(f"Rule Bot: {rule_reply}")
    
    # --- AI Bot Logic ---
    prompt = f"You are a clinic assistant. Answer this in 1 short sentence: {q}"
    ai_reply = model.invoke(prompt).content
    print(f"AI Bot:   {ai_reply}")

print(f"\n--- Result: Rules failed to answer {unanswered_by_rules} out of {len(questions)} questions ---")