import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if use_digits else ""
    special_characters = string.punctuation if use_special else ""

    # Combine selected character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure there are characters to select from
    if not all_characters:
        return "Error: Select at least one character type."

    # Ensure at least one character from each selected set is included
    password_chars = []
    if use_digits:
        password_chars.append(random.choice(digits))
    if use_special:
        password_chars.append(random.choice(special_characters))

    # Fill the rest of the password with random choices
    while len(password_chars) < length:
        password_chars.append(random.choice(all_characters))

    # Shuffle to randomize order
    random.shuffle(password_chars)

    return ''.join(password_chars)

# Streamlit UI setup
st.title("🔑 Password Generator")

# Sidebar inputs
length = st.sidebar.number_input("Password Length", min_value=8, max_value=32, value=12)
use_digits = st.sidebar.checkbox("Include Digits")
use_special = st.sidebar.checkbox("Include Special Characters")

# Generate Password
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write("### Generated Password:")  
    st.code(password, language="text")  
    st.balloons()