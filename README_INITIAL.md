# AI README Agent Starter

This project automatically improves and updates `README.md` one time per day using Google Gemini AI.

## Setup

1. Copy `.env.example` to `.env` and fill it with:
   - `GITHUB_TOKEN` — GitHub PAT with `repo` scope
   - `GEMINI_API_KEY` — Google Gemini API key
   - `REPO_NAME` — `your-username/repo-name`
2. Push this repo to GitHub.
3. In **Settings → Secrets → Actions**, add:
   - `GITHUB_TOKEN`
   - `GEMINI_API_KEY`
4. Add an initial `README.md` in the root.
5. Await first GitHub Actions run (scheduled at 10:00 UTC daily).

Use the workflow_dispatch button to run it manually anytime.
