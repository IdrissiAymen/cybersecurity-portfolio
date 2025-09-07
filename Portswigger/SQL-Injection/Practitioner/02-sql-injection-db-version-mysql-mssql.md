<img width="771" height="64" alt="Capture d'écran 2025-09-07 212809" src="https://github.com/user-attachments/assets/7d9127b1-e4af-40d3-b30c-2febfebe96c3" />

<img width="1656" height="220" alt="Capture d'écran 2025-09-07 212759" src="https://github.com/user-attachments/assets/5581aafa-f886-4a76-b8b1-076c6d0e90dd" />

# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft

## Steps I took
1. Tested the category parameter with `'` → saw an error, confirming SQL injection.
2. Checked the number of columns with `UNION SELECT NULL, NULL#` → confirmed there are 2 columns.
3. Used this payload to extract the version:
 ' UNION SELECT @@version, 'def'#
- `@@version` returns the database version string.
- `'def'` is just a filler value for the second column.
- `#` is the comment syntax for MySQL (instead of `--`).

## Result
The page displayed the database version string → lab solved ✅.

## What I learned
- How to determine the correct number of columns using `NULL` tests.
- Different comment styles across databases (`--` for Oracle/SQL Server, `#` for MySQL).
- The `@@version` variable reveals database version in MySQL and Microsoft SQL.


