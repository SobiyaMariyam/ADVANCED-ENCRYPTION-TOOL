import os
import hashlib
from tkinter import Tk, filedialog, Label, Button, Entry, messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(data):
    """
    Add padding to the data to make it a multiple of 16 bytes (block size for AES).
    AES requires the input data to be a multiple of the block size.
    """
    return data + b"\0" * (16 - len(data) % 16)

def unpad(data):
    """
    Remove padding from the decrypted data.
    This restores the original data after decryption.
    """
    return data.rstrip(b"\0")

def generate_key(password):
    """
    Generate a 256-bit key (32 bytes) using the SHA-256 hash of the provided password.
    A fixed-length key is necessary for AES encryption.
    """
    return hashlib.sha256(password.encode()).digest()

def encrypt_file(file_path, password):
    """
    Encrypt the contents of a file using AES-256 in CBC mode.
    The encrypted file is saved with a .enc extension.
    """
    key = generate_key(password)  # Generate encryption key from password
    iv = get_random_bytes(16)     # Generate a random 16-byte initialization vector (IV)
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Create AES cipher object in CBC mode
    
    # Read the contents of the file
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    
    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(pad(plaintext))
    
    # Save the encrypted file (IV + ciphertext)
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + ciphertext)
    
    messagebox.showinfo("Success", f"File encrypted successfully: {encrypted_file_path}")

def decrypt_file(file_path, password):
    """
    Decrypt an AES-256 encrypted file using the provided password.
    The decrypted file is saved without the .enc extension.
    """
    key = generate_key(password)  # Generate decryption key from password
    
    # Read the IV and ciphertext from the encrypted file
    with open(file_path, 'rb') as f:
        iv = f.read(16)  # First 16 bytes are the IV
        ciphertext = f.read()
    
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Create AES cipher object in CBC mode
    plaintext = unpad(cipher.decrypt(ciphertext))  # Decrypt and unpad the plaintext
    
    # Save the decrypted file (original name without .enc)
    decrypted_file_path = file_path.rstrip(".enc")
    with open(decrypted_file_path, 'wb') as f:
        f.write(plaintext)
    
    messagebox.showinfo("Success", f"File decrypted successfully: {decrypted_file_path}")

def select_file():
    """Open a file dialog for the user to select a file."""
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file_path.delete(0, "end")  # Clear any existing path in the entry field
        entry_file_path.insert(0, file_path)  # Insert the selected file path

def encrypt_action():
    """Handle the encrypt button click event."""
    file_path = entry_file_path.get()
    password = entry_password.get()
    if not file_path or not password:
        messagebox.showwarning("Warning", "Please select a file and enter a password.")
        return
    encrypt_file(file_path, password)

def decrypt_action():
    """Handle the decrypt button click event."""
    file_path = entry_file_path.get()
    password = entry_password.get()
    if not file_path or not password:
        messagebox.showwarning("Warning", "Please select a file and enter a password.")
        return
    decrypt_file(file_path, password)

# Create the main GUI window
root = Tk()
root.title("AES-256 File Encryption Tool")
root.geometry("400x200")

# File selection section
Label(root, text="Select File:").pack(pady=5)
entry_file_path = Entry(root, width=40)
entry_file_path.pack(pady=5)
Button(root, text="Browse", command=select_file).pack(pady=5)

# Password entry section
Label(root, text="Enter Password:").pack(pady=5)
entry_password = Entry(root, show="*", width=40)
entry_password.pack(pady=5)

# Action buttons for encryption and decryption
Button(root, text="Encrypt", command=encrypt_action, width=10).pack(side="left", padx=50, pady=10)
Button(root, text="Decrypt", command=decrypt_action, width=10).pack(side="right", padx=50, pady=10)

# Run the main GUI loop
root.mainloop()
