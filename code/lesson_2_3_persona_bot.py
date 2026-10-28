"""
Task 2.3: Persona Bot with Real Facts
A clinic/business bot that uses a facts dictionary to answer price queries accurately, 
switches personas, and allows adding new items dynamically (Stretch Goal).
"""

from langchain.chat_models import init_chat_model

# 1. A facts dictionary for your business
facts = {
    "business_name": "City Care Clinic",
    "location": "Main Boulevard, Lahore",
    "timings": "9 am to 10 pm",
    "contact": "0300-1234567",
    "prices": {
        "checkup": 1500,
        "blood test": 2000,
        "xray": 3500
    }
}

# 2. A personas dictionary with at least 3 styles
personas = {
    "friendly": "warm, welcoming, and uses emojis.",
    "formal": "highly professional, polite, and brief.",
    "sales": "persuasive, always suggests getting a full body checkup."
}

# 4. config dictionary for the model
config = {
    "model_name": "llama3.2",
    "temperature": 0.4,
    "memory_size": 8
}

model = init_chat_model(config["model_name"], model_provider="ollama", temperature=config["temperature"])

def build_system_msg():
    # 3. Build the system message from facts and strictly tell AI to only use these facts
    return f"You are the assistant for {facts['business_name']}. Only use these facts: {facts}. Style: {current_persona_style}"

current_persona_style = personas["friendly"]
messages = [{"role": "system", "content": build_system_msg()}]

print("Bot ready. Commands: /persona friendly|formal|sales, /price <item>, /add <item> <price>, bye")

while True:
    raw_msg = input("You: ")
    msg = raw_msg.strip().lower()
    
    if msg == "bye":
        print("Bot: Goodbye!")
        break
        
    # 5. Change persona
    elif msg.startswith("/persona "):
        persona_name = msg.replace("/persona ", "").strip()
        # Why: .get() with a default prevents a KeyError crash if the user types a wrong persona name
        current_persona_style = personas.get(persona_name, "helpful and standard")
        messages[0]["content"] = build_system_msg()
        print(f"Bot: Style changed to: {current_persona_style}")
        continue
        
    # Stretch Goal: Add a new item and rebuild system message
    elif msg.startswith("/add "):
        try:
            parts = msg.replace("/add ", "").strip().rsplit(" ", 1)
            new_item, new_price = parts[0], int(parts[1])
            facts["prices"][new_item] = new_price
            messages[0]["content"] = build_system_msg()
            print(f"Bot: Added {new_item} for {new_price} PKR. AI updated!")
        except Exception:
            print("Bot: Invalid format. Use /add item price")
        continue

    # 6. /price answers directly from dictionary without AI
    elif msg.startswith("/price "):
        item_name = msg.replace("/price ", "").strip()
        # Why: We check if the exact item exists in our facts dictionary to avoid AI hallucinations
        if item_name in facts["prices"]:
            print(f"Bot: {item_name.capitalize()} costs {facts['prices'][item_name]} PKR.")
        else:
            print(f"Bot: Sorry, {item_name} is not on our menu.")
        continue
        
    messages.append({"role": "user", "content": raw_msg})
    
    response = model.invoke(messages)
    print(f"Bot: {response.content}")
    
    messages.append({"role": "assistant", "content": response.content})
    messages = [messages[0]] + messages[1:][-config["memory_size"]:]