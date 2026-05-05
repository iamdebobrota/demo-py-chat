# import requests

# response = requests.get('https://api.github.com')
# print("status code: ", response.status_code)
# print("Data: ", response.json())


import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-3-flash-preview")

print("AI started (type 'exit' to stop) \n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chat ended.")
        break
    
    response = model.generate_content(user_input)

    print("AI: ", response.text)




