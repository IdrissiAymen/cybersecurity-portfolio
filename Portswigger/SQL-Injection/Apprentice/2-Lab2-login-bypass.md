# SQL Injection: Authentication Bypass (Apprentice)

**Lab:** SQL injection vulnerability allowing login bypass  
**Difficulty:** Apprentice  
**Link:** [PortSwigger Lab](https://portswigger.net/web-security/sql-injection/lab-login-bypass)  

---

## 📝 Description
This lab demonstrates how SQL injection can be used to bypass authentication in a login form.  
By modifying the username input, I was able to trick the query into always returning `TRUE`, allowing me to log in as the administrator without knowing the password.  

---

## ⚙️ Steps Taken
1. Tested the login form by entering:  
admin'--
- This caused an error, which indicated that the input was being concatenated directly into an SQL query.  

2. Then I crafted a payload that always evaluates to true:  
admin' OR 1=1--
<img width="700" height="349" alt="SQL2_LAB1" src="https://github.com/user-attachments/assets/560d132c-7000-43d9-8ede-a05043071bce" />
<img width="700" height="349" alt="Screenshot_1" src="https://github.com/user-attachments/assets/f57c3ac4-9ed5-4064-8271-b03a9ccf28ac" />

- The query behind the scenes became something like:  
  ```sql
  SELECT * FROM users WHERE username = 'admin' OR 1=1--' AND password = '...';
  ```  
- Because `1=1` is always true, the query bypassed the password check.  

---

## ✅ Result
- Successfully logged in as the **administrator** user without needing the correct password.  

---

## 📚 What I Learned
- How SQL injection can be used to bypass authentication mechanisms.  
- How login forms are especially vulnerable when input is not sanitized.  
- The importance of testing different payloads to identify exploitable queries.  

