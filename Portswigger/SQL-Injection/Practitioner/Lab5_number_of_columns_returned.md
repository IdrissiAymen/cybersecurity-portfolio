<img width="600" height="300" alt="Screenshot_16" src="https://github.com/user-attachments/assets/aa2a6f16-c76e-459b-b88a-425198e2b84b" />

# Lab: SQL Injection UNION Attack – Determining the Number of Columns

🔗 **Lab Link**: [PortSwigger – Lab: SQL injection UNION attack, determining the number of columns returned by the query](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns)  

---

##  Lab Summary
In this lab, you must exploit a **SQL injection vulnerability** using a **UNION-based attack** to discover how many columns the original query returns. This is a foundational step before you can extract any real data using UNION injections. :contentReference[oaicite:0]{index=0}

---

##  Step-by-Step Exploitation

### 1. Identify injection point
Intercept the request (e.g., via Burp Suite) and locate the `category` parameter—or equivalent—that appears vulnerable.

### 2. Use `UNION SELECT null, null, null--`
Inject the following payload:

' UNION SELECT null, null, null--

### 3. Observe response
If the page returns normally (without error), the payload has successfully executed, confirming the original query returns 3 columns.

