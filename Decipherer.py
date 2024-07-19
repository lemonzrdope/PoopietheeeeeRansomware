from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to load the key from a file
def load_key(key_file_path):
    """Load the key from a .key file."""
    with open(key_file_path, 'rb') as key_file:
        return Fernet(key_file.read())

# Function to decrypt a file
def decrypt_file(file_path, cipher_suite):
    """Decrypt a single file."""
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Function to decrypt all files in a directory
def decrypt_directory(directory_path, cipher_suite):
    """Decrypt all files in a directory."""
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path, cipher_suite)

# Function to show a file dialog to select the directory
def select_directory():
    """Open a dialog to select a directory."""
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Select the directory with encrypted files")
    return directory

# Function to show a file dialog to select the key file
def select_key_file():
    """Open a dialog to select the key file."""
    root = tk.Tk()
    root.withdraw()
    key_file = filedialog.askopenfilename(title="Select the key file", filetypes=[("Key files", "*.key")])
    return key_file

# Main function to handle decryption
def main():
    # Ask the user for the key file and directory
    key_file_path = select_key_file()
    if not key_file_path:
        messagebox.showerror("Error", "No key file selected!")
        return

    directory_path = select_directory()
    if not directory_path:
        messagebox.showerror("Error", "No directory selected!")
        return

    # Load the key and create a cipher suite
    cipher_suite = load_key(key_file_path)

    # Decrypt the files
    decrypt_directory(directory_path, cipher_suite)

    # Show a success message
    messagebox.showinfo("Success", "Files have been decrypted successfully!")

if __name__ == "__main__":
    main()
