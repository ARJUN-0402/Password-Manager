#!/usr/bin/env python3
"""
Password Manager Application
Securely stores and manages passwords using encryption.
"""

import os
import json
import getpass
from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self, data_file="passwords.json", key_file="key.key"):
        """Initialize the Password Manager."""
        self.data_file = data_file
        self.key_file = key_file
        self.key = self.load_or_generate_key()
        self.cipher = Fernet(self.key)
        self.passwords = self.load_passwords()

    def generate_key(self):
        """Generate a new encryption key."""
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)
        return key

    def load_or_generate_key(self):
        """Load existing key or generate a new one."""
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                key = key_file.read()
        else:
            key = self.generate_key()
        return key

    def encrypt_data(self, data):
        """Encrypt data using the cipher."""
        return self.cipher.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        """Decrypt data using the cipher."""
        return self.cipher.decrypt(encrypted_data).decode()

    def load_passwords(self):
        """Load passwords from file."""
        if not os.path.exists(self.data_file):
            return {}
        
        try:
            with open(self.data_file, 'rb') as f:
                encrypted_data = f.read()
            if not encrypted_data:
                return {}
            decrypted_data = self.decrypt_data(encrypted_data)
            return json.loads(decrypted_data)
        except Exception as e:
            print(f"Error loading passwords: {e}")
            return {}

    def save_passwords(self):
        """Save passwords to file."""
        try:
            data = json.dumps(self.passwords)
            encrypted_data = self.encrypt_data(data)
            with open(self.data_file, 'wb') as f:
                f.write(encrypted_data)
        except Exception as e:
            print(f"Error saving passwords: {e}")

    def add_password(self, account, password):
        """Add a new password."""
        self.passwords[account] = password
        self.save_passwords()
        print(f"Password for {account} added successfully!")

    def get_password(self, account):
        """Retrieve a password."""
        return self.passwords.get(account, None)

    def list_accounts(self):
        """List all accounts."""
        return list(self.passwords.keys())

    def delete_password(self, account):
        """Delete a password."""
        if account in self.passwords:
            del self.passwords[account]
            self.save_passwords()
            print(f"Password for {account} deleted successfully!")
        else:
            print(f"No password found for {account}")


def main():
    """Main application loop."""
    pm = PasswordManager()
    
    while True:
        print("\n" + "="*40)
        print("Password Manager")
        print("="*40)
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. List all accounts")
        print("4. Delete a password")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            account = input("Enter account name: ").strip()
            if account:
                password = getpass.getpass("Enter password: ")
                if password:
                    pm.add_password(account, password)
                else:
                    print("Password cannot be empty!")
            else:
                print("Account name cannot be empty!")
        
        elif choice == '2':
            account = input("Enter account name: ").strip()
            if account:
                password = pm.get_password(account)
                if password:
                    print(f"Password for {account}: {password}")
                else:
                    print(f"No password found for {account}")
            else:
                print("Account name cannot be empty!")
        
        elif choice == '3':
            accounts = pm.list_accounts()
            if accounts:
                print("\nStored accounts:")
                for account in accounts:
                    print(f"- {account}")
            else:
                print("No accounts stored yet.")
        
        elif choice == '4':
            account = input("Enter account name to delete: ").strip()
            if account:
                confirm = input(f"Are you sure you want to delete {account}? (y/N): ").strip().lower()
                if confirm == 'y':
                    pm.delete_password(account)
            else:
                print("Account name cannot be empty!")
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()