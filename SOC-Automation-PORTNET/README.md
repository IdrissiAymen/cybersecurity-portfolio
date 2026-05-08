# 🛡️ SOC Automation Lab — End-to-End Detection & Response Pipeline

### 🎯 Project Description
Developed as a Final Year Project (PFA) during a Cybersecurity internship at Portnet S.A., Morocco — a fully operational SOC pipeline built from the ground up across 5 VMware virtual machines. This project replicates real-world SOC operations: threat detection, automated containment, SOAR-driven alert enrichment, dynamic risk scoring, MITRE ATT&CK mapping, and live security monitoring — built entirely on enterprise-grade open-source tools with no managed services or cloud shortcuts.


### ⚡ What Happens When Kali Attacks

When Kali Linux launches a brute force attack against the Windows 10 victim, the following happens automatically — zero human intervention:
1. Wazuh         →  Detects the attack within seconds (rule 60204, level 10)
2. Windows FW    →  Auto-blocks attacker IP via netsh (active response, 300s)
3. Slack         →  Instant SOC channel notification
4. n8n           →  Calculates dynamic risk score (0–100) + maps MITRE ATT&CK tactics
5. TheHive       →  Receives a fully enriched, structured alert
6. Gmail         →  Formatted email with risk label, MITRE details, agent info
7. Grafana       →  Live security dashboard updates in real time
The analyst then opens the TheHive alert, adds the attacker IP as an observable, and triggers Cortex (AbuseIPDB + VirusTotal) for deep IOC enrichment — all from the same interface.

### 🏗️ Architecture
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

🖥️ Virtual Machines
VMIPOSRAMRoleWazuh Server192.168.228.10Ubuntu 24.044 GBSIEM · Active Response · GrafanaWindows 10192.168.228.20Windows 104 GBVictim endpointKali Linux192.168.228.30Kali4 GBAttackerTheHive + Cortex192.168.228.40Ubuntu 24.048 GBCase management · IOC enrichmentn8n192.168.228.50Ubuntu 24.042 GBSOAR orchestration
All VMs run on VMware Workstation — Host-only network (VMnet1) + NAT for external API access.

🔧 Tools & Versions
ToolVersionRoleWazuh4.xSIEM / EDR — detection, alerting, active responseSysmonSwiftOnSecurity configEnhanced Windows event telemetryTheHive5.6.1Security incident case managementCortex3.2.1IOC enrichment enginen8n2.11.4SOAR workflow automationGrafanaLatestLive security metrics dashboardAbuseIPDBAPI v2IP abuse reputation scoringVirusTotalAPI v3IP / hash / domain analysisSlackIncoming WebhookReal-time SOC notificationsGmailSMTP + App PasswordEmail alert delivery

✅ Features
CapabilityStatusBrute force detection — SSH, SMB, FTP, RDP✅ AutomatedSAM database dump detection✅ AutomatedActive response — auto IP block via netsh✅ AutomatedSlack real-time SOC notification✅ AutomatedDynamic risk scoring (0–100)✅ AutomatedMITRE ATT&CK tactic & technique tagging✅ AutomatedTheHive alert creation✅ AutomatedGmail alert with risk label + MITRE context✅ AutomatedIOC enrichment — AbuseIPDB + VirusTotal🔵 Manual trigger in TheHiveGrafana live security dashboard🟢 Live

🎯 Attack Scenarios Tested
AttackToolWazuh RuleLevelMITRESMB Brute Forcesmbclient60122, 6020410T1110SSH Brute ForceHydra60122, 6010610T1110FTP Brute ForceHydra601045T1110RDP Brute ForceHydra601045T1110SAM Hive Dumpreg.exe9202614T1003.002Account Discoverynet.exe920393T1087PowerShell ExecutionPowerShell918164T1082

📊 Risk Scoring System
Risk score is calculated dynamically in the n8n Code node on every alert:
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

⚙️ n8n SOAR Workflow
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

🔒 Active Response — Auto IP Block
When a brute force alert fires (rules 60122, 60204, 60115), Wazuh tells the Windows agent to execute netsh.exe — blocking the attacker's IP in Windows Firewall for 300 seconds automatically. No analyst action required.
Relevant ossec.conf block:
xml<command>
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

📁 Repository Structure
SOC-Automation-Lab/
├── README.md               ← You are here
├── ARCHITECTURE.md         ← Full technical breakdown: ports, flow, node descriptions
├── TROUBLESHOOTING.md      ← Real errors hit during the build + exact fixes
├── src/
│   ├── custom-thehive.py   ← Wazuh integration script (TheHive + n8n)
│   └── ossec-active-response.xml  ← Active response config snippet
└── screenshots/            ← Proof screenshots (flat structure)

📸 Screenshots
Architecture overviewn8n WorkflowShow ImageShow Image
TheHive AlertCortex IOC EnrichmentSlack NotificationShow ImageShow ImageShow Image

👤 Author
KARKOURI IDRISSI Aymen
Cybersecurity Intern @ Portnet S.A., Morocco
Cybersecurity Engineering Student — Mundiapolis University
This project was developed as a Penultimate Year Project (PFA) in a professional internship setting.
https://www.linkedin.com/in/aymen-karkouri-idrissi-653259334/

⚠️ Disclaimer
Educational purposes only. All attacks were performed inside a fully isolated virtual network with no external exposure. No real systems were targeted.
