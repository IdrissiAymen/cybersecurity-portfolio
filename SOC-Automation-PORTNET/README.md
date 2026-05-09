# 🛡️ SOC Automation Lab — End-to-End Detection & Response Pipeline

[![Status](https://img.shields.io/badge/Status-Complete-brightgreen)](https://github.com/IdrissiAymen)
[![Platform](https://img.shields.io/badge/Platform-VMware_Workstation-blue)](https://github.com/IdrissiAymen)
[![SIEM](https://img.shields.io/badge/SIEM-Wazuh_4.x-red)](https://wazuh.com)
[![SOAR](https://img.shields.io/badge/SOAR-n8n_2.11.4-orange)](https://n8n.io)
[![License](https://img.shields.io/badge/License-Educational-green)](https://github.com/IdrissiAymen)

> Developed as a **4th Year Project (PFA)** during a Cybersecurity internship at **Portnet S.A., Morocco**  a fully operational SOC pipeline built from the ground up across 5 VMware virtual machines. This project replicates real-world SOC operations: threat detection, automated containment, SOAR-driven alert enrichment, dynamic risk scoring, MITRE ATT&CK mapping, and live security monitoring built entirely on enterprise-grade open-source tools with no managed services or cloud shortcuts.

---

## ⚡ What Happens When Kali Attacks

When Kali Linux launches a brute force attack against the Windows 10 victim, the following happens **automatically — zero human intervention:**

```
1. Wazuh         →  Detects the attack within seconds (rule 60204, level 10)
2. Windows FW    →  Auto-blocks attacker IP via netsh (active response, 300s)
3. Slack         →  Instant SOC channel notification
4. n8n           →  Calculates dynamic risk score (0–100) + maps MITRE ATT&CK tactics
5. TheHive       →  Receives a fully enriched, structured alert
6. Gmail         →  Formatted email with risk label, MITRE details, agent info
7. Grafana       →  Live security dashboard updates in real time
```

The analyst then opens the TheHive alert, adds the attacker IP as an observable, and triggers **Cortex** (AbuseIPDB + VirusTotal) for deep IOC enrichment — all from the same interface.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    ATTACK PHASE                         │
│  Kali Linux (192.168.228.30)                            │
│  └─ Hydra / smbclient / reg.exe / PowerShell            │
└───────────────────────┬─────────────────────────────────┘
                        │ brute force / credential attacks
                        ▼
┌─────────────────────────────────────────────────────────┐
│                 VICTIM ENDPOINT                         │
│  Windows 10 (192.168.228.20)                            │
│  └─ Wazuh Agent + Sysmon (SwiftOnSecurity config)       │
└───────────────────────┬─────────────────────────────────┘
                        │ events forwarded in real time
                        ▼
┌─────────────────────────────────────────────────────────┐
│              SIEM + ACTIVE RESPONSE                     │
│  Wazuh Server (192.168.228.10)                          │
│  ├─ Ruleset evaluation → alert fired                    │
│  ├─ PATH A: Active Response → netsh.exe → IP blocked    │
│  └─ PATH B: custom-thehive.py integration               │
└──────────────┬──────────────────────┬───────────────────┘
               │                      │
               ▼                      ▼
┌──────────────────────┐  ┌──────────────────────────────┐
│  TheHive (direct)    │  │  n8n Webhook (192.168.228.50) │
│  Raw alert creation  │  │  SOAR pipeline triggered      │
└──────────────────────┘  └──────────┬───────────────────┘
                                     │
                    ┌────────────────┼───────────────────┐
                    ▼                ▼                    ▼
             Slack notify     Risk Score +         TheHive enriched
                              MITRE mapping        alert + Gmail
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────┐
│              CASE MANAGEMENT + IOC ENRICHMENT           │
│  TheHive + Cortex (192.168.228.40)                      │
│  ├─ TheHive 5.6.1  → alert → observable → case         │
│  └─ Cortex 3.2.1   → AbuseIPDB + VirusTotal analyzers  │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                  MONITORING                             │
│  Grafana (192.168.228.10:3000)                          │
│  └─ Live dashboard on wazuh-alerts-4.x-* index          │
└─────────────────────────────────────────────────────────┘
```
<img width="1800" height="2200" alt="Untitled design" src="https://github.com/user-attachments/assets/e6fc9984-7194-458e-a891-1a385a1eb301" />

---

## 🖥️ Virtual Machines

| VM | IP | OS | RAM | Role |
|---|---|---|---|---|
| Wazuh Server | 192.168.228.10 | Ubuntu 24.04 | 4 GB | SIEM · Active Response · Grafana |
| Windows 10 | 192.168.228.20 | Windows 10 | 4 GB | Victim endpoint |
| Kali Linux | 192.168.228.30 | Kali | 4 GB | Attacker |
| TheHive + Cortex | 192.168.228.40 | Ubuntu 24.04 | 8 GB | Case management · IOC enrichment |
| n8n | 192.168.228.50 | Ubuntu 24.04 | 2 GB | SOAR orchestration |

All VMs run on **VMware Workstation** — Host-only network (VMnet1) + NAT for external API access.

---

## 🔧 Tools & Versions

| Tool | Version | Role |
|---|---|---|
| Wazuh | 4.x | SIEM / EDR — detection, alerting, active response |
| Sysmon | SwiftOnSecurity config | Enhanced Windows event telemetry |
| TheHive | 5.6.1 | Security incident case management |
| Cortex | 3.2.1 | IOC enrichment engine |
| n8n | 2.11.4 | SOAR workflow automation |
| Grafana | Latest | Live security metrics dashboard |
| AbuseIPDB | API v2 | IP abuse reputation scoring |
| VirusTotal | API v3 | IP / hash / domain analysis |
| Slack | Incoming Webhook | Real-time SOC notifications |
| Gmail | SMTP + App Password | Email alert delivery |

---

## ✅ Features

| Capability | Status |
|---|---|
| Brute force detection — SSH, SMB, FTP, RDP | ✅ Automated |
| SAM database dump detection | ✅ Automated |
| Active response — auto IP block via netsh | ✅ Automated |
| Slack real-time SOC notification | ✅ Automated |
| Dynamic risk scoring (0–100) | ✅ Automated |
| MITRE ATT&CK tactic & technique tagging | ✅ Automated |
| TheHive alert creation | ✅ Automated |
| Gmail alert with risk label + MITRE context | ✅ Automated |
| IOC enrichment — AbuseIPDB + VirusTotal | 🔵 Manual trigger in TheHive |
| Grafana live security dashboard | 🟢 Live |

---

## 🎯 Attack Scenarios Tested

| Attack | Tool | Wazuh Rule | Level | MITRE |
|---|---|---|---|---|
| SMB Brute Force | smbclient | 60122, 60204 | 10 | T1110 |
| SSH Brute Force | Hydra | 60122, 60106 | 10 | T1110 |
| FTP Brute Force | Hydra | 60104 | 5 | T1110 |
| RDP Brute Force | Hydra | 60104 | 5 | T1110 |
| SAM Hive Dump | reg.exe | 92026 | 14 | T1003.002 |
| Account Discovery | net.exe | 92039 | 3 | T1087 |
| PowerShell Execution | PowerShell | 91816 | 4 | T1082 |

---

## 📊 Risk Scoring System

Risk score is calculated dynamically in the n8n Code node on every alert:

```
Base score = Wazuh rule level (1–15)

MITRE tactic bonuses:
  Exfiltration          → +35
  Lateral Movement      → +30
  Impact                → +30
  Privilege Escalation  → +25
  Credential Access     → +20
  Defense Evasion       → +20

Score capped at 100.

Labels:
  0–24   → LOW
  25–49  → MEDIUM
  50–74  → HIGH
  75–100 → CRITICAL
```

---

## ⚙️ n8n SOAR Workflow

```
Webhook (receives raw Wazuh alert JSON)
        │
        ▼
HTTP Request → Slack notification (SOC channel)
        │
        ▼
Code Node (JavaScript)
  ├─ Filter: level < 10 → skip
  ├─ Calculate risk score
  ├─ Map MITRE ATT&CK tactics & techniques
  └─ Build enriched payload
        │
        ▼
HTTP Request → TheHive enriched alert
        │
        ▼
Send Email → Gmail alert (risk label + MITRE + agent info)
```

---

## 🔒 Active Response — Auto IP Block

When a brute force alert fires (rules 60122, 60204, 60115), Wazuh tells the Windows agent to execute `netsh.exe` — blocking the attacker's IP in Windows Firewall for **300 seconds automatically**. No analyst action required.

Relevant `ossec.conf` block:

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
```

---

## 📁 Repository Structure

```
SOC-Automation-Lab/
├── README.md               ← You are here
├── ARCHITECTURE.md         ← Full technical breakdown: ports, flow, node descriptions
├── TROUBLESHOOTING.md      ← Real errors hit during the build + exact fixes
├── src/
│   ├── custom-thehive.py   ← Wazuh integration script (TheHive + n8n)
│   └── ossec-active-response.xml  ← Active response config snippet
└── screenshots/            ← Proof screenshots (flat structure)
```

---

## 📸 Screenshots

| Architecture overview | n8n Workflow |
|---|---|
| ![Wazuh Alerts](screenshots/wazuh-alerts.png) | ![n8n Workflow]<img width="1509" height="284" alt="upgraded n8n workflow to send custom message to my gmail account 20" src="https://github.com/user-attachments/assets/79f86bbf-81a7-4767-aef7-9bfb0bef2b04" />
 |

| TheHive Alert | Cortex IOC Enrichment | Slack Notification |
|---|---|---|
| <img width="1918" height="893" alt="Test alert for The hive integration 6" src="https://github.com/user-attachments/assets/b215bc3d-3e15-4907-b058-730dfc1259f6" />
 | ![Cortex](screenshots/cortex-abuseipdb.png) | <img width="1850" height="694" alt="n8n alerts on slack #new-channel 11" src="https://github.com/user-attachments/assets/03c89082-a35f-4a32-a045-2db1f81e4c12" />
 |

---

## 👤 Author

**Aymen Idrissi**
*Cybersecurity Intern @ Portnet S.A., Morocco*
*Cybersecurity Engineering Student — Mundiapolis University*

This project was developed as a **Final Year Project (PFA)** in a professional internship setting.

[![GitHub](https://img.shields.io/badge/GitHub-IdrissiAymen-181717?logo=github)](https://github.com/IdrissiAymen)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aymen_Idrissi-0077B5?logo=linkedin)](https://www.linkedin.com/in/aymen-karkouri-idrissi-653259334/)

---

## ⚠️ Disclaimer

Educational purposes only. All attacks were performed inside a fully isolated virtual network with no external exposure. No real systems were targeted.
