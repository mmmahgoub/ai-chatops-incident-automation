from app.services.log_analyzer import read_logs
from app.services.ai_engine import summarize_logs
from app.services.remediation import suggest_fix
from app.integrations.monitoring import get_metrics, check_alerts

def handle_query(query: str) -> str:
    if "error" in query or "incident" in query:
        logs = read_logs()
        print("DEBUG logs loaded")

        metrics = get_metrics("payment-service")
        print("DEBUG metrics:", metrics)

        alerts = check_alerts(metrics)

        analysis = summarize_logs(logs, metrics)
        print("DEBUG analysis:", analysis)

        fix = suggest_fix(analysis)

        return f"""
🚨 Alerts: {alerts}

📊 Metrics:
CPU: {metrics['cpu_usage']}%
Memory: {metrics['memory_usage']}%
Latency: {metrics['latency_ms']}ms

🧠 AI Analysis:
{analysis}

🔧 Suggested Action:
{fix}
"""

    return "Query not recognized."