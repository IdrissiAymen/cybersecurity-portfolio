<img width="600" height="345" alt="Screenshot_3" src="https://github.com/user-attachments/assets/9bdb45f2-2688-4d2e-9c16-8c88f773da58" />

<img width="600" height="345" alt="Screenshot_4" src="https://github.com/user-attachments/assets/9509c923-31ee-4ed8-8078-5746e9971c3b" />

# Bandit Challenge 20 --> 21: Using Netcat to Capture the Next Level Password

**Objective:**  
The goal of this challenge was to interact with a setuid binary (`suconnect`) that connects to a specified port on localhost, reads the previous level's password, and returns the next level's password. The task was to use Netcat (`nc`) to capture this communication.

---

## Step 1: Start a listener with Netcat

In the first terminal, I ran:

nc -l -p 5555

- l tells Netcat to listen for incoming connections.
- p 5555 specifies the port on which Netcat waits.
This terminal now acts as a server, ready to accept the connection from suconnect.

## Step 2: Run the setuid binary
In a second terminal, I executed:
./suconnect 5555

- ./suconnect runs the binary from the current directory.
- 5555 is the port number that the binary will connect to on localhost (our listener).
## Step 3: Send the previous password

Once the binary connects to the Netcat listener, I sent the previous level's password (bandit20 password).
Netcat receives this connection and transmits the password to the binary automatically (or manually typed in the listener terminal
## Step 4: Capture the next level password

After sending the correct password, the binary responded with the password for the next level (bandit21), which appeared directly in the Netcat listener terminal.
