<img width="600" height="349" alt="Screenshot_2" src="https://github.com/user-attachments/assets/d5c077d7-6ae1-4f8a-85a7-a27bf86a5fb0" />

# Lab: SQL injection attack, querying the database type and version on Oracle

**Category:** SQL Injection → Practitioner  
**Objective:** Display the database version string.

---

## Steps I Took

1. Tested the category parameter with a single quote (`'`) → this confirmed that the input was vulnerable to SQL injection.  
2. Knew that Oracle requires selecting from a table in UNION queries. The special table `dual` is often used.  
3. Learned that Oracle stores version info in the `v$version` view.  
4. Constructed a UNION-based payload to retrieve the banner column from that view:  

category=gifts' UNION SELECT banner, 'def' FROM v$version--
The query successfully returned the Oracle database version string.

---

## What I Learned
- Oracle UNION injections require selecting from a valid table/view (`dual` or others).  
- System info like DB version is often stored in system views (`v$version`).  
- Commenting (`--`) helps terminate the query and ignore trailing code.  

---

