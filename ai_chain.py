import os
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def improve_readme_content(old_content: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Generate the daily motivational quote
    prompt = (
        "Generate one short, elegant motivational quote without author name. "
        "Keep it simple, positive, and powerful."
    )
    response = model.generate_content(prompt)
    quote = response.text.strip().strip('"')

    # Format current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    # Replace the daily quote section
    if "## 📅 Daily Quote" in old_content:
        before, _ = old_content.split("## 📅 Daily Quote", 1)
        new_section = f"## 📅 Daily Quote\n\n> \"{quote}\"\n\n*🕒 Updated on {timestamp}*"
        return before + new_section
    else:
        # If section not found, append
        return old_content + f"\n\n## 📅 Daily Quote\n\n> \"{quote}\"\n\n*🕒 Updated on {timestamp}*"
