"""
Task 1.8: Business Helper Bot (Module 1 Final)
A mini chatbot for City Care Clinic that handles common questions, 
tracks complaints, and provides a summary upon exiting.
"""

print("City Care Bot: Hi! Ask about timings, fees, location or appointments. Type 'bye' to exit.")

# 1. Ask the user's name once before starting the loop
user_name = input("City Care Bot: What is your name? ").strip().title()

# Trackers for the end-of-chat summary
total_messages = 0
unanswered_count = 0
complaint_count = 0  # Stretch Goal: track complaints

# 2. while True creates an infinite loop so the chat keeps going until 'break' is hit
while True:
    # Get user input and clean it with .strip().lower()
    raw_msg = input(f"{user_name}: ")
    msg = raw_msg.strip().lower()
    
    if not msg:
        continue
        
    total_messages += 1

    # 3. Exit rule
    # We use == for exact matching so 'bye' works but 'say bye' doesn't accidentally trigger it
    if msg == 'bye' or msg == 'exit':
        print(f"City Care Bot: Take care, {user_name}!")
        break
        
    # 4. Complaint or human-handover rule (comes first to catch urgent issues)
    elif "complaint" in msg or "late" in msg or "agent" in msg or "human" in msg:
        complaint_count += 1
        print("City Care Bot: Sorry about that. Connecting you to a human...")
        break  # Stretch Goal: ends the chat and hands over to a human
        
    # 5. Common intents (Timings, Fees, Location)
    elif "timing" in msg or "open" in msg or "hours" in msg:
        print("City Care Bot: We are open 10 am to 8 pm, Monday to Saturday.")
        
    elif "fee" in msg or "price" in msg or "cost" in msg:
        print("City Care Bot: Consultation fee is 2,000 PKR.")
        
    elif "location" in msg or "address" in msg or "where" in msg:
        print("City Care Bot: We are located at Main Boulevard, Lahore.")
        
    # 6. Fallback (Unanswered questions)
    # If no keywords match, we count it as unanswered and prep the AI prompt for Module 2
    else:
        unanswered_count += 1
        print("City Care Bot: I am not sure yet. In Module 2, an AI will answer:")
        print(f"Prompt -> You are the friendly assistant of City Care Clinic. Answer in 2 lines: {raw_msg}")

# 7. Summary printed after the loop breaks
print("========================================")
print(f"Chat summary: {total_messages} messages, {unanswered_count} unanswered.")
print(f"Complaints received: {complaint_count}")