"""This is the Prompt Cleaner script."""
# Get raw input from the user
raw_name = input("Enter your name: ")
raw_question = input("Enter your messy question (include 'stupid' to see it censored): ")

# Clean the text: fix capitalization, and replace bad words (Stretch Goal part 1)
clean_name = raw_name.strip().title()
clean_question = raw_question.strip().capitalize().replace("stupid", "*****")

# Calculate tokens
char_count = len(clean_question)
estimated_tokens = round(char_count / 4)

# Calculate estimated cost (Stretch Goal part 2)
estimated_cost = estimated_tokens * 0.05

print(f"Characters: {char_count}, Estimated tokens: {estimated_tokens}")

# Print the cost with exactly 2 decimal places using :.2f
print(f"Estimated Cost: {estimated_cost:.2f} PKR")

# Check if python is mentioned
mentions_python = "python" in clean_question.lower()
print(f"Mentions 'python': {mentions_python}")

# Limit question to 150 chars
short_question = clean_question[:150]

# Build final multi-line prompt
prompt = f"""Hello {clean_name},
You asked: {short_question}
Let me help you with that!"""

print("\n--- Final Prompt ---")
print(prompt)