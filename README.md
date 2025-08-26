# Password Manager 🔐

A secure password manager application that stores account credentials in an encrypted file using Python's cryptography library.

## Features
- Securely store account names and passwords
- AES encryption for data protection
- Simple command-line interface
- Key-based encryption with secure key storage

## Requirements
- Python 3.x
- cryptography library

## Installation
```bash
pip install cryptography
```

## Usage
```bash
python password_manager.py
```

## How It Works
1. Generates a secure encryption key on first run
2. Stores the key in a separate key file
3. Encrypts all password data before saving to file
4. Decrypts data when retrieving passwords