import random
from datetime import datetime

def get_metrics(service_name: str):
    """
    Simulate fetching metrics from a monitoring system
    """
    return {
        "service": service_name,
        "timestamp": datetime.utcnow().isoformat(),
        "cpu_usage": random.randint(50, 95),
        "memory_usage": random.randint(60, 98),
        "error_rate": random.uniform(0.1, 5.0),
        "latency_ms": random.randint(100, 2000)
    }


def check_alerts(metrics: dict):
    """
    Simple rule-based alert detection
    """
    alerts = []

    if metrics["cpu_usage"] > 85:
        alerts.append("High CPU usage detected")

    if metrics["memory_usage"] > 90:
        alerts.append("High memory usage detected")

    if metrics["error_rate"] > 2.5:
        alerts.append("High error rate detected")

    if metrics["latency_ms"] > 1000:
        alerts.append("High latency detected")

    return alerts