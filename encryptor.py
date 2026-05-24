import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file():
    file_path = filedialog.askopenfilename(title="Select File to Encrypt")
    if not file_path:
        return
    
    password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
    if not password:
        return

    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        salt = os.urandom(16)
        iv = os.urandom(16)
        key = derive_key(password, salt)

        encryptor = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend()).encryptor()
        ciphertext = encryptor.update(data) + encryptor.finalize()

        with open(file_path + ".enc", 'wb') as f:
            f.write(salt + iv + ciphertext)

        messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as: {os.path.basename(file_path)}.enc")
    except Exception as e:
        messagebox.onerror("Error", f"Encryption failed: {str(e)}")

def decrypt_file():
    file_path = filedialog.askopenfilename(title="Select Encrypted (.enc) File")
    if not file_path:
        return
    
    password = simpledialog.askstring("Password", "Enter decryption password:", show='*')
    if not password:
        return

    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()

        salt = file_data[:16]
        iv = file_data[16:32]
        ciphertext = file_data[32:]
        
        key = derive_key(password, salt)

        decryptor = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend()).decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

        if file_path.endswith(".enc"):
            output_path = file_path[:-4]
        else:
            output_path = file_path + ".dec"

        with open(output_path, 'wb') as f:
            f.write(decrypted_data)

        messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as: {os.path.basename(output_path)}")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed. Wrong password or corrupted file.")

# Setup User Interface
root = tk.Tk()
root.title("AES-256 File Locker")
root.geometry("300x150")

tk.Label(root, text="Advanced Encryption Tool", font=("Arial", 12, "bold")).pack(pady=10)
tk.Button(root, text="🔒 Encrypt a File", command=encrypt_file, width=20, bg="salmon").pack(pady=5)
tk.Button(root, text="🔓 Decrypt a File", command=decrypt_file, width=20, bg="lightgreen").pack(pady=5)

root.mainloop()
