import hashlib
import streamlit as st

st.header("Welcome to SHA-384!🔐")

st.write('SHA-384, short for Secure Hash Algorithm 384, is part of the SHA-2 (Secure Hash Algorithms 2nd version) suite that was developed by the National Institutes of Standards and Technology (NIST) and published in 2001. Also used as a unique file identifier, that generates a 384-bit message digest. It is part of the Secure Hash Algorithm 3 (SHA-3) family.')

def sha384_hash(input_string):
    # Encode the input string to bytes
    input_bytes = input_string.encode()

    # Create a new SHA-384 hash object
    sha384_hash_obj = hashlib.sha384()

    # Update the hash object with the input bytes
    sha384_hash_obj.update(input_bytes)

    # Get the hexadecimal representation of the hash value
    hash_hex = sha384_hash_obj.hexdigest()

    return hash_hex

# Example usage
input_string = "Hello, World!"
sha384_hash_value = sha384_hash(input_string)
print("SHA-384 Hash:", sha384_hash_value)

genre = st.radio(
    "Choose Input:",
    ["Text", "File"])

if genre == 'Text':
    st.write('Input Your Text.')
    input_string = st.text_area('Plaintext', placeholder="Input Text...")
    button = st.button("Submit", type="primary")

    if button:
        if input_string:  # Check if input_string is not empty
            st.write("Input Text:", input_string)
            sha384_hash_value = sha384_hash(input_string)
            st.write("SHA-384 hash of '{}' is: {}".format(input_string, sha384_hash_value))
        else:
            st.warning("Please input text for SHA-384 hash to work!")

elif genre == 'File':
    st.write('Enter Your Selected File.')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # Read file contents as string
        file_contents = uploaded_file.getvalue().decode("utf-8")
        st.write("File contents:", file_contents)

        # Compute SHA-384 hash of file contents
        sha384_hash_value = sha384_hash(file_contents)
        st.write("SHA-384 hash of file contents:", sha384_hash_value)

else:
    st.write("Please choose.")