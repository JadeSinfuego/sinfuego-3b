import streamlit as st
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# AES Encryption

def encrypt_text_aes(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    # Add padding to the plaintext to make it align with the block size
    padded_plaintext = _pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def _pad(data, block_size):
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length]) * padding_length
    return data + padding

def decrypt_text_aes(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def encrypt_file_aes(file_path, key):
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    with open(file_path + '.enc', 'wb') as f:
        f.write(ciphertext)

def decrypt_file_aes(file_path, key):
    with open(file_path, 'rb') as f:
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    with open(file_path[:-4], 'wb') as f:
        f.write(plaintext)

aes_key = get_random_bytes(16)  # Generate a 128-bit AES key
plaintext = b'Hello, World!'
encrypted_text_aes = encrypt_text_aes(plaintext, aes_key)
decrypted_text_aes = decrypt_text_aes(encrypted_text_aes, aes_key)
st.write("AES Encrypted Text:", encrypted_text_aes)
st.write("AES Decrypted Text:", decrypted_text_aes)      