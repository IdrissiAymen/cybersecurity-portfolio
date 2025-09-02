<img width="486" height="41" alt="OTW2" src="https://github.com/user-attachments/assets/7e068a43-74ee-43cd-a6b0-ecd4bdd4fb78" />

# OverTheWire Bandit: Level 12 → 13

## 🎯 Objective
The password for the next level (**bandit13**) is stored in a file (`data.txt`) that has been repeatedly compressed and represented as a hexdump.  
The goal is to extract and decompress it until a plain text file containing the password is obtained.

---

## 📝 Steps I Took

1. **Create a temporary working directory**  
   - Using `mktemp -d` ensures a unique folder to safely work in `/tmp`.  
   ```bash
   cd /tmp
   mktemp -d
   cd tmp.HBMzPxdtuY  # example folder created
#### Copy the hexdump file to the working directory
cp /home/bandit12/data.txt /tmp/tmp.HBMzPxdtuY
#### Convert the hexdump back to binary
xxd -r data.txt > data.bin
#### Identify the file type
file data.bin
(First check showed: gzip compressed data.) 
#### Rename and decompress accordingly
mv data.bin data.gz
gunzip data.gz
file data  # check next file type
#### Handle tar archives
mv data data.tar
tar -xf data.tar
ls -l  # see new files
file newfile  # check next file type
#### Repeat the process
Each new file may be another tar, gzip, or bzip2:
.tar → tar -xf
.gz → gunzip
.bz2 → bunzip2
Keep checking each time with file until you finally reach a plain text file.
###### Once file says ASCII text, display the content:
FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
