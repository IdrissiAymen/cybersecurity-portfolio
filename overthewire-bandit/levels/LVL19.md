<img width="824" height="363" alt="Screenshot_3" src="https://github.com/user-attachments/assets/f22f0ae3-226a-42ad-8fb2-b63a04574d46" />

## Bandit Level 19 → Level 20

### Challenge
A setuid binary is located in Bandit19’s home directory. This binary executes commands with the permissions of its owner (bandit20).  
The goal is to use this binary to read Bandit20’s password, which is stored in `/etc/bandit_pass/bandit20`.

### Solution
1. First, I listed the files in the home directory:
   ```bash
   ls -l
##### I found the binary bandit20-do with setuid permissions (-rwsr-x---).
2. Running it without arguments showed usage instructions:
./bandit20-do
Output:
Run a command as another user.
Example: ./bandit20-do id
3. I used the binary to read Bandit20’s password:
./bandit20-do cat /etc/bandit_pass/bandit20
And i got this pw : 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO

