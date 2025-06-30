from dotenv import load_dotenv
from ai_chain import improve_readme_content
from github_tool import fetch_and_push_readme
from email_reporter import send_commit_email
import re

load_dotenv(dotenv_path=".env")

def run_daily_readme_agent():
    import os
    from github import Github

    token = os.getenv("PAT_TOKEN")  # use PAT_TOKEN env variable
    print(f"PAT_TOKEN is set: {'Yes' if token else 'No'}")
    if token:
        print(f"Token preview: {token[:4]}{'*' * (len(token) - 8)}{token[-4:]}")
    else:
        print("⚠️ Warning: PAT_TOKEN is not set or empty.")
        raise ValueError("PAT_TOKEN environment variable not set")

    repo_name = os.getenv("REPO_NAME")
    branch = os.getenv("BRANCH", "main")

    g = Github(token)
    repo = g.get_repo(repo_name)

    try:
        file = repo.get_contents("README.md", ref=branch)
        old_content = file.decoded_content.decode()
    except Exception as e:
        print("❌ README.md not found. Listing root files:")
        try:
            root_files = repo.get_contents("/", ref=branch)
            print("📂 Files in root:", [f.path for f in root_files])
        except Exception as inner:
            print("⚠️ Could not list files:", inner)
        print("🛑 Error:", e)
        return

    new_content = improve_readme_content(old_content)
    result = fetch_and_push_readme(new_content)

    print(result)

    if "updated" in result.lower():
        # Extract the quote from the new_content
        quote_match = re.search(r"## 📅 Daily Quote\s*\n\s*> \"([^\"]+)\"", new_content)
        quote_text = quote_match.group(1) if quote_match else "Here's today's inspiring quote."

        subject = f"✅ AI Agent Commit on {repo_name}"
        body = (
            f"The README was updated and committed by the AI agent.\n\n"
            f"Here is today's quote:\n\n\"{quote_text}\""
        )
        send_commit_email(subject, body)

if __name__ == "__main__":
    run_daily_readme_agent()
