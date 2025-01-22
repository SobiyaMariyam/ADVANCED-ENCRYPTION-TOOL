# ADVANCED-ENCRYPTION-TOOL
***COMPANY***: CDETECH IT SOLUTION

***NAME***: Sobiya vhora

***INTERN ID***: CT08GRD

***DOMAIN***: Cyber Security & Ethical Hacking

***BATCH DURATION***: December 25th, 2024 to January 25th, 2025

***MENTOR NAME***: Neela Santhosh

***DESCRIPTION OF TASK-4***
# AES-256 File Encryption Tool

## Objective
This tool provides a secure and user-friendly way to encrypt and decrypt files using the AES-256 encryption standard. With a simple graphical user interface (GUI), users can select files, provide a password, and perform encryption or decryption seamlessly.

---

## Features

1. **AES-256 Encryption**:
   - Implements AES-256 in CBC (Cipher Block Chaining) mode for robust file encryption.

2. **Password-Based Key Derivation**:
   - Derives a 256-bit key from the user-provided password using the SHA-256 hash function.

3. **Random Initialization Vector (IV)**:
   - Generates a unique 16-byte IV for each encryption to ensure strong cryptographic security.

4. **File Handling**:
   - Allows users to encrypt any file type, saving the encrypted version with a `.enc` extension.
   - Decrypts `.enc` files back to their original format.

5. **Graphical User Interface**:
   - Built with `tkinter` for ease of use, featuring file selection and password input fields.

6. **Padding and Unpadding**:
   - Ensures data size compatibility with AES block size requirements through padding.

---

## Code Description

### Imports
- **`os`**: Provides file handling utilities.
- **`hashlib`**: Used to derive a fixed-length encryption key from the password.
- **`tkinter`**: Creates the GUI for file selection and encryption/decryption operations.
- **`Crypto.Cipher.AES`**: Provides AES encryption and decryption functionality.
- **`Crypto.Random.get_random_bytes`**: Generates random IVs for encryption.

### Core Functions

1. **`pad(data)`**:
   - Adds padding to the input data to align with AES's 16-byte block size.

2. **`unpad(data)`**:
   - Removes padding from decrypted data to restore the original file content.

3. **`generate_key(password)`**:
   - Creates a 256-bit key by hashing the password with SHA-256.

4. **`encrypt_file(file_path, password)`**:
   - Encrypts a file using AES-256.
   - Saves the encrypted file with a `.enc` extension.
   - Combines the IV and ciphertext for secure storage.

5. **`decrypt_file(file_path, password)`**:
   - Decrypts an AES-256 encrypted file.
   - Extracts the IV from the encrypted file and restores the original file without the `.enc` extension.

6. **`select_file()`**:
   - Opens a file dialog for the user to select a file for encryption or decryption.

7. **`encrypt_action()`**:
   - Triggered when the "Encrypt" button is clicked.
   - Validates inputs and calls `encrypt_file`.

8. **`decrypt_action()`**:
   - Triggered when the "Decrypt" button is clicked.
   - Validates inputs and calls `decrypt_file`.

### Graphical User Interface (GUI)
- **File Selection**:
  - Entry field and "Browse" button for choosing files.
- **Password Input**:
  - Secure password input field with masked characters.
- **Action Buttons**:
  - "Encrypt" and "Decrypt" buttons to perform respective operations.

---

## How to Execute

### Prerequisites
1. Install Python (>=3.8).
2. Install the `pycryptodome` library:
   ```bash
   pip install pycryptodome
   ```

### Steps
1. Save the code to a file, e.g., `aes_encryption_tool.py`.
2. Run the script:
   ```bash
   python aes_encryption_tool.py
   ```
3. The GUI will appear. Use the following steps:
   - **Encryption**:
     1. Click "Browse" to select a file.
     2. Enter a password.
     3. Click "Encrypt". The encrypted file will be saved with a `.enc` extension.
   - **Decryption**:
     1. Select an encrypted file (`.enc`).
     2. Enter the correct password.
     3. Click "Decrypt". The decrypted file will be restored.

---

## Security Notes
- Use strong, unique passwords for encryption.
- Encrypted files require the exact password for decryption.
- This tool does not store passwords; ensure you remember the password used.

## Example

### Encryption
#### Input:
- File: `example.txt`
- Password: `securepassword`

#### Output:
- Encrypted File: `example.txt.enc`

### Decryption
#### Input:
- File: `example.txt.enc`
- Password: `securepassword`

#### Output:
- Decrypted File: `example.txt`

---
![Image](https://github.com/user-attachments/assets/bd4fcc09-dfc5-4288-9d78-c0bd22db59d0)

## Encypted File Data
![Image](https://github.com/user-attachments/assets/6d78215e-d283-461d-a232-49de5da0cffa)

## Wrong Password Decryption
![Image](https://github.com/user-attachments/assets/63b9a520-5040-465c-8e42-be30866b1fd0)

## Right Password Decryption
![Image](https://github.com/user-attachments/assets/2ac0581a-8305-4ae8-86d4-06ddbcbe4449)
---

