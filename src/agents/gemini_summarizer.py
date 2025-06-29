import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-pro")

def summarize(text):
    prompt = f"Summarize the following research abstract in 3–4 lines:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text
