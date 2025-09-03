<img width="841" height="593" alt="OTW3" src="https://github.com/user-attachments/assets/7499689f-3c8b-4dc5-9f85-50f9843ab263" />

## Bandit Level 13 → 14

#### Challenge: The password for the next level was not stored directly in a file, but provided via an SSH private key.

Action: I found the sshkey.private file in bandit13’s home directory, copied it into a temporary directory I controlled (/tmp), fixed its permissions with chmod 600, and used it to log in as bandit14 with 
##### (ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220)
Key Skill Learned: How to properly handle SSH private keys (permissions, ownership) and authenticate without a password.
 
