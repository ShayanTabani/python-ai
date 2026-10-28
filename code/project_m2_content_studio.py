"""
Module 2 Checkpoint 1: AI Content Studio
A content studio for City Care Clinic that generates menus, writes streamed 
social media posts in different tones (including Roman Urdu), answers prices 
instantly, and chats with customers using memory.
"""

from langchain.chat_models import init_chat_model
import time
import sys

# 2. Config dictionary
config = {
    "model_name": "llama3.2",
    "memory_size": 8,
    "cloud_price_per_1k": 0.50  # Stretch/Bonus goal
}

# 3. Facts dictionary (5+ keys, 4+ prices including one 0)
facts = {
    "business_name": "City Care Clinic",
    "city": "Lahore",
    "hours": "10 am to 8 pm, Monday to Saturday",
    "delivery": "200 PKR delivery, free for orders above 3000 PKR",
    "contact": "0300-1122334",
    "prices": {
        "checkup": 1500,
        "blood test": 2000,
        "xray": 3500,
        "mri scan": 0  # 0 price means "coming soon"
    }
}

# 4. Tones dictionary for social media
tones = {
    "fun": "playful, highly energetic, and uses emojis.",
    "urgent": "urgent, emphasizing limited time or quick action.",
    "premium": "elegant, calm, and focused on high quality."
}

# 5. Two models created once
# Why: We use temperature 0.1 for chat to keep it factual, and 0.7 for creative tasks like posts
precise_model = init_chat_model(config["model_name"], model_provider="ollama", temperature=0.1)
creative_model = init_chat_model(config["model_name"], model_provider="ollama", temperature=0.7)

# 6. System message
system_msg_content = f"You are the assistant for {facts['business_name']}. Only use these facts: {facts}. If you do not know something, explicitly say 'I don't know'."
messages = [{"role": "system", "content": system_msg_content}]

# Trackers for the session report
report = {
    "chat_answers": 0,
    "menu_descriptions": 0,
    "posts": 0,
    "price_answers": 0,
    "total_tokens": 0,
    "total_seconds": 0.0
}

# 7. Header
print("==================================================")
print(f"   {facts['business_name']} AI Content Studio")
print("==================================================")
print("Commands: /menu, /post <tone>, /price <item>, /reset, bye")

# 8. Command loop
while True:
    raw_input = input("You: ")
    msg = raw_input.strip().lower()
    
    # 9. Empty input or bye
    if not msg:
        continue
    if msg == "bye":
        print("Studio: Goodbye!")
        break
        
    # --- C. /menu: Batch Descriptions ---
    elif msg == "/menu":
        menu_items = []
        # 10. Loop over prices, skip 0
        for item, price in facts["prices"].items():
            if price == 0:
                print(f"Studio: Skipping {item} (coming soon)")
                continue
                
            prompt = f"Write a catchy 1-sentence marketing description for our medical service: {item}"
            
            start_time = time.time()
            # 11. Use creative model
            response = creative_model.invoke(prompt)
            end_time = time.time()
            
            # 13. Accumulators
            report["total_tokens"] += response.usage_metadata["total_tokens"]
            report["total_seconds"] += (end_time - start_time)
            
            # 12. Collect results
            menu_items.append({
                "item": item.title(),
                "price": price,
                "desc": response.content.strip()
            })
            report["menu_descriptions"] += 1
            
        print("-" * 50)
        # Enumerate and print with commas
        for i, item_data in enumerate(menu_items, start=1):
            print(f"{i}. {item_data['item']} ({item_data['price']:,} PKR)")
            print(f"   {item_data['desc']}")
        print("-" * 50)
        
        # Bonus: Cloud cost estimate
        # Why: To show the client how much money they save by using our local Ollama model
        cloud_cost = (report["total_tokens"] / 1000) * config["cloud_price_per_1k"]
        print(f"Bonus Info: This menu cost 0 PKR locally. On the cloud, it would cost {cloud_cost:.2f} PKR.")
        
    # --- D. /post <tone>: Streamed Social Media Post ---
    elif msg.startswith("/post "):
        tone_name = msg.replace("/post ", "").strip()
        # 14. .get() with default
        tone_desc = tones.get(tone_name, "friendly and helpful")
        
        prompt = f"Write a short social media post for {facts['business_name']}. Tone: {tone_desc}. Mention we are in {facts['city']}."
        
        print(f"Studio ({tone_desc}):")
        
        start_time = time.time()
        english_post = ""
        # 15. Stream chunks
        for chunk in creative_model.stream(prompt):
            content = chunk.content
            print(content, end="")
            sys.stdout.flush()
            english_post += content
        end_time = time.time()
        print() 
        
        # Track usage for streaming (approximated based on output length for Ollama streams)
        approx_tokens = int(len(english_post) / 4) + 20 
        report["total_tokens"] += approx_tokens
        report["total_seconds"] += (end_time - start_time)
        report["posts"] += 1
        
        # Bonus: Roman Urdu translation
        print("\n--- Roman Urdu Version ---")
        urdu_prompt = f"Translate this exact post into Roman Urdu (Urdu written in English letters). Make it sound natural for Pakistanis:\n\n{english_post}"
        start_time2 = time.time()
        urdu_resp = precise_model.invoke(urdu_prompt)
        end_time2 = time.time()
        print(urdu_resp.content)
        report["total_tokens"] += urdu_resp.usage_metadata["total_tokens"]
        report["total_seconds"] += (end_time2 - start_time2)
        
    # --- E. /price <item> ---
    elif msg.startswith("/price "):
        item_name = msg.replace("/price ", "").strip()
        report["price_answers"] += 1
        
        # 16. Answer from dictionary
        # Why: Doing this directly saves AI tokens, time, and completely avoids hallucinations
        if item_name in facts["prices"]:
            item_price = facts["prices"][item_name]
            if item_price == 0:
                print(f"Studio: {item_name.title()} is coming soon.")
            else:
                print(f"Studio: {item_name.title()} costs {item_price:,} PKR.")
        else:
            print("Studio: Not on our menu.")
            
    # --- E. /reset ---
    elif msg == "/reset":
        # 19. Clear chat but keep system message
        messages = [messages[0]]
        print("Studio: Chat memory cleared.")
        
    # --- E. Chat with Memory ---
    else:
        # 17. Append user message
        messages.append({"role": "user", "content": raw_input})
        
        start_time = time.time()
        response = precise_model.invoke(messages)
        end_time = time.time()
        
        ai_reply = response.content
        print(f"Studio: {ai_reply}")
        
        messages.append({"role": "assistant", "content": ai_reply})
        # Trim memory
        messages = [messages[0]] + messages[1:][-config["memory_size"]:]
        
        # Track
        tokens_sent = response.usage_metadata["input_tokens"]
        report["total_tokens"] += response.usage_metadata["total_tokens"]
        report["total_seconds"] += (end_time - start_time)
        report["chat_answers"] += 1
        
        # 18. Print memory size and tokens sent
        print(f"        (memory: {len(messages)} messages, {tokens_sent} tokens sent)")

# --- F. Session Report ---
print("==================================================")
print("Session report")
print(f"Chat answers: {report['chat_answers']} | Menu descriptions: {report['menu_descriptions']} | Posts: {report['posts']} | Price answers: {report['price_answers']}")
print(f"AI usage: {report['total_tokens']:,} tokens in {report['total_seconds']:.1f} seconds")
print("==================================================")