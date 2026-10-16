"""
Task 1.4: Business Prompt Builder
This script takes business details from the user and generates a ready-to-use AI prompt.
"""

# Get details from the client to personalize the prompt
user_name = input("Your name: ")
business_type = input("Business type: ")
biggest_problem = input("Biggest problem: ")

# Stretch Goal: Ask for budget to make the AI solutions more realistic
budget_str = input("Monthly budget in PKR: ")
budget = int(budget_str)

# Print a friendly welcome line
print(f"\nWelcome, {user_name}!")
print("--- Your AI Prompt ---")

# Combine all inputs into a single powerful prompt using f-strings
print(f"Suggest 3 AI solutions for a {business_type} that struggles with {biggest_problem}. Budget: {budget} PKR per month.")