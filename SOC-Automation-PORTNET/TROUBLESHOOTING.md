# 🛠️ Troubleshooting — SOC Automation Lab

Real errors hit during the 15-day build, with exact fixes. No fluff.

---

## Wazuh

### ❌ Active response invalid location error

**Error:**
```
wazuh-analysisd: ERROR (1302): Invalid active response location: 'agent'
```

**Root cause:** The `<active-response>` block was using `location=agent` instead of `local`.

**Fix:**
```xml
<active-response>
  <command>netsh</command>
  <location>local</location>
  <rules_id>60122,60204,60115</rules_id>
  <timeout>300</timeout>
</active-response>
```

---

### ❌ Active response fires but IP not blocked

**Error:** netsh runs but Windows Firewall shows no block rule for Kali's IP.

**Root cause:** Windows Firewall was disabled on the Windows VM — turned off earlier to allow attack traffic during initial setup.

**Fix:**
```cmd
netsh advfirewall set allprofiles state on
netsh advfirewall firewall add rule name="Allow SMB" protocol=TCP dir=in localport=445 action=allow
netsh advfirewall firewall add rule name="Allow SSH" protocol=TCP dir=in localport=22 action=allow
netsh advfirewall firewall add rule name="Allow FTP" protocol=TCP dir=in localport=21 action=allow
```

---

## n8n

### ❌ TheHive fields show [undefined]

**Error:** n8n HTTP node creates TheHive alert but title, agent, and description all show `[undefined]`.

**Root cause:** The Slack HTTP node only passed `{data: 'ok'}` forward, losing all original Wazuh alert data.

**Fix:** Add a Code node after Slack, before TheHive, to re-extract from the Webhook node:
```javascript
const webhookData = $('Webhook').item.json;
return {
  rule: webhookData.body.rule,
  agent: webhookData.body.agent,
  timestamp: webhookData.body.timestamp,
  sourceRef: 'n8n-' + webhookData.body.rule.id + '-' + Date.now()
};
```

---

### ❌ Duplicate alert error from TheHive

**Error:**
```
400 — Alert already exists in organisation socaymen
```

**Root cause:** TheHive rejects alerts with a duplicate `sourceRef`. Happens when testing with the same rule ID twice.

**Fix:** Always generate a unique `sourceRef` using `Date.now()`:
```javascript
sourceRef: 'n8n-' + rule.id + '-' + Date.now()
```

---

### ❌ TheHive case creation 403 Forbidden

**Error:**
```
You don't have the permission manageCase/create
```

**Root cause:** TheHive 5 community (free) license restricts case creation via API. This is a licensing limitation, not a config error.

**Fix:** Create cases manually by promoting alerts in the TheHive UI. Alerts are still created automatically — only case promotion is restricted.

---

### ❌ Getting spam emails for every alert

**Error:** Gmail receiving emails for package installs, system noise, and low-severity events.

**Root cause:** n8n was processing all alerts level 7+, including irrelevant system events.

**Fix:** Add this filter at the top of the Code node:
```javascript
const level = $('Webhook').item.json.body.rule.level || 0;
if (level < 10) return [];
```

---

## Cortex

### ❌ 0 analyzers showing after install

**Error:** Cortex UI shows "No analyzers found" after cloning Cortex-Analyzers.

**Root cause:** `application.conf` was still pointing to the StrangeBee online URL instead of the local path.

**Fix:**
```hocon
# In /etc/cortex/application.conf:
analyzer {
  urls = [
    "/opt/cortex/analyzers/analyzers"
  ]
}
```
Then restart:
```bash
sudo systemctl restart cortex
```

---

### ❌ AbuseIPDB fails — No module named cortexutils

**Error:**
```
ModuleNotFoundError: No module named 'cortexutils'
```

**Root cause:** `cortexutils` was installed for the local user only. Cortex runs as the `cortex` system user who can't access it.

**Fix:**
```bash
sudo pip3 install cortexutils --break-system-packages
sudo systemctl restart cortex
```

---

### ❌ VirusTotal fails — missing modules

**Error:** VirusTotal analyzer job fails with multiple `ModuleNotFoundError`.

**Root cause:** Several Python dependencies missing for the VirusTotal analyzer.

**Fix:**
```bash
sudo pip3 install filetype --break-system-packages
sudo pip3 install vt-py --break-system-packages
sudo pip3 install python-magic --break-system-packages
sudo apt install -y libmagic1
sudo systemctl restart cortex
```

---

## TheHive

### ❌ Config error on restart

**Error:**
```
Configuration error at 'etc/thehive/application.conf'
```

**Root cause:** The `play.modules.enabled` and `cortex {}` blocks were accidentally placed inside the `storage {}` block due to a missing closing brace.

**Fix — correct structure:**
```hocon
storage {
  provider = localfs
  localfs.location = /opt/thp/thehive/files
}   # <-- this closing brace must be here before the next block

play.modules.enabled += connectors.cortex.CortexConnector

cortex {
  servers = [{
    name = "Cortex"
    url = "http://127.0.0.1:9001"
    auth {
      type = "bearer"
      key = "YOUR_CORTEX_API_KEY"
    }
  }]
}
```

---

## Grafana

### ❌ Can't connect to OpenSearch

**Error:**
```
Health check failed: Failed to connect to Elasticsearch
```

**Root cause:** OpenSearch uses HTTPS not HTTP, and only listens on `localhost` not the network IP.

**Fix — use these exact settings in the Grafana data source config:**

| Setting | Value |
|---|---|
| URL | `https://localhost:9200` |
| Authentication | Basic auth |
| User | `admin` |
| Skip TLS cert validation | ON |
| Index name | `wazuh-alerts-4.x-*` |
| Time field | `@timestamp` |
