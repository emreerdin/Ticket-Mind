from google import genai
from dotenv import load_dotenv
import os

model_name = "gemini-2.5-flash-lite"
load_dotenv()
def llm_call(prompt, is_offline):
    if is_offline:
        return ""
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )

    return response.candidates[0].content.parts[0].text