"""
Task 2.5: AI Skills Toolkit
A reusable AI toolkit for a clinic/agency with summarizing, translating, and review replying skills.
Includes usage tracking, batch processing, and non-AI token estimation.
"""

from langchain.chat_models import init_chat_model

# 1. Create the models once at the top
# Why 1: Creating models outside functions prevents re-initializing them on every call, saving time and resources.
precise_model = init_chat_model("llama3.2", model_provider="ollama", temperature=0.1)
creative_model = init_chat_model("llama3.2", model_provider="ollama", temperature=0.7)

# 2. ask_ai function
def ask_ai(prompt: str, system: str = "You are a helpful assistant.", creative_mode: bool = False) -> str:
    """Picks the model, calls it, and returns the response text."""
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt}
    ]
    model = creative_model if creative_mode else precise_model
    response = model.invoke(messages)
    # Using .content to get the text, though older versions might use .text
    return response.content 

# 3. Three skills with type hints and docstrings
def summarize(text: str) -> str:
    """Summarizes the given text into one short sentence."""
    return ask_ai(f"Summarize this text in one very short sentence: {text}", system="You are an expert summarizer.", creative_mode=False)

# 4. Skill with a default parameter
def translate(text: str, language: str = "Urdu") -> str:
    """Translates text into the specified language."""
    return ask_ai(f"Translate this to {language}: {text}", system="You are a professional translator.", creative_mode=False)

def reply_to_review(review: str) -> str:
    """Writes a polite, creative reply to a customer review."""
    return ask_ai(f"Write a short, polite reply to this customer review: {review}", system="You are a customer service expert.", creative_mode=True)

# 5. Non-AI function with at least 2 assert tests
def estimate_tokens(text: str) -> int:
    """Estimates the number of tokens in a string (approx 4 chars per token) without calling AI."""
    # Why 2: We use simple math estimation instead of an API call to save money and time on rough counts.
    return round(len(text) / 4)

# Asserts for the non-AI function (will throw an error if math is wrong, otherwise does nothing)
assert estimate_tokens("1234") == 1
assert estimate_tokens("This is a test.") == 4

# Usage dictionary
usage = {"summarize": 0, "translate": 0, "reply": 0, "batch": 0}

print("City Care AI Toolkit. Commands: /summarize, /translate, /reply, /batch, bye")

# 6. Menu Loop
# Why 3: A while True loop keeps the toolkit running so staff can perform multiple tasks without restarting the script.
while True:
    raw_cmd = input("Command: ").strip().lower()
    
    if raw_cmd == "bye":
        break
        
    elif raw_cmd == "/summarize":
        user_text = input("Text to summarize: ").strip()
        print(f"AI: {summarize(user_text)}")
        usage["summarize"] += 1
        
    elif raw_cmd == "/translate":
        user_text = input("Text to translate: ").strip()
        lang = input("Language (Enter for Urdu): ").strip()
        if not lang:  # User just pressed Enter
            print(f"AI: {translate(user_text)}")
        else:
            print(f"AI: {translate(user_text, language=lang)}")
        usage["translate"] += 1
        
    elif raw_cmd == "/reply":
        user_review = input("Customer review: ").strip()
        ans = reply_to_review(user_review)
        tokens = estimate_tokens(user_review)
        print(f"AI: {ans}")
        print(f"    (review was about {tokens} tokens)")
        usage["reply"] += 1
        
    elif raw_cmd == "/batch":
        # Stretch goal: Run a skill over a list using a for loop and enumerate
        reviews = ["The clinic was very clean.", "Too expensive for a basic checkup.", "Doctor was late but helpful."]
        print("Running batch replies...")
        for idx, review in enumerate(reviews, start=1):
            print(f"{idx}. Review: {review}")
            print(f"   Reply: {reply_to_review(review)}")
        usage["batch"] += 1
        
    else:
        print("Unknown command. Try /summarize, /translate, /reply, /batch or bye.")

# Print the final counts with a for loop
print("\nSkills used today:")
for skill, count in usage.items():
    print(f"  {skill}: {count}")