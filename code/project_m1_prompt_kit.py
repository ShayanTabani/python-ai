"""
Module 1 Project: AI Prompt Kit
This tool asks a local business owner for their details and generates ready-to-use AI prompts to help them with marketing, customer service, and growth.
"""

# Ask 5 questions to gather business context
biz_name = input("Business name: ")
biz_type = input("Business type (e.g. bakery): ")
city = input("City: ")
customers = input("Main customers (e.g. students, families): ")

# We convert budget to an integer to ensure it is treated as a number for any future calculations
budget_str = input("Monthly budget in PKR: ")
budget = int(budget_str)

# Print a clean header with the business name for a professional look
print("\n==========================================")
print(f"       AI Prompt Kit for {biz_name}")
print("==========================================\n")

# Build and print the prompts using f-strings
# We use f-strings here because they easily inject the specific user inputs directly into the prompt text

print("[1] Marketing")
print(f"Write a short Instagram post for {biz_name}, a {biz_type} in {city}.")
print(f"Target {customers}. Friendly tone, 1 call to action.\n")

print("[2] Customer Service")
print(f"You are the manager of {biz_name}. Write a polite reply to a customer")
print("whose order arrived late. Apologise and offer a small discount.\n")

print("[3] Growth")
print(f"Suggest 3 low-cost AI tools a {biz_type} in {city} can use")
print(f"to attract {customers} with a budget of {budget} PKR per month.\n")

# Adding a bonus 4th prompt to capture extra marks
print("[4] Online Review (Bonus)")
print(f"Write a professional and warm response to a 5-star Google review left for {biz_name}.")
print("Express gratitude and invite them to visit again soon.\n")