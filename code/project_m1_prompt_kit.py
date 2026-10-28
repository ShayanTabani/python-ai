"""
Module 1 Project: AI Prompt Kit (Upgraded for Module 2 Stretch Goal)
Now it actually sends the prompt to the AI and prints the real answer!
"""

from langchain.chat_models import init_chat_model

business_name = input("What is your business name? ")
business_type = input("What type of business is it? ")
target_audience = input("Who is your target audience? ")
main_problem = input("What problem do you solve? ")
budget = int(input("What is your marketing budget (in PKR)? "))

ai_prompt = f"""
Act as an expert marketer for a {business_type} called {business_name}.
The target audience is {target_audience} and we solve this problem: {main_problem}.
Our budget is {budget} PKR. Create a short marketing plan.
"""

print("\n--- Sending to AI... Please wait ---")
# Call the AI model directly
model = init_chat_model("llama3.2", model_provider="ollama", temperature=0.7)
response = model.invoke(ai_prompt)

print("\n--- AI Response ---")
print(response.content)