import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def improve_readme_content(old_content: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = (
        "You are an assistant that improves the clarity, tone, and structure of README files. "
        "Edit the text directly to sound more professional, engaging, and well-structured. "
        "⚠️ Do NOT explain the changes. "
        "⚠️ Do NOT use code blocks like ```markdown. "
        "Just return the full improved README text — nothing else.\n\n"
        f"README:\n{old_content}"
    )
    response = model.generate_content(prompt)
    return response.text.strip()
