
<img width="622" height="135" alt="overthewire4" src="https://github.com/user-attachments/assets/739303a9-34b9-4011-a1bd-ba4744a748be" />

## Bandit Level 2 → Level 3

### Challenge
The password for the next level is stored in a file somewhere under the `inhere` directory and has the following properties:
- Human-readable
- Exactly **1033 bytes** in size
- Not executable

### Steps I Used
1. **Navigate into the `inhere` directory**  
   ```bash
   cd inhere
   
Search for the file with the correct properties
I used the find command with size and non-executable filters:
find . -type f -size 1033c ! -executable

Read the content of the file found
cat ./maybeinhere07/.file2
The password : HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
