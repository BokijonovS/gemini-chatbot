import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

chat = model.start_chat()
while True:
    user_input = input("You: ")
    if user_input != "stop":
        res = chat.send_message(user_input)
        print("Gemini: ", res.text, end='')
    else:
        break