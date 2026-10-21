"""
Task 1.7: Smart Model Router
This script routes user requests to the correct AI model (local, strong, or cheap) to save costs.
"""

# 1. Ask for task type and clean it
# .strip() removes accidental spaces and .lower() ensures " Code " and "code" are treated the same
raw_task = input("Task (code / private / chat): ")
task_type = raw_task.strip().lower()

# 2. Ask for estimated tokens and convert to integer
tokens = int(input("Estimated tokens: "))

# Stretch Goal: Ask if the user is a paid user
is_paid = input("Is this a paid user? (yes/no): ").strip().lower()

# 3 & 4. Use if / elif / else to choose the model and set the price
if task_type == "code":
    model = "claude (cloud, strong at code)"
    price_per_1k = 0.80
elif task_type == "private":
    model = "llama3.2 (local, Ollama)"
    price_per_1k = 0.00  # Local models don't cost money
else:
    model = "gpt-4o-mini (cloud, cheap chat)"
    price_per_1k = 0.10

# Calculate the total cost
cost = (tokens / 1000) * price_per_1k

# 5. Check length limits with warnings (Stretch goal included using 'and')
# We enforce a stricter limit for free users using the 'and' condition
if is_paid == "no" and tokens > 2000:
    print("Upgrade to send long requests.")
elif tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

# 6. Print the chosen model and cost
# :.2f ensures the cost always shows two decimal places, even if it's 0.00
print(f"Chosen model: {model}")
print(f"Estimated cost: {cost:.2f} PKR")