from openai import OpenAI
import os
from app.utils.helpers import build_prompt, truncate_text

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_logs(logs: str, metrics: dict = None) -> str:
    try:
        logs = truncate_text(logs, 1000)
        prompt = build_prompt(logs, metrics)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI analysis failed: {str(e)}"