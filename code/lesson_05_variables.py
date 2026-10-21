"""This is the AI Model Profile Card."""
# Storing model profile using 4 core data types
model_name = "llama-3"       # str
context_window = 128000      # int
price_per_1k = 0.5           # float
runs_locally = True          # bool

# Printing variables and their types using f-strings and type()
print(f"Model: {model_name} | Type: {type(model_name)}")
print(f"Context Window: {context_window} | Type: {type(context_window)}")
print(f"Price per 1K tokens: ${price_per_1k} | Type: {type(price_per_1k)}")
print(f"Runs Locally: {runs_locally} | Type: {type(runs_locally)}\n")

# Asking user for tokens used and converting string input to int for math
tokens_used = int(input("How many tokens does a chat use? "))

# Calculating cost and rounding to 2 decimals
cost = (tokens_used / 1000) * price_per_1k
print(f"Estimated Cost: ${round(cost, 2)}")

# Stretch Goal: Monthly cost calculation
chats_per_day = int(input("How many chats per day? "))
monthly_cost = cost * chats_per_day * 30
print(f"Estimated Monthly Cost: ${round(monthly_cost, 2)}")