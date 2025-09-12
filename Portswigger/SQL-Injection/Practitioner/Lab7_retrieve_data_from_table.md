<img width="700" height="350" alt="Screenshot_18" src="https://github.com/user-attachments/assets/b7b55c6c-268b-4561-8cd6-a787cd83ff41" />

# Lab: SQL injection UNION attack — Retrieving data from other tables

🔗 **Lab link**: [PortSwigger — Lab: SQL injection UNION attack, retrieving data from other tables](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables). :contentReference[oaicite:0]{index=0}

---

## 📝 Lab goal
Exploit a **UNION-based SQL injection** in the product category filter to retrieve rows from another table (`users`) and use the recovered credentials to log in as the `administrator`. :contentReference[oaicite:1]{index=1}

---

## ✅ solution — concise
1. Intercept the request that sets the product category (e.g., using Burp Suite).  
2. Confirm the number of columns and which columns can hold text (you already did this in previous labs).  
3. Inject the payload to retrieve the `users` table contents:
   ```sql
   ' UNION SELECT username, password FROM users--
'''markdown
(URL-encoded form commonly used in labs: '+UNION+SELECT+username,+password+FROM+users--)
4. The application response contained usernames and passwords — copy the administrator credentials.
5. Log in to the application using the retrieved administrator username and password → Lab solved.
