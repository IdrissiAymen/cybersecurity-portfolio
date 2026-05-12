#!/usr/bin/env python3
"""
custom-thehive.py — Wazuh integration script
Location:    /var/ossec/integrations/custom-thehive
Permissions: chmod +x, owner root:wazuh
"""

import sys
import json
import requests
from datetime import datetime

THEHIVE_URL     = "http://192.168.228.40:9000"
THEHIVE_API_KEY = "YOUR_API_KEY_HERE"
N8N_WEBHOOK     = "http://192.168.228.50:5678/webhook/YOUR_WEBHOOK_ID"


def map_severity(level):
    if level >= 12:
        return 3
    elif level >= 7:
        return 2
    return 1


def send_to_n8n(alert):
    try:
        r = requests.post(
            N8N_WEBHOOK,
            headers={"Content-Type": "application/json"},
            json=alert,
            timeout=10
        )
        print(f"[+] n8n: {r.status_code}")
    except Exception as e:
        print(f"[-] n8n error: {e}")


def create_thehive_alert(alert):
    try:
        rule  = alert.get("rule", {})
        agent = alert.get("agent", {})
        mitre = rule.get("mitre", {})
        ts    = alert.get("timestamp", datetime.now().isoformat())

        payload = {
            "title": f"Wazuh Alert: {rule.get('description', 'No description')}",
            "description": (
                f"Rule ID:    {rule.get('id')}\n"
                f"Level:      {rule.get('level')}\n"
                f"Agent:      {agent.get('name')} ({agent.get('ip')})\n"
                f"Time:       {ts}\n"
                f"Tactics:    {', '.join(mitre.get('tactic',    ['N/A']))}\n"
                f"Techniques: {', '.join(mitre.get('technique', ['N/A']))}"
            ),
            "type":      "Wazuh",
            "source":    "Wazuh SIEM",
            "sourceRef": f"wazuh-{rule.get('id')}-{ts}",
            "severity":  map_severity(rule.get("level", 0)),
            "tags":      ["wazuh", f"rule-{rule.get('id')}", agent.get("name", "unknown")],
            "tlp":       2
        }

        headers = {
            "Authorization": f"Bearer {THEHIVE_API_KEY}",
            "Content-Type":  "application/json"
        }

        r = requests.post(
            f"{THEHIVE_URL}/api/v1/alert",
            headers=headers,
            json=payload,
            verify=False,
            timeout=10
        )

        if r.status_code == 201:
            print(f"[+] TheHive alert created: {r.json().get('_id')}")
        else:
            print(f"[-] TheHive {r.status_code}: {r.text}")

    except Exception as e:
        print(f"[-] Exception: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: custom-thehive <alert_file>")
        sys.exit(1)

    try:
        with open(sys.argv[1]) as f:
            alert = json.load(f)
    except Exception:
        alert = json.loads(sys.argv[1])

    create_thehive_alert(alert)
    send_to_n8n(alert)
