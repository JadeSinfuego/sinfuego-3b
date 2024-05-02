import streamlit as st
import hashlib
import pandas as pd

st.header("Welcome to SHA1!🔐")
st.write('SHA1')

def compute_sha1(input_string):
    # Create a SHA-1 hash object
    sha1_hash = hashlib.sha1()

    # Update the hash object with the input string
    sha1_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    hex_digest = sha1_hash.hexdigest()

    return hex_digest

genre = st.radio(
    "Choose Input",
    ["Text", "File"])

if genre == 'Text':
    st.write('You selected Text.')
    input_string = st.text_area('Plaintext', placeholder="Input Text...")
    button = st.button("Submit", type="primary")

    if button:
        if input_string:  # Check if input_string is not empty
            st.write("Input Text:", input_string)
            sha1_hash = compute_sha1(input_string)
            st.write("SHA1 hash of '{}' is: {}".format(input_string, sha1_hash))
        else:
            st.warning("Please input text for SHA1 hash to work!")

elif genre == 'File':
    st.write('You selected File.')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Read file contents as string
        file_contents = uploaded_file.getvalue().decode("utf-8")
        st.write("File contents:", file_contents)

        # Compute SHA1 hash of file contents
        sha1_hash = compute_sha1(file_contents)
        st.write("SHA1 hash of file contents:", sha1_hash)
        
else:
    st.write("Please choose.")




