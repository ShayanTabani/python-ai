"""
Task 2.4: Batch Product Writer
Automatically writes one-sentence descriptions for all priced products in a dictionary,
skipping free/zero-price items to save tokens.
"""

from langchain.chat_models import init_chat_model
import time

# 1. Dictionary of at least 5 products, including one with price 0
products = {
    "Checkup": 1500,
    "Blood Test": 2000,
    "Xray": 3500,
    "MRI Scan": 8000,
    "Free BP Check": 0  # 0 price item
}

# 3. Create the model once, before the loop
model = init_chat_model("llama3.2", model_provider="ollama", temperature=0.5)

# 4. Collect results in a list of dictionaries
results = []

# 5. Token and time accumulators
total_tokens = 0
total_seconds = 0.0

# 2. Loop with .items()
for name, price in products.items():
    if price == 0:
        # Why: We use 'continue' to skip the AI call for 0-price items, saving time and tokens
        print(f"Skipping {name} (no price)")
        continue
        
    system_msg = f"Write a catchy one-sentence description for a medical service called '{name}'. Keep it under 15 words."
    
    start_time = time.time()
    response = model.invoke(system_msg)
    end_time = time.time()
    
    # Calculate stats
    total_tokens += response.usage_metadata["total_tokens"]
    total_seconds += (end_time - start_time)
    
    # Store result
    results.append({
        "item": name,
        "price": price,
        "text": response.content.strip()
    })

# 6. Print numbered menu using enumerate
print("==================================================")
# Why: enumerate(start=1) automatically numbers our items starting from 1 instead of 0
for i, entry in enumerate(results, start=1):
    print(f"{i}. {entry['item']} ({entry['price']} PKR)")
    print(f"   {entry['text']}")
print("==================================================")

# Print summary line
print(f"{len(results)} descriptions, {total_tokens} tokens, {total_seconds:.1f} seconds")