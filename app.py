import streamlit as st

# Function to check password strength
def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*" for char in password):
        strength += 1
    return strength

# Custom CSS for styling
def set_custom_style():
    st.markdown(
        """
        <style>
        /* Full border around input fields with eye icon */
        div.stTextInput > div {
            border: 2px solid #3498db;
            border-radius: 5px;
            padding: 10px;
            background-color: #e6f3ff;  /* Light blue background */
        }

        /* Full border around the entire app */
        .stApp {
            border: 4px solid #3498db;
            border-radius: 10px;
            padding: 20px;
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        }

        /* Title */
        h1 {
            color: #2c3e50;
            text-align: center;
            font-size: 36px;
            margin-bottom: 20px;
        }

        /* Progress bar */
        .stProgress > div > div {
            background-color: #3498db;
            border-radius: 10px;
        }

        /* Buttons */
        .stButton button {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
        }

        /* Feedback messages */
        .stSuccess {
            color: #27ae60;
            font-size: 18px;
        }
        .stWarning {
            color: #f39c12;
            font-size: 18px;
        }
        .stError {
            color: #e74c3c;
            font-size: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Streamlit App
def main():
    # Set custom style
    set_custom_style()

    # App title
    st.title("Password Strength Meter 🔒")

    # Bold text for instructions
    st.write("**Enter your password to check its strength.**")

    # Password input field
    password = st.text_input("Password:", type="password", key="password_input")

    # Check password strength when input is provided
    if password:
        strength = check_password_strength(password)
        st.write(f"Password Strength: {strength}/5")
        
        # Progress bar for password strength
        st.progress(strength / 5)
        
        if strength == 5:
            st.success("✅ Strong Password! Good job!")
        elif strength >= 3:
            st.warning("⚠️ Moderate Password. Consider improving it.")
        else:
            st.error("❌ Weak Password. Please choose a stronger one.")
        
        st.write("**Tips for a strong password:**")
        st.write("- Use at least 8 characters.")
        st.write("- Mix uppercase and lowercase letters.")
        st.write("- Include numbers and special characters (!@#$%^&*).")

    # Reset Your Password section
    st.write("---")  # Separator
    st.write("**Reset Your Password**")
    email = st.text_input("Enter your email to reset your password:", key="email_input")
    new_password = st.text_input("Enter a new password:", type="password", key="new_password_input")
    
    if email and new_password:
        st.success(f"Password reset instructions have been sent to {email}.")
        st.write(f"Your new password has been set to: `{new_password}`")

        # Check the strength of the new password
        new_strength = check_password_strength(new_password)
        st.write(f"New Password Strength: {new_strength}/5")
        
        # Progress bar for new password strength
        st.progress(new_strength / 5)
        
        if new_strength == 5:
            st.success("✅ Your new password is strong! Good job!")
        elif new_strength >= 3:
            st.warning("⚠️ Your new password is moderate. Consider improving it.")
        else:
            st.error("❌ Your new password is weak. Please choose a stronger one.")

# Run the app
if __name__ == "__main__":
    main()