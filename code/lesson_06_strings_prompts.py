"""This is the Prompt Cleaner script."""
# Get raw input from the user
raw_name = input("Enter your name: ")
raw_question = input("Enter your messy question (include 'stupid' to see it censored): ")

# Clean the text: remove extra spaces, fix capitalization, and replace bad words
clean_name = raw_name.strip().title()
clean_question = raw_question.strip().capitalize().replace("stupid", "*****")

# Calculate tokens (rule of thumb: 1 token = ~4 characters)
char_count = len(clean_question)
estimated_tokens = round(char_count / 4)

print(f"Characters: {char_count}, Estimated tokens: {estimated_tokens}")

# Check if python is mentioned (using lower() to catch any capitalization)
mentions_python = "python" in clean_question.lower()
print(f"Mentions 'python': {mentions_python}")

# Limit question to 150 chars to save tokens
short_question = clean_question[:150]

# Build final multi-line prompt using f-strings
prompt = f"""Hello {clean_name},
You asked: {short_question}
Let me help you with that!"""

print("\n--- Final Prompt ---")
print(prompt)