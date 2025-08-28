
<img width="827" height="574" alt="otw8" src="https://github.com/user-attachments/assets/c16e6eb1-a654-4379-b8e7-338d5436e547" />

<img width="823" height="560" alt="otw9" src="https://github.com/user-attachments/assets/d7de8b8d-0bbb-465f-bf77-588a23bb770d" />


# OverTheWire Bandit: Level 9 → 10

## 🎯 Objective
The password for the next level (**bandit10**) is stored in `data.txt` as a **human-readable string**, preceded by several `=` characters.

---

## 📝 Steps I Took

1. **Understand the task**  
   - The file is mostly binary, but contains some human-readable strings.  
   - The password is one of these readable strings, marked by `=` at the beginning.

2. **Use `strings` to extract readable parts**
```bash
strings data.txt
and it said ==== the ==== paswword === is === FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
