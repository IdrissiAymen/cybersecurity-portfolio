<img width="601" height="400" alt="Screenshot_5" src="https://github.com/user-attachments/assets/c245cd8a-421f-4d1f-981e-b6220135f672" />

# Bandit Challenge 21 --> 22: Exploiting a Cron Job to Retrieve the Next Level Password

**Objective:**  
The goal of this challenge was to retrieve the password for the next Bandit level (bandit22) by investigating a cron job that runs automatically at regular intervals.

---

## Step 1: Identify the cron job

I looked in the system cron directory:

- ls -l /etc/cron.d/
and found a cron job pointing to a script:
- /usr/bin/cronjob_bandit22.sh &> /dev/null
The &> /dev/null part means the output is redirected and not visible.
The script runs as a scheduled task automatically.

## Step 2: Inspect the script
I read the contents of the script:
- cat /usr/bin/cronjob_bandit22.sh
The script contained:
- #!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

- The chmod 644 command makes the file readable by everyone.
- The script copies the bandit22 password into a temporary file in /tmp.
## Step 3: Retrieve the password
- cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
- Output : tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q

