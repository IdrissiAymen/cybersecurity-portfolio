<img width="856" height="582" alt="otw10" src="https://github.com/user-attachments/assets/4bb2caaa-91db-4bf9-9787-1b898224e475" />
<img width="817" height="630" alt="otw11" src="https://github.com/user-attachments/assets/aece1a0c-790f-4ed1-9ff0-2fdce25d0d14" />

# OverTheWire Bandit: Level 10 → 11

## 🎯 Objective
The password for the next level (**bandit11**) is stored in the file `data.txt`.  
- The file contains **Base64-encoded data**.

---

## 📝 Steps I Took

1. **Inspect the file**
```bash
cat data.txt
This shows a long string of characters, which is Base64-encoded.
Decode the Base64 string
I copied the content and used an online Base64 decoder.
After decoding, I obtained the password for bandit11.
