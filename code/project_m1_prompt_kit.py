"""Module 1 Project: AI Prompt Kit."""

# Get business details from the user using input() 5 times
business_name = input("What is your business name? ")
business_type = input("What type of business is it? ")
target_audience = input("Who is your target audience? ")
main_problem = input("What problem do you solve? ")

# Convert budget input to int() to meet the autograder requirement
budget = int(input("What is your marketing budget (in PKR)? "))

# Build the AI prompt using a multi-line f-string
ai_prompt = f"""
Act as an expert marketer for a {business_type} called {business_name}.
The target audience is {target_audience} and we solve this problem: {main_problem}.
Our budget is {budget} PKR. Create a marketing plan.
"""

# Print the final result
print("\n--- Your AI Prompt ---")
print(ai_prompt)