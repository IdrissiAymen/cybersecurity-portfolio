
<img width="906" height="580" alt="overthewire7" src="https://github.com/user-attachments/assets/862399a0-9626-4373-a357-472dd0ab148e" />

# OverTheWire Bandit: Level 8 → 9

## 🎯 Objective
The password for the next level (**bandit9**) is stored in the file `data.txt`  
👉 It is the **only line of text that occurs once**.

---

## 📝 Steps I Took

1. **Understand the task**  
   - `data.txt` has many lines.  
   - Most lines are duplicates.  
   - Only **one line appears exactly once**, and that line is the password.

2. **Try with `uniq`**  
   ```bash
   uniq data.txt
   
This removes duplicate consecutive lines, but still shows one copy of every repeated value. Not enough to isolate the password.

Realize duplicates need to be consecutive
uniq only works properly if identical lines are next to each other.
So first, I need to sort the file.
Combine sort with uniq -u (sort data.txt | uniq -u)

#### the password that i got : 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
