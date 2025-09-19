<img width="500" height="306" alt="Screenshot_17" src="https://github.com/user-attachments/assets/7ee36a9b-15ab-4ac9-8a90-c7289c2f8172" />

# Lab: SQL injection UNION attack — Finding a column containing text

🔗 **Lab link**: [PortSwigger — Lab: SQL injection UNION attack, finding a column containing text](https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text). :contentReference[oaicite:0]{index=0}

---

## 📝 Lab goal
Make the database return a specific random string (provided by the lab) in the application response by using a `UNION SELECT` injection. To do that you must:
1. Determine how many columns the original query returns.  
2. Find which column(s) can hold string/text data.  
3. Return a row containing the lab-provided string so it appears in the page. :contentReference[oaicite:1]{index=1}

---

## ✅ Your solution (concise)
1. Determine column count using:  
   ```sql
   ' UNION SELECT NULL,NULL,NULL--
   ```markdown
this confirmed the original query returns 3 columns. 

- Find which column accepts text by replacing NULL values one at a time with the lab-provided string (2MFhch) until it shows up in the app:
The payload that worked for you was:
- ' UNION SELECT NULL,'2MFhch',NULL--
— meaning the second returned column accepts string data and the lab string is visible there.
- With the text column identified, you can craft further UNION SELECT payloads to retrieve usernames/passwords or other text data from database tables. 
