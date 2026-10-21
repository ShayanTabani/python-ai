"""
Task 1.7: Smart Model Router
This script routes user requests to the correct AI model (local, strong, or cheap) to save costs.
"""

# 1. Ask for task type and clean it
raw_task = input("Task (code / private / chat): ")
task_type = raw_task.strip().lower()

# 2. Ask for estimated tokens and convert to integer
try:
    tokens = int(input("Estimated tokens: "))
except ValueError:
    print("Invalid token count! Defaulting to 1000 tokens.")
    tokens = 1000

# Stretch Goal: Ask if the user is a paid user (handles 'yes', 'y', 'no', 'n')
paid_input = input("Is this a paid user? (yes/no): ").strip().lower()
is_paid = paid_input in ["yes", "y"]

# 3 & 4. Use if / elif / else to choose the model and set the price
if task_type == "code":
    model = "claude (cloud, strong at code)"
    price_per_1k = 0.80
elif task_type == "private":
    model = "llama3.2 (local, Ollama)"
    price_per_1k = 0.00  # Local models don't cost money
elif task_type == "chat":
    model = "gpt-4o-mini (cloud, cheap chat)"
    price_per_1k = 0.10
else:
    # Fallback for unrecognized task type
    print(f"Unknown task '{task_type}', defaulting to chat model.")
    model = "gpt-4o-mini (cloud, cheap chat)"
    price_per_1k = 0.10

# Calculate the total cost
cost = (tokens / 1000) * price_per_1k

# 5. Check length limits with warnings (Stretch goal included)
print("\n--- Request Status ---")
if not is_paid and tokens > 2000:
    print("Limit Warning: Free tier limit is 2,000 tokens. Upgrade to send long requests.")
elif tokens > 4000:
    print("Warning: Long request (>4,000 tokens), consider shortening it to reduce latency.")
else:
    print("Length is fine.")

# 6. Print the chosen model and cost
print(f"Chosen model: {model}")
print(f"Estimated cost: {cost:.2f} PKR")  # Agar assignment me $ tha to PKR ki jagah $ laga lena