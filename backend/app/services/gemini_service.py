import google.generativeai as genai
from app.config import GEMINI_API_KEY


print("Loaded API Key:", GEMINI_API_KEY)


genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")


def ask_gemini(prompt: str) -> str:
    """
    Sends prompt to Gemini and returns response.
    """

    try:

        response = model.generate_content(prompt)

        print("Gemini raw response:", response)

        return response.text

    except Exception as e:

        print("ERROR:", str(e))

        return f"Error occurred: {str(e)}"