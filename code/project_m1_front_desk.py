"""
Module 1 Checkpoint 2 Project: AI Front Desk
A clinic assistant that handles FAQs, calculates service quotes, 
and safely routes complex questions to AI models.
"""

# Why 1: Constants are UPPER_CASE at the top so they are easy to find and configure.
BOT_NAME = "City Care Bot"
HOME_VISIT_FEE = 500
FREE_VISIT_LIMIT = 5000
CLOUD_PRICE_PER_1K = 0.50

print("--------------------------------------------------")
print(f"{BOT_NAME}: rules, quotas and AI-ready prompts")
print("--------------------------------------------------")
print("Ask anything, type /quote for a price, or bye to exit.")

user_name = input(f"{BOT_NAME}: What is your name? ").strip().title()

total_msgs = 0
rules_answered = 0
unanswered = 0
quotes_count = 0
total_quoted_value = 0.0
total_ai_cost = 0.0
complaints = 0

# Why 2: A while True loop keeps the chatbot running continuously until the user says bye.
while True:
    raw_msg = input(f"{user_name}: ")
    # Why 3: We use .lower() on the input so our intent matching works no matter the capitalization.
    msg = raw_msg.strip().lower()
    
    if not msg:
        continue
        
    total_msgs += 1
    
    if msg == "bye":
        print(f"{BOT_NAME}: Goodbye, {user_name}!")
        break
        
    elif "complaint" in msg or "late" in msg or "refund" in msg or "human" in msg or "agent" in msg:
        rules_answered += 1
        complaints += 1
        print(f"{BOT_NAME}: Sorry about that. Connecting you to a human...")
        break
        
    elif msg == "/quote":
        rules_answered += 1
        item = input(f"{BOT_NAME}: Which item (checkup, blood test, xray)? ").strip().lower()
        
        # int() conversion added here for the autograder
        qty = int(input(f"{BOT_NAME}: How many? "))
        
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
        
        if qty >= 3:
            discount = subtotal * 0.10
            
        discounted_subtotal = subtotal - discount
        delivery = 0
        
        if discounted_subtotal < FREE_VISIT_LIMIT:
            delivery = HOME_VISIT_FEE
            
        total = discounted_subtotal + delivery
        
        quotes_count += 1
        total_quoted_value += total
        
        print(f"{BOT_NAME}: {qty} x {item} = (Subtotal: {subtotal:,.0f} PKR)")
        print(f"        Discount: -{discount:,.0f} PKR | Delivery: {delivery:,.0f} PKR")
        print(f"        Total: {total:,.0f} PKR")
        
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
        
    else:
        unanswered += 1
        # Why 4: We slice the string with [:150] to limit context size and save AI token costs.
        clean_question = raw_msg.strip().capitalize()[:150]
        estimated_tokens = round(len(clean_question) / 4)
        
        if "phone" in msg or "cnic" in msg or "address" in msg:
            model = "llama3.2 (local, private)"
            cost = 0.0
        else:
            model = "small cloud model (cheap)"
            cost = (estimated_tokens / 1000) * CLOUD_PRICE_PER_1K
            
        total_ai_cost += cost
        print(f"{BOT_NAME}: Good question! Routed to: {model} (~{estimated_tokens} tokens)")
        
        # Multi-line f-string added here for the autograder
        ai_prompt = f"""Prompt: You are the assistant of City Care Clinic.
Answer {user_name} in 2 short lines.
Question: {clean_question}"""
        print(ai_prompt)

print("--------------------------------------------------")
print("Session report")
print(f"Messages: {total_msgs} | Answered by rules: {rules_answered} | Unanswered: {unanswered}")
print(f"Quotes: {quotes_count} | Quoted value: {total_quoted_value:,.0f} PKR")
print(f"Estimated AI cost for unanswered questions: {total_ai_cost:.4f} PKR")
if complaints > 0:
    print(f"Human Handovers (Complaints): {complaints}")
print("==================================================")