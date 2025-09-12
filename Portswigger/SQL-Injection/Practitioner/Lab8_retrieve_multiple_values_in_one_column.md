<img width="1499" height="729" alt="Screenshot_19" src="https://github.com/user-attachments/assets/9054f57b-137c-4de4-812f-281aa183d756" />

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
'''
''''markdown
### 2 Test type-compatibility / extract one column
