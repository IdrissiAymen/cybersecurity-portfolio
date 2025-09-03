<img width="539" height="92" alt="OTW4" src="https://github.com/user-attachments/assets/6e3fa86c-79b1-4c96-b86c-d69c19a7f0bd" />

## Bandit Level 14 → 15

Challenge: The password for the next level had to be retrieved by submitting the current password to a service running locally on port 30000.
Action: I used nc (netcat) to connect to the local service 
##### nc localhost 30000

Then I provided the bandit14 password, and the service responded with the password for bandit15.
Key Skill Learned: How to use netcat to interact with network services and understand client-server communication over TCP. 
The password for this level is : 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo


