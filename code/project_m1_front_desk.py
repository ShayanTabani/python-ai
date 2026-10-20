"""
Module 1 Checkpoint 2 Project: AI Front Desk
A clinic assistant that handles FAQs, calculates service quotes, 
and safely routes complex questions to AI models.
"""

# Constants at the top in UPPER_CASE (Best practice for fixed values)
BOT_NAME = "City Care Bot"
HOME_VISIT_FEE = 500
FREE_VISIT_LIMIT = 5000
CLOUD_PRICE_PER_1K = 0.50  # Example PKR price

print("==================================================")
print(f"   {BOT_NAME}: rules, quotes and AI-ready prompts")
print("==================================================")
print("Ask anything, type /quote for a price, or bye to exit.")

# Ask user's name once and clean it
user_name = input(f"{BOT_NAME}: What is your name? ").strip().title()

# Trackers for the session report
total_msgs = 0
rules_answered = 0
unanswered = 0
quotes_count = 0
total_quoted_value = 0.0
total_ai_cost = 0.0
complaints = 0

# Infinite loop to keep the chat going until the user says bye
while True:
    raw_msg = input(f"{user_name}: ")
    msg = raw_msg.strip().lower()
    
    # If the user just presses Enter, ask again without counting it
    if not msg:
        continue
        
    total_msgs += 1
    
    # 1. Exit Rule
    if msg == "bye":
        print(f"{BOT_NAME}: Goodbye, {user_name}!")
        break
        
    # 2. Complaint / Handover Rule (Checked first so angry customers aren't delayed)
    elif "complaint" in msg or "late" in msg or "refund" in msg or "human" in msg or "agent" in msg:
        rules_answered += 1
        complaints += 1
        print(f"{BOT_NAME}: Sorry about that. Connecting you to a human...")
        break  # Bonus: Handover ends the chatbot session
        
    # 3. Quote System (/quote)
    elif msg == "/quote":
        rules_answered += 1
        item = input(f"{BOT_NAME}: Which item (checkup, blood test, xray)? ").strip().lower()
        qty_input = input(f"{BOT_NAME}: How many? ").strip()
        
        # Bonus: Safe quantity check to avoid ValueError crash
        if not qty_input.isdigit():
            print(f"{BOT_NAME}: Quantity must be a number. Please try /quote again.")
            continue
            
        qty = int(qty_input)
        
        # Determine price based on item
        if item == "checkup":
            price = 1500
        elif item == "blood test":
            price = 2000
        elif item == "xray":
            price = 3500
        else:
            print(f"{BOT_NAME}: Sorry, {item} is not on our menu.")
            continue
            
        subtotal = price * qty
        discount = 0
        
        # Discount Rule: 10% off for 3 or more items
        if qty >= 3:
            discount = subtotal * 0.10
            
        discounted_subtotal = subtotal - discount
        delivery = 0
        
        # Delivery Rule: charge fee if subtotal is below the limit
        if discounted_subtotal < FREE_VISIT_LIMIT:
            delivery = HOME_VISIT_FEE
            
        total = discounted_subtotal + delivery
        
        # Update quote trackers
        quotes_count += 1
        total_quoted_value += total
        
        # Print using :, to add thousand separators
        print(f"{BOT_NAME}: {qty} x {item} = {subtotal:,.0f} PKR")
        print(f"     Discount: -{discount:,.0f} PKR | Delivery: {delivery:,.0f} PKR")
        print(f"     Total: {total:,.0f} PKR")
        
    # 4. Specific FAQ Intents
    elif msg == "hi" or msg.startswith("hello"):
        rules_answered += 1
        print(f"{BOT_NAME}: Hello! How can I help you today?")
        
    elif "hours" in msg or "timing" in msg or "open" in msg:
        rules_answered += 1
        print(f"{BOT_NAME}: We are open 9 am to 10 pm, every day.")
        
    elif "location" in msg or "address" in msg or "where" in msg:
        rules_answered += 1
        print(f"{BOT_NAME}: We are located at Main Boulevard, Lahore.")
        
    elif "fee" in msg or "consultation" in msg or "price" in msg:
        rules_answered += 1
        print(f"{BOT_NAME}: Basic consultation is 1,500 PKR. Type /quote for exact costs.")
        
    # 5. Smart Fallback for anything else (AI Routing)
    else:
        unanswered += 1
        # Slice to 150 characters for safety and cost control
        clean_question = raw_msg.strip().capitalize()[:150]
        estimated_tokens = round(len(clean_question) / 4)
        
        # Route private details to local model
        if "phone" in msg or "cnic" in msg or "address" in msg:
            model = "llama3.2 (local, private)"
            cost = 0.0
        else:
            model = "small cloud model (cheap)"
            cost = (estimated_tokens / 1000) * CLOUD_PRICE_PER_1K
            
        total_ai_cost += cost
        
        print(f"{BOT_NAME}: Good question! Routed to: {model} (~{estimated_tokens} tokens)")
        print(f"     Prompt: You are the assistant of City Care Clinic.")
        print(f"     Answer {user_name} in 2 short lines. Question: {clean_question}")

# Session Report (Prints after the loop breaks)
print("==================================================")
print("Session report")
print(f"Messages: {total_msgs} | Answered by rules: {rules_answered} | Unanswered: {unanswered}")
print(f"Quotes: {quotes_count} | Quoted value: {total_quoted_value:,.0f} PKR")
print(f"Estimated AI cost for unanswered questions: {total_ai_cost:.4f} PKR")
if complaints > 0:
    print(f"Human Handovers (Complaints): {complaints}")
print("==================================================")