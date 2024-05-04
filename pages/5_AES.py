import streamlit as st
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# AES encryption function
def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

# AES decryption function
def decrypt_message(iv, ct, key):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
    return pt

# Streamlit UI
st.title("AES Encryption and Decryption")

# Encryption section
st.header("Encryption")
message = st.text_input("Enter message to encrypt:")
encrypt_button = st.button("Encrypt")

# Decryption section
st.header("Decryption")
iv = st.text_input("Enter IV:")
ct = st.text_input("Enter ciphertext:")
decrypt_button = st.button("Decrypt")

# AES key (fixed for demonstration purposes, in practice generate a secure random key)
key = get_random_bytes(16)

# Encrypt button event handler
if encrypt_button:
    if message:
        iv, ct = encrypt_message(message, key)
        st.write("IV:", iv)
        st.write("Ciphertext:", ct)
    else:
        st.warning("Please enter a message to encrypt.")

# Decrypt button event handler
if decrypt_button:
    if iv and ct:
        decrypted_message = decrypt_message(iv, ct, key)
        st.write("Decrypted message:", decrypted_message)
    else:
        st.warning("Please enter IV and ciphertext.")
