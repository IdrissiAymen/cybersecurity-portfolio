
<img width="817" height="543" alt="OTW300" src="https://github.com/user-attachments/assets/57b935d2-9e0b-4ceb-9fe1-7688111e1c41" />

## Bandit Level 18 → Level 19

### Challenge
The password for the next level is stored in a file called `readme` located in Bandit18’s home directory.  
However, when attempting to SSH into Bandit18 normally, the connection closes immediately, preventing manual commands.

### Solution
To bypass the auto-logout, I executed the command directly during the SSH login:

```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
and after u type the current pw u get
 
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8
