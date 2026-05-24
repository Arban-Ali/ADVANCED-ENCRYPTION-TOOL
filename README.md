# ADVANCED-ENCRYPTION-TOOL
# 🔒 AES-256 File Locker

A lightweight, secure, and user-friendly desktop application built in Python to encrypt and decrypt sensitive files using the robust **AES-256 (Advanced Encryption Standard)** algorithm.

---

## ✨ Features
* **Strong Encryption:** Uses AES-256 bit encryption in CFB mode.
* **Secure Key Derivation:** Uses PBKDF2HMAC with SHA-256 and 100,000 iterations to turn passwords into strong keys.
* **Unique Salting:** Generates a random cryptographic salt and Initialization Vector (IV) for every single file.
* **User-Friendly GUI:** Simple, minimalist interface built with Tkinter for effortless file handling.
* **No Cloud Dependency:** Works 100% offline. Your data and passwords never leave your machine.

---

## 🛠️ Prerequisites

Before running the application, make sure you have the following installed on your computer:

1. **Python 3.x** (Ensure you check the box to **"Add Python to PATH"** during installation).
2. **Pip** (Python package installer, included automatically with Python).

---

## 🚀 Quick Start Guide

### 1. Clone or Download this Repository
Download this project to your local computer and open the project directory in your terminal or command prompt.

### 2. Install Required Security Package
This application relies on the trusted `cryptography` library. Install it by running:
```bash
pip install cryptography
```

### 3. Run the Application
Launch the application with the following command:
```bash
python encryptor.py
```

---

## 📖 How to Use

### 🔒 Encrypting a File
1. Click the **🔒 Encrypt a File** button.
2. Select any file from your computer that you want to secure.
3. Enter a strong password when prompted.
4. The tool will generate a locked copy of your file with a `.enc` extension in the same folder.

### 🔓 Decrypting a File
1. Click the **🔓 Decrypt a File** button.
2. Select your encrypted file (ending in `.enc`).
3. Enter the exact password used during encryption.
4. The tool will restore your original file instantly.

---

## 🛡️ Security Architecture
* **Algorithm:** AES-256-CFB (Cipher Feedback Mode)
* **Key Derivation Function:** PBKDF2 (Password-Based Key Derivation Function 2)
* **Salt Size:** 16 Bytes (Randomly generated via `os.urandom`)
* **IV Size:** 16 Bytes (Randomly generated via `os.urandom`)

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).





OUTPUT: 
<img width="1920" height="1032" alt="Image" src="https://github.com/user-attachments/assets/48cc5643-5167-42e5-bc47-45127e8ce076" />
