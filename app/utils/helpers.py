import datetime
import json


def format_timestamp(ts=None):
    """
    Returns a formatted UTC timestamp
    """
    if not ts:
        ts = datetime.datetime.utcnow()
    return ts.strftime("%Y-%m-%d %H:%M:%S UTC")


def pretty_json(data: dict):
    """
    Formats dictionary into readable JSON string
    """
    return json.dumps(data, indent=2)


def truncate_text(text: str, max_length: int = 500):
    """
    Truncate long text (useful for logs / AI prompts)
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "... [truncated]"


def build_prompt(logs: str, metrics: dict = None):
    """
    Build structured prompt for LLM
    """
    prompt = "Analyze the following system data:\n\n"

    if metrics:
        prompt += f"Metrics:\n{pretty_json(metrics)}\n\n"

    prompt += f"Logs:\n{logs}\n\n"
    prompt += "Provide root cause and suggested fix."

    return prompt


def safe_get(dictionary: dict, key: str, default=None):
    """
    Safe dictionary access
    """
    return dictionary.get(key, default)