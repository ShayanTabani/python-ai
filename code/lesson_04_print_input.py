# Taking inputs to customize the AI prompt based on user's specific business needs
name = input("What is your name? ")
business = input("Enter your business type (e.g. bakery): ")
problem = input("Enter one problem you face: ")

# Using f-string to inject variables into the text for the LLM
prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}."

print(f"\nWelcome, {name}!")
print("Here is your prompt:")
print(prompt)