<img width="904" height="613" alt="overthewire5" src="https://github.com/user-attachments/assets/3f806b7e-e6a4-416d-8c89-a90693ca5a7a" />

# OverTheWire Bandit: Level 6 → 7

## 🎯 Objective
Find the password for the next level (**bandit7**).  
Conditions given in the challenge:  
- The file is **owned by user `bandit7`**  
- The file is **owned by group `bandit6`**  
- The file is **exactly 33 bytes** in size  

---

## 📝 Steps I Took

1. **Check the challenge hint**  
   Learned that the password file is hidden somewhere on the system, not in the home directory.

2. **Test `find` with size in current directory**  
   ```bash
   find . -type f -size 33c
   → No results, because this only searches the current folder (./).
  ## Search the entire filesystem for 33-byte files
 #### find / -type f -size 33c 2>/dev/null
 Refine search with user and group filters
#### find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
This matched exactly one file:
#### /var/lib/dpkg/info/bandit7.password
Read the password directly using full path
#### cat /var/lib/dpkg/info/bandit7.password

## Key Learnings

./ searches only the current directory tree. / searches the entire filesystem.

find filters:

-user → search by file owner

-group → search by group owner

-size 33c → file is exactly 33 bytes (c = bytes)

2>/dev/null suppresses error messages, making results easier to read.

Absolute paths (/var/lib/...) allow direct access without using cd.


