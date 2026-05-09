# 🏗️ Architecture — SOC Automation Lab

---

## 🖥️ Virtual Machines

All VMs run on **VMware Workstation** on a Host-only network (VMnet1) `192.168.228.0/24` with NAT for external API access.

| VM | IP | OS | RAM | Role |
|---|---|---|---|---|
| Wazuh Server | 192.168.228.10 | Ubuntu 24.04 | 4 GB | SIEM · Active Response · Grafana |
| Windows 10 | 192.168.228.20 | Windows 10 | 4 GB | Victim endpoint |
| Kali Linux | 192.168.228.30 | Kali Linux | 4 GB | Attacker |
| TheHive + Cortex | 192.168.228.40 | Ubuntu 24.04 | 8 GB | Case management · IOC enrichment |
| n8n | 192.168.228.50 | Ubuntu 24.04 | 2 GB | SOAR orchestration |

---
<img width="1800" height="2200" alt="Untitled design" src="https://github.com/user-attachments/assets/dd224e7c-4b84-43a7-b902-22f242692e37" />


## 🔌 Services & Ports

| VM | Service | Port |
|---|---|---|
| Wazuh Server | Wazuh Manager | 1514 |
| Wazuh Server | Wazuh Dashboard | 443 |
| Wazuh Server | OpenSearch | 9200 |
| Wazuh Server | Grafana | 3000 |
| TheHive VM | Cassandra | 9042 |
| TheHive VM | TheHive | 9000 |
| TheHive VM | Cortex | 9001 |
| n8n VM | n8n | 5678 |
| Windows 10 | OpenSSH | 22 |
| Windows 10 | FTP | 21 |
| Windows 10 | SMB | 445 |
| Windows 10 | RDP | 3389 |

---

## 🔁 Full Pipeline

```
KALI attacks Windows 10
        │
        ▼
Sysmon logs every event in detail
        │
        ▼
Wazuh Agent reads logs → forwards to Wazuh Server
        │
        ▼
Wazuh Server evaluates ruleset → alert fires
        │
        ├─── PATH A: ACTIVE RESPONSE (instant, automated)
        │         Rule 60204 fires (level 10)
        │         Wazuh tells Windows Agent → run netsh.exe
        │         Windows Firewall blocks 192.168.228.30 for 300s
        │         Attack stops. Zero human intervention.
        │
        └─── PATH B: INTEGRATION PIPELINE
                  Wazuh runs custom-thehive.py
                  Script sends alert to:
                    → TheHive directly (raw alert creation)
                    → n8n webhook (SOAR pipeline start)
                          │
                          ├── Slack notification (SOC channel)
                          ├── Code Node → risk score + MITRE mapping
                          ├── TheHive enriched alert
                          └── Gmail email with risk label + MITRE details
                                │
                                ▼
                  Analyst opens TheHive alert
                  Adds attacker IP as observable
                  Clicks Run Analyzers
                          │
                          ├── Cortex → AbuseIPDB (IP reputation)
                          └── Cortex → VirusTotal (hash/URL scan)
                                │
                                ▼
                  Enriched IOC results returned to TheHive case
                          │
                          ▼
                  Grafana dashboard updates in real time
```

---

## ⚙️ n8n Workflow Nodes

| Node | Type | Function |
|---|---|---|
| Webhook | Trigger | Receives raw Wazuh alert JSON from custom-thehive.py |
| HTTP Request | Action | Posts alert notification to Slack SOC channel |
| Code (JavaScript) | Transform | Calculates risk score + maps MITRE ATT&CK tactics |
| HTTP Request | Action | Creates enriched alert in TheHive |
| Send Email | Action | Sends formatted Gmail alert with risk label and MITRE details |

### n8n Code Node — JavaScript

This is the full logic inside the n8n Code node. It filters low-severity alerts, calculates a dynamic risk score, and maps MITRE ATT&CK tactics.

```javascript
const webhookData = $('Webhook').item.json;
const level = webhookData.body.rule.level || 0;

// Only process level 10+ alerts
if (level < 10) return [];

const rule = webhookData.body.rule;
const agent = webhookData.body.agent;
const mitre = rule.mitre || {};
const tactics = mitre.tactic || [];
const techniques = mitre.technique || [];

// Dynamic risk scoring
let riskScore = rule.level || 0;
if (tactics.includes('Credential Access'))   riskScore += 20;
if (tactics.includes('Privilege Escalation')) riskScore += 25;
if (tactics.includes('Defense Evasion'))     riskScore += 20;
if (tactics.includes('Lateral Movement'))    riskScore += 30;
if (tactics.includes('Exfiltration'))        riskScore += 35;
if (tactics.includes('Impact'))              riskScore += 30;
riskScore = Math.min(riskScore, 100);

let riskLabel;
if (riskScore >= 75)      riskLabel = 'CRITICAL';
else if (riskScore >= 50) riskLabel = 'HIGH';
else if (riskScore >= 25) riskLabel = 'MEDIUM';
else                      riskLabel = 'LOW';

return {
  rule,
  agent,
  timestamp: webhookData.body.timestamp,
  sourceRef: 'n8n-' + rule.id + '-' + Date.now(),
  riskScore,
  riskLabel,
  mitreTactics: tactics.join(', ') || 'N/A',
  mitreTechniques: techniques.join(', ') || 'N/A',
};
```

---

## 📋 Wazuh Rule Reference

| Rule ID | Description | Level | MITRE Technique |
|---|---|---|---|
| 60122 | Logon failure — bad password | 5 | T1110 |
| 60204 | Multiple Windows logon failures | 10 | T1110 |
| 60115 | User account locked out | 9 | T1110 |
| 60106 | SSH brute force | 10 | T1110 |
| 60104 | FTP/RDP brute force | 5 | T1110 |
| 92026 | reg.exe SAM hive dump | 14 | T1003.002 |
| 92039 | net.exe account discovery | 3 | T1087 |
| 91816 | PowerShell env variable query | 4 | T1082 |
| 92043 | Netsh used to add firewall rule | 10 | — |

---

## 📁 Key Files

| File | Location on VM | Purpose |
|---|---|---|
| custom-thehive.py | /var/ossec/integrations/ | Sends alerts to TheHive and n8n webhook |
| ossec.conf | /var/ossec/etc/ | Wazuh config — active response + integration blocks |
| sysmonconfig.xml | C:\Sysmon\ | SwiftOnSecurity config for enhanced Windows telemetry |

---

## 🔒 Active Response Config

The relevant blocks added to `/var/ossec/etc/ossec.conf`:

```xml
<command>
  <name>netsh</name>
  <executable>netsh.exe</executable>
  <timeout_allowed>yes</timeout_allowed>
</command>

<active-response>
  <command>netsh</command>
  <location>local</location>
  <rules_id>60122,60204,60115</rules_id>
  <timeout>300</timeout>
</active-response>

<integration>
  <name>custom-thehive</name>
  <level>7</level>
  <alert_format>json</alert_format>
</integration>
```
