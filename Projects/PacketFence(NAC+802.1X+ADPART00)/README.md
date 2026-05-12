# 🔐 NAC with PacketFence, 802.1X & Active Directory

**Category:** Network Access Control
**Environment:** VMware Workstation
**PacketFence Version:** ZEN v15.0.0
**Domain:** `nac.local`
**Status:** In Progress

---

## 📌 Overview

This project implements a **Network Access Control (NAC)** solution using **PacketFence ZEN** with **IEEE 802.1X port-based authentication**, backed by a **Windows Server Active Directory** domain.

Only users authenticated against AD via RADIUS are granted network access. Unauthorized devices are blocked at the port level before they can reach any network resource.

---

## 🧱 Lab Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   VMware Workstation                     │
│                                                         │
│  ┌──────────────────┐     ┌──────────────────────────┐  │
│  │  VM1: PacketFence│     │   VM2: Windows Server    │  │
│  │  ZEN v15.0.0     │◄───►│   Active Directory       │  │
│  │  192.168.x.10    │     │   192.168.x.20           │  │
│  │  NAC + RADIUS    │     │   AD DS + DNS + NPS      │  │
│  └────────┬─────────┘     └──────────────────────────┘  │
│           │                          ▲                   │
│           │                          │                   │
│           ▼                          │                   │
│  ┌──────────────────┐                │                   │
│  │  VM3: Windows 10 │────────────────┘                   │
│  │  192.168.x.30    │                                    │
│  │  802.1X Client   │                                    │
│  └──────────────────┘                                    │
└─────────────────────────────────────────────────────────┘
```

> ⚠️ **Note:** IPs above are placeholders 

| VM | OS | Role | IP | Network Adapter |
|----|----|------|----|-----------------|
| VM1 | PacketFence ZEN v15 | NAC Server + RADIUS | `192.168.x.10` | Bridged (eth0) + LAN (eth1) |
| VM2 | Windows Server 2022 | AD DS + DNS + NPS | `192.168.x.20` | LAN Internal |
| VM3 | Windows 10/11 | 802.1X Client | `192.168.x.30` | LAN Internal |

---

## 🗂️ Step-by-Step Implementation

---

### PART 0 – Preparation

#### 0.1 Downloads

| Item | Source |
|------|--------|
| PacketFence ZEN v15.0.0 | [packetfence.org/download.html](https://packetfence.org/download.html) |
| WinSCP (file transfer) | [winscp.net](https://winscp.net) |
| `pf15-zen-trim.sh` | Provided by teacher |

#### 0.2 VM Optimization (Before First Boot)

Transferred `pf15-zen-trim.sh` to the PacketFence VM using **WinSCP**, then ran it to reduce disk/memory overhead:

```bash
chmod +x pf15-zen-trim.sh
sudo ./pf15-zen-trim.sh
```

#### 0.3 VMware Network Setup

- **VM1 (PacketFence):** Two adapters — one Bridged (internet access), one on the Internal LAN
- **VM2 (AD):** One adapter on the Internal LAN
- **VM3 (Client):** One adapter on the Internal LAN

All three VMs share the same **Internal Network** so they can communicate.

---

### PART 1 – PacketFence Installation

#### 1.1 Import the ZEN VM

1. Open VMware Workstation → `File > Open` → select the `.vmx` from the extracted ZEN archive
2. Set RAM to **4–6 GB**, disk **40 GB**, **2 network interfaces**

#### 1.2 First Boot & Static IP

On first boot, PacketFence will prompt for network configuration via console:

```
Interface eth1 (LAN) → 192.168.x.10 / 255.255.255.0
Gateway → 192.168.x.1
DNS → 192.168.x.20  (points to the AD server)
```

#### 1.3 Access the Admin Web UI

Open a browser from your host machine:

```
https://192.168.x.10:1443
Login: admin / admin
```

#### 1.4 Setup Wizard

Follow the wizard:
- **Hostname:** `packetfence.nac.local`
- **Domain:** `nac.local`
- **Managed Interface:** eth1 (LAN)
- **RADIUS secret:** (set a shared secret — same one used in NPS later)
- **Admin password:** change from default

---

### PART 2 – Active Directory Setup

#### 2.1 Windows Server VM

- OS: Windows Server 2022
- Static IP: `192.168.x.20`
- Subnet: `255.255.255.0`
- DNS: `127.0.0.1` (points to itself after AD install)

#### 2.2 Install AD DS, DNS, NPS

In **Server Manager → Add Roles and Features**, install:
- ✅ Active Directory Domain Services
- ✅ DNS Server
- ✅ Network Policy and Access Services (NPS)

#### 2.3 Promote to Domain Controller

After installing AD DS, click the flag notification → **Promote this server to a domain controller**:

```
Operation: Add a new forest
Root domain name: nac.local
Forest/Domain functional level: Windows Server 2016
DSRM password: (set a recovery password)
```

Reboot after promotion.

#### 2.4 Create Users

Open **Active Directory Users and Computers** → `nac.local` → `Users`:

| User | Password | Purpose |
|------|----------|---------|
| `user1` | `Password1!` | Valid — should authenticate successfully |
| `user2` | `Password2!` | Invalid — should be denied access |

> For `user2`, you can disable the account or use it with a wrong password during testing.

#### 2.5 Register PacketFence as RADIUS Client in NPS

Open **NPS Console** → `RADIUS Clients and Servers` → `RADIUS Clients` → New:

```
Friendly name: PacketFence
Address: 192.168.x.10
Shared secret: (same secret set in PacketFence wizard)
```

#### 2.6 Create Network Policy (PEAP)

In NPS → `Policies` → `Network Policies` → New:

```
Policy name: 802.1X-PEAP
Conditions: NAS Port Type = Ethernet
Authentication method: Protected EAP (PEAP)
Permission: Access Granted
```

---

### PART 3 – PacketFence ↔ Active Directory Integration

#### 3.1 Add AD as Authentication Source

In PacketFence web UI:
```
Configuration → Authentication Sources → Add Source → AD/LDAP
```

Fill in:

```
Name:        ActiveDirectory
Host:        192.168.x.20
Port:        389 (LDAP) or 636 (LDAPS)
Base DN:     DC=nac,DC=local
Bind DN:     CN=Administrator,CN=Users,DC=nac,DC=local
Password:    <admin password>
```

#### 3.2 Test the LDAP Connection

Click **Test** in the Authentication Source config — you should get a green success message confirming PacketFence can reach and query the AD.

---

### PART 4 – Windows 10 Client (802.1X)

#### 4.1 VM Network

- Connect VM3 to the same Internal LAN as VM1 and VM2
- Static IP: `192.168.x.30` / DNS: `192.168.x.20`

#### 4.2 Enable 802.1X Authentication

1. Open `Services.msc` → enable and start **Wired AutoConfig** service
2. Go to `Network Connections` → right-click the LAN adapter → Properties
3. **Authentication** tab:
   - ✅ Enable IEEE 802.1X authentication
   - Method: **Protected EAP (PEAP)**
   - Click Settings → uncheck "Validate server certificate" (lab environment)
   - Inner method: **Secured Password (EAP-MSCHAP v2)**

#### 4.3 Configure Credentials

In the Authentication tab → **Additional Settings**:
- Select: **User or computer authentication**
- Or manually specify credentials when prompted

---

### PART 5 – Testing & Validation

| Test | User | Credentials | Expected | Result |
|------|------|-------------|----------|--------|
| Valid authentication | user1 | Correct password | ✅ Access granted | — |
| Invalid authentication | user2 | Wrong/disabled | ❌ Access denied | — |
| RADIUS logs | — | PacketFence UI | Logs visible | — |
| NPS logs | — | Event Viewer | Events logged | — |

#### Where to check logs

**PacketFence:**
```
Status → RADIUS Audit Log
```

**Windows Server (NPS):**
```
Event Viewer → Custom Views → Server Roles → Network Policy and Access Services
```

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| PacketFence ZEN v15 | NAC server + integrated RADIUS |
| Windows Server 2022 | AD DS, DNS, NPS |
| VMware Workstation | Lab virtualization |
| WinSCP | File transfer to Linux VM |
| IEEE 802.1X / PEAP | Port-based auth protocol |
| LDAP (port 389) | AD directory queries from PacketFence |
| FreeRADIUS (built-in) | RADIUS backend inside PacketFence |

---

## 📚 Key Concepts

**802.1X** — IEEE standard for port-based Network Access Control. A device must authenticate before the switch port is opened.

**RADIUS** — Remote Authentication Dial-In User Service. The protocol PacketFence and NPS use to exchange authentication decisions.

**NAC** — Network Access Control. Enforces security policy (who/what can connect) before granting network access.

**PEAP** — Protected EAP. Wraps the EAP exchange in a TLS tunnel so credentials aren't sent in cleartext.

**LDAP** — Lightweight Directory Access Protocol. Used by PacketFence to query Active Directory and validate user identities.

---

## 👥 Authors

- **Aymen Karkouri Idrissi** — [@IdrissiAymen](https://github.com/IdrissiAymen)

*Part of the [cybersecurity-portfolio](https://github.com/IdrissiAymen/cybersecurity-portfolio) — documenting hands-on labs and real projects.*
