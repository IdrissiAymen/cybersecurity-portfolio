<img width="548" height="254" alt="overthewire6" src="https://github.com/user-attachments/assets/9424d9bc-c609-4064-a80e-27fea75353a6" />

# OverTheWire Bandit: Level 7 → 8

## 🎯 Objective
The password for the next level (**bandit8**) is stored in the file `data.txt`, **next to the word `millionth`**.

---

## 📝 Steps I Took

1. **Read the instructions carefully**  
   The hint says the password is located next to the word `millionth` inside `data.txt`.

2. **Think about tools to use**  
   The file could be very large, so manually searching isn’t practical.  
   Best tool: `grep` (search for a string inside a file).

3. **Run `grep` to find the matching line**  
   ```bash
   grep "millionth" data.txt
This command searches through data.txt and prints the line containing millionth.

**View the result**
millionth dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
