# Step 1 – Prepare Test Environment

I created a folder called `ransomware` and added a few test files inside it.  
This simulates the “target” files for the ransomware.

<img width="1339" height="822" alt="py1" src="https://github.com/user-attachments/assets/1e4b7e18-345e-4d17-8b09-a6de15ab1e37" />

# Step 2 – Create the Script

Created a Python script called `definetlynotahacker.py` and started with:

```python
#!/usr/bin/env python3
import os

files = os.listdir()
print(files)
```
This lets us see all files in the directory.
I added an if statement to skip the script itself so it won't encrypt itself.
<img width="1372" height="811" alt="py2" src="https://github.com/user-attachments/assets/6c3022a9-4001-4ace-ad70-c3ade5241f10" />

---

## 3️⃣ Step 3 – Filter Only Files (`step3.md`)

# Step 3 – Filter Only Files

When I added a folder to the directory, it showed up in the list.  
To make sure only files are processed, I used:

```python
if os.path.isfile(file):
    files.append(file)
```
Now only real files are encrypted, folders are skipped.
<img width="1371" height="821" alt="py3" src="https://github.com/user-attachments/assets/261cd9bf-b30a-49f3-a63e-278a55612307" />

