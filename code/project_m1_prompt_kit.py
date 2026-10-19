"""
Task 1.6: Prompt Cleaner
This script cleans messy user input, calculates tokens, safely sizes the prompt, and formats it for the AI.
"""

# 1. Ask the user for their name and a messy question
raw_name = input("Your name: ")
raw_question = input("Your question: ")

# 2. Clean the inputs
# .strip() removes extra spaces at the start/end, .title() capitalizes each word, and .capitalize() capitalizes only the first letter
clean_name = raw_name.strip().title()
clean_question = raw_question.strip().capitalize()

# Stretch Goal: Replace a bad word before building the prompt
clean_question = clean_question.replace("stupid", "***")

# 3. Calculate characters and estimated tokens (1 token is roughly 4 chars)
char_count = len(clean_question)
estimated_tokens = round(char_count / 4)

# 4. Check if "python" is mentioned using .lower() so it catches "PYTHON", "Python", etc.
mentions_python = "python" in clean_question.lower()

# Stretch Goal: Calculate estimated cost (e.g., 0.05 PKR per token)
estimated_cost = estimated_tokens * 0.05

# Print the cleaned data and stats
print("========================================")
print(f"Cleaned question: {clean_question}")
print(f"Characters: {char_count}, about {estimated_tokens} tokens")
print(f"Mentions Python: {mentions_python}")
print("========================================")

# 5. Build and print the multi-line f-string prompt
# We use slicing [:150] on the question to ensure it's limited to 150 characters, keeping the prompt safe and cheap
# We use :.2f to format the cost to exactly 2 decimal places
prompt = f"""You are a friendly Python tutor.
Greet {clean_name} by name and answer in 3 short lines.
Question: {clean_question[:150]}

(Estimated cost: {estimated_cost:.2f} PKR)"""

print(prompt)