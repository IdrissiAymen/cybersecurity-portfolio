# SQL Injection: WHERE Clause Hidden Data (Apprentice)

**Lab:** SQL injection vulnerability in WHERE clause allowing retrieval of hidden data  
**Difficulty:** Apprentice  
**Link:** [PortSwigger Lab](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)  

---

## 📝 Description
This lab demonstrates a basic **SQL injection** vulnerability in the `WHERE` clause of a product filter.  
By carefully modifying the input, it’s possible to access hidden products that are normally not shown to users.  

---

## ⚙️ Steps Taken
1. Started by testing the parameter with a single quote (`'`):  
<img width="700" height="349" alt="SQL_LAB1" src="https://github.com/user-attachments/assets/77d78837-a594-4711-8e90-7111097d229a" />
<img width="700" height="349" alt="SQL_LAB2" src="https://github.com/user-attachments/assets/f3693a66-9b6e-43cf-9310-51b59ee28858" />
- This returned an **SQL error**, which confirmed that the application was directly embedding user input into a query.  

2. Next, I tried using a tautology injection:
   category='+OR+1=1--
<img width="700" height="349" alt="SQL_LAB3" src="https://github.com/user-attachments/assets/e58d1b05-859e-44f1-ad15-ea051b8704b6" />
- The `OR 1=1` condition always evaluates to `TRUE`.  
- This forced the database to return **all products**, not just the intended category.  

---

## ✅ Result
- Hidden products appeared on the website.  
- Proved that the filtering logic was vulnerable to SQL injection.  

---

## 📚 What I Learned
- How to detect SQL injection by causing errors with a single quote.  
- How to use a simple **OR 1=1** injection to bypass query restrictions.  
- Basic understanding of how attackers can retrieve unintended data from databases.  


