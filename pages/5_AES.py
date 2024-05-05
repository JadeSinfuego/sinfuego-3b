from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
import os
import streamlit as st

def encrypt_AES(data, key):
    # Convert data to bytes
    data_bytes = data.encode()

    # Generate a random initialization vector
    iv = os.urandom(16)

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create a padder using PKCS7 padding scheme
    padder = padding.PKCS7(128).padder()

    # Apply padding to the data
    padded_data = padder.update(data_bytes) + padder.finalize()

    # Encrypt the padded data
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(padded_data) + encryptor.finalize()

    return iv, cipher_text

def decrypt_AES(iv, cipher_text, key):
    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create an unpadder using PKCS7 padding scheme
    unpadder = padding.PKCS7(128).unpadder()

    # Decrypt the cipher text
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(cipher_text) + decryptor.finalize()

    # Remove padding
    unpadded_data = unpadder.update(padded_data) + unpadder.finalize()

    # Convert bytes to string
    decrypted_data = unpadded_data.decode()

    return decrypted_data

# Generate a random 256-bit (32-byte) key
key = os.urandom(32)

# Data to be encrypted
data = st.text_input("Enter your text")

# Encrypt the data
iv, cipher_text = encrypt_AES(data, key)

# Decrypt the data
decrypted_data = decrypt_AES(iv, cipher_text, key)

st.write("Original data:", data)
st.write("Encrypted data:", cipher_text)
st.write("Decrypted data:", decrypted_data)
