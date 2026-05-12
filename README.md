# 👾 Aymen Karkouri Idrissi — Cybersecurity Portfolio

**Cybersecurity Engineering Student | 4th Year @ Mundiapolis University**
📍 Mohammedia, Morocco &nbsp;|&nbsp; 📧 gilnashidrissi@gmail.com &nbsp;|&nbsp; 🔗 [LinkedIn](https://www.linkedin.com/in/aymen-karkouri-idrissi-653259334/) &nbsp;|&nbsp; 📸 [Instagram](https://instagram.com/the.gaffer_)

---

## 🧭 About Me

I'm a 4th-year cybersecurity engineering student driven by a genuine passion for how security works at every layer — from network packets to incident response. I build hands-on labs, compete in CTFs, and document everything I learn.

My journey into cybersecurity was heavily inspired by **[UNIXGUY](https://www.youtube.com/@UnixGuy)** on YouTube — his content on SOC operations and blue team fundamentals shaped a lot of how I think about security.

- 🎓 Mundiapolis University — Cloud Computing & Security
- 🔭 Current focus: Blue Team, Network Security, Threat Detection
- 🛠️ Building: SOC infrastructure, enterprise network security labs
- 🌍 Based in Mohammedia, Morocco

---

## 🏆 CTF Achievements

| Competition | Team | Result |
|-------------|------|--------|
| MACC 2026 | Mundi[0x41]PWN | 🥈 **54th / 1,071 teams** |
| CTF Mundiapolis | Skarawalflag | 🥇 **2nd Place** |
| ENSET Challenge CTF 2026 | — | Participated |
| N7SEC CTF | — | Participated |

> Challenges solved across: Cryptography · Reverse Engineering · Pwn · Web · Misc

---

## 🚀 Projects & Internships

---

### 🔵 [SOC Home Lab — Final Year Project](./Projects/SOC-HomeLab/)
> Personal Lab | VMware Workstation | 5 VMs

Full Security Operations Center built from scratch as my personal final year project.

**Stack:** Wazuh · TheHive · Cortex · n8n · Grafana · Slack · Gmail

- Deployed 5 interconnected VMs (Ubuntu/Windows) on VMware Workstation
- Wazuh as SIEM: log ingestion, rule tuning, agent deployment across endpoints
- TheHive + Cortex for case management and automated response workflows
- n8n as SOAR engine: alert → ticket → Slack/Gmail notification pipeline
- Grafana dashboards for real-time threat visibility

---

### 🟠 [Enterprise Network Security @ PORTNET — Internship (2024–2025)](./Projects/PORTNET-Internship-2025/)
> Internship | PORTNET S.A. — Morocco's National Single Window for Foreign Trade | VMware Workstation

Designed and deployed a **secure, segmented enterprise network** simulating real-world infrastructure with layered firewalls, DMZ isolation, centralized monitoring, and identity management — aligned with PortNet's Zero Trust architecture goals.

**Stack:** OPNsense · Wazuh · Keycloak · PostgreSQL · Squid Proxy · Postfix · WireGuard · Apache2

**Architecture — 6 isolated zones:**

```
Internet
    │
[FIREWALL1 - OPNsense] (192.168.80.1)
    ├── Public DMZ      → Apache Web Server
    │
[FIREWALL2 - OPNsense] (192.168.80.2)
    ├── DMZ-Production  → Keycloak (IAM) + PostgreSQL  [192.168.30.0/24]
    ├── DMZ-Proxy/Mail  → Squid Proxy + Postfix        [192.168.40.0/24]
    ├── DMZ-Security    → Wazuh SIEM + Syslog          [192.168.50.0/24]
    ├── Internal LAN    → Ubuntu/Windows Clients       [192.168.60.0/24]
    └── Management DMZ  → Jump Host + WireGuard VPN
```

**Key implementations:**
- Dual OPNsense firewall setup (FW1 ↔ FW2 link: `192.168.80.0/24`) with deny-all default policy
- OPNsense IDS/IPS with Emerging Threats ruleset for real-time traffic inspection
- Wazuh agents deployed across all VMs including directly on FIREWALL1 via OPNsense plugin
- Keycloak SSO + LDAP federation + RBAC, hardened with UFW (ports 443 and 389 only)
- PostgreSQL backend for Keycloak (port 5432, internal traffic only)
- Squid Proxy on port 3128 for filtered and logged outbound web access
- Postfix mail relay (ports 25/80/443) for controlled outbound mail
- WireGuard VPN on Management DMZ with IP forwarding for encrypted remote admin access
- Simulated attack: Kali Linux netcat probe on port 12174 → confirmed detection in both Wazuh and OPNsense IDS logs

---

### 🟡 [NAC with PacketFence, 802.1X & Active Directory](./Projects/PacketFence(NAC+802.1X+ADPART00)/)
> Group Project | VMware Workstation | Domain: nac.local

Implemented a full Network Access Control solution with port-based authentication.

**Stack:** PacketFence ZEN v15 · Windows Server 2022 · NPS · FreeRADIUS · LDAP

- Configured 802.1X PEAP authentication on a Windows client
- Integrated PacketFence with Active Directory over LDAP (port 389)
- Registered NPS as RADIUS client with network policies for allow/deny
- Tested valid (`user1`) and invalid (`user2`) scenarios with full RADIUS audit logs

---

### 🐍 [Ransomware Simulation — Educational Project](./Ransomware/)
> Python | cryptography.Fernet | Lab Environment Only

Built a Python-based ransomware simulator to understand encryption mechanics and how ransomware operates internally — no real targets, fully isolated lab.

- Scans a target folder, skips system/key files, encrypts all others using `cryptography.Fernet`
- Generates and saves a symmetric key (`thekey.key`) for later decryption
- Separate decryption script restores files when the correct passphrase is entered
- Simulates the full ransom flow: encrypt → ransom message → passphrase check → decrypt

**What it taught me:** why file integrity monitoring and endpoint detection matter, and how ransomware authors think about key storage and delivery.

---

## 🧪 Labs & Platforms

### CyberDefenders

Hands-on blue team investigations using real malware traffic, memory dumps, and logs.

| Lab | Category | Skills Practiced |
|-----|----------|-----------------|
| WebStrike | Network Forensics | HTTP log analysis, attacker TTPs |
| Hammered | Log Analysis | SSH brute-force investigation |
| PsExec Hunt | Threat Hunting | Lateral movement detection |
| IcedID | Malware Analysis | Banking trojan traffic analysis |
| GrabThePhisher | Phishing Analysis | Phishing kit reverse engineering |
| RedLine | Malware Analysis | Stealer artifact analysis |
| Ransomware Lab | Malware Analysis | Ransomware behavior & IOC extraction |

---

### OverTheWire — Bandit
> ✅ All levels completed

Completed all **Bandit** levels on OverTheWire — a wargame focused on Linux fundamentals, file system navigation, SSH, permissions, environment variables, scripting, and basic cryptography. Solid foundation for everything that came after.

---

### PortSwigger Web Security Academy
> SQL Injection — Apprentice & Practitioner levels

Completed ~10 SQL injection labs using **Burp Suite**, covering both Apprentice and Practitioner difficulty:
- In-band SQLi (UNION-based, error-based)
- Blind SQLi (boolean-based, time-based)
- Database enumeration and data extraction techniques

---

## 🌐 Events & Networking

- **GITEX Africa** — Networked with representatives from Fortinet, DataProtect, CyberSOC, and Nucleon

---

## 📜 Certifications

| Certification | Issuer | Status |
|---------------|--------|--------|
| CC — Certified in Cybersecurity | ISC² | ✅ |
| CC Domain 1: Security Principles | ISC² | ✅ |
| CC Domain 2: Incident Response & Business Continuity | ISC² | ✅ |
| CC Domain 4: Network Security | ISC² | ✅ |
| Security Operations | ISC² | ✅ |
| Access Control Concepts | ISC² | ✅ |
| Cisco Certified | Cisco | ✅ |
| Certification TATA (IAM) | TATA | ✅ |
| Intro to Splunk (eLearning) | Splunk | ✅ |
| Design a Phishing Email Simulation | Mastercard Forage | ✅ |
| Google Cybersecurity Certificate | Google | 🔄 In Progress |

---

## 🛠️ Skills & Tools

**Defensive / Blue Team**
`Wazuh` `TheHive` `Cortex` `Grafana` `n8n` `Splunk` `Wireshark` `Syslog` `Suricata`

**Networking & Infrastructure**
`OPNsense` `Active Directory` `DNS` `RADIUS` `802.1X` `LDAP` `PacketFence` `NPS` `WireGuard`

**Identity & Access**
`Keycloak` `PostgreSQL` `UFW` `SSO` `RBAC`

**Offensive / Web / CTF**
`Nmap` `Metasploit` `Netcat` `Burp Suite` `SQLi` `BloodHound` `Impacket`

**Dev & Automation**
`Python` `Bash` `Git` `n8n`

**Platforms & OS**
`Linux (Ubuntu/Kali)` `Windows Server 2022` `VMware Workstation` `WSL`

---

## 💡 Inspiration

A big part of what pushed me toward blue team and SOC work was **[UNIXGUY](https://www.youtube.com/@UnixGuy)** on YouTube. His no-fluff breakdowns of what it actually means to work in a SOC, what skills matter, and how to build a real career in cybersecurity hit different when you're starting out. Highly recommend his channel if you're on the same path.

---

*Always learning. Always building.*
