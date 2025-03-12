import string
import random
import streamlit as st
import re
import pyperclip

# Streamlit UI Setup
st.set_page_config(page_title="🔐 Secure Password Generator", layout="centered")

# Function to Generate Password
def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-./:;<=>?"
    return "".join(random.choice(characters) for _ in range(length))

# Function to Check Password Strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Common weak passwords
    common_passwords = ["12345678", "password", "qwerty", "Pakistan", "123456789", "abc123", "password123"]
    if password in common_passwords:
        return "❌ This password is too common! Choose a more unique one.", "Weak", 0

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🚨 Password should be at least **8 characters long**.")

    # Upper and Lower case check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔠 Include both **uppercase and lowercase letters**.")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 Include at least **one number**.")

    # Special character check
    if re.search(r"[!@#$%^&*()_+-./:;<=>?]", password):
        score += 1
    else:
        feedback.append("🔣 Include at least **one special character**.")

    # Bonus for extra secure length (>12)
    if len(password) > 12:
        score += 1

    # Strength Levels
    if score == 5:
        return "✅ **Strong Password!** 🔥", "Strong", score
    elif score >= 3:
        return "⚠️ **Moderate Password.** 🔄", "Moderate", score
    else:
        return "❌ **Weak Password!** 🚨", "Weak", score

# Streamlit UI Elements
st.title("🔒 Secure Password Generator & Strength Checker")

# Password Input (Live Checking)
password_input = st.text_input("📝 **Enter your password to check strength:**", type="password")

if password_input:
    strength_msg, strength_level, score = check_password_strength(password_input)
    st.write(strength_msg)
    st.progress(score / 5)

# Password Generator
st.subheader("🔑 **Generate a Strong Password**")
password_length = st.slider("📏 Select Password Length:", min_value=8, max_value=20, value=12)

# Password storage
generated_password = ""

if st.button("🎲 **Generate Password**"):
    generated_password = generate_password(password_length)
    st.success("🔐 **Generated Password:**")
    st.code(generated_password, language="plaintext")

    # Copy Button (Only if a password is generated)
    if generated_password:
        if st.button("📋 **Copy Password**"):
            pyperclip.copy(generated_password)
            st.success("✅ Password copied to clipboard!")

# Additional Security Tips
st.warning("⚠️ **Never share your password with anyone!**")
st.info("🔹 Use a mix of **uppercase, lowercase, numbers, and special characters** for stronger passwords.")

st.markdown("---")
st.markdown("🧑‍💻 **Sadia - Student at GIAIC** 🎓")
