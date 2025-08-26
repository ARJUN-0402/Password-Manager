#!/usr/bin/env python3
"""
Test script for Password Manager
"""

from password_manager import PasswordManager

def test_password_manager():
    """Test the PasswordManager class functionality."""
    print("Testing Password Manager...")
    
    # Create a PasswordManager instance
    pm = PasswordManager()
    
    # Test adding a password
    print("\n1. Testing add_password...")
    pm.add_password("test_account", "test_password")
    
    # Test retrieving a password
    print("\n2. Testing get_password...")
    password = pm.get_password("test_account")
    print(f"Retrieved password: {password}")
    
    # Test listing accounts
    print("\n3. Testing list_accounts...")
    accounts = pm.list_accounts()
    print(f"Stored accounts: {accounts}")
    
    # Test deleting a password
    print("\n4. Testing delete_password...")
    pm.delete_password("test_account")
    
    # Test listing accounts again
    print("\n5. Testing list_accounts after deletion...")
    accounts = pm.list_accounts()
    print(f"Stored accounts: {accounts}")
    
    print("\nTest completed successfully!")

if __name__ == "__main__":
    test_password_manager()