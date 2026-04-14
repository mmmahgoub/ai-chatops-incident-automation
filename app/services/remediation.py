def suggest_fix(analysis: str) -> str:
    if "database" in analysis.lower():
        return "Restart DB connections or increase pool size."
    elif "memory" in analysis.lower():
        return "Restart service or scale memory."
    return "Investigate manually."