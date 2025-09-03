
<img width="628" height="45" alt="otw5" src="https://github.com/user-attachments/assets/2e1c11d3-bea0-434e-ae32-c6834a6561cb" />

<img width="335" height="79" alt="otw6" src="https://github.com/user-attachments/assets/d672ccb3-dc0d-4e14-b7d0-5e12203338eb" />

## Bandit Level 15 → 16

**Challenge:**  
The password for the next level can be retrieved by submitting the password of the current level to port **30001** on localhost using **SSL/TLS encryption**.

**Solution Steps:**  
1. Connected to the SSL/TLS-enabled port using OpenSSL:  
   ```bash
   openssl s_client -connect localhost:30001
After the handshake, I submitted the password from Level 15.
The server returned the password for the next level. (kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx)
