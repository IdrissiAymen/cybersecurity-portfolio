<img width="687" height="247" alt="OTW13" src="https://github.com/user-attachments/assets/a98c5ef5-6124-47d6-891d-df82b1192214" />
<img width="812" height="72" alt="OTW14" src="https://github.com/user-attachments/assets/e89b77b1-6039-49d8-bc1d-a4be874306b8" />
<img width="721" height="38" alt="Screenshot_2" src="https://github.com/user-attachments/assets/b1349683-1455-4d40-aef1-7e63958799b0" />

## Bandit Level 16 → Level 17

**Challenge Description:**  
The password for the next level could not be obtained directly. Instead, the task was to connect to different ports on `localhost` (in the range 31000–32000), find which ones were open, and determine which one was using SSL/TLS. The correct service would provide the next credentials.

---

**Steps Taken:**

1. **Scanned open ports** in the given range using `nmap`:
   ```bash
   nmap -p31000-32000 localhost
This revealed several open ports.

2. Checked which ports spoke SSL/TLS using openssl s_client. For example
#### openssl s_client -connect localhost:31790
One of the ports returned a block of text instead of echoing input.

3. Submitted the Bandit16 password (kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx) to that SSL-enabled port 
After typing the password, the server returned an RSA Private Key.

4.Saved the private key locally into a file named bandit16_key
nano bandit16_key
##### pasted the key here
chmod 600 bandit16_key

5. Used the private key to SSH into Bandit17:
ssh -i bandit16_key bandit17@bandit.labs.overthewire.org -p 2220
With this technique you go directly inside bandit17 without needing to type any password because you have already integrated the file bandit16_key.


