# 🔐 Ransomware Simulation (Educational Project)

## ⚠️ For learning only
This project is purely for practicing cybersecurity in a lab environment. It shows how ransomware works internally — no real attacks here.

<img width="1086" height="703" alt="py14" src="https://github.com/user-attachments/assets/4d008689-b8a1-4531-bb4e-3891fe026dd8" />

## 📌 What This Project Is

This is a small Python project that simulates what ransomware does:

-Looks through files in a folder

-Encrypts them using a key

-Saves the key so you can decrypt later

-Simulates a ransom message with a passphrase

It’s meant to help understand ransomware mechanics and how to defend against them.

## 🎯 Why I Built It

I wanted to learn:

-How files and folders are handled in Python

-How to filter files safely

-How encryption and decryption work with cryptography.Fernet

-How ransomware logic is structured in a controlled lab

Basically, it’s a way to see “what ransomware actually does” without putting anyone at risk.

## ⚙️ How It Works

-The script scans the folder for files.

-Skips itself, the key file, and any folders.

-Generates a symmetric encryption key and saves it in thekey.key.

-Encrypts the files using the key.

-A separate decryption script can read the key and restore the files.

-Added a simple passphrase mechanism to simulate a ransom check (if you enter the correct word, it decrypts).

## 🖥 What You’ll See

-Screenshots in this repo show:
-Files before encryption

-Files after encryption

-Files decrypted back to normal

-(Check the /screenshots folder for visuals)

## 🛡 What I Learned

-This project made me think about:

-Why endpoint monitoring and file integrity checks are important

-The importance of safe key storage
