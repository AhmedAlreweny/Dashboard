import streamlit as st
import random

def seeded_random(date_str):
    random.seed(date_str)
    return random.randint(0, 9999)

def format_code(code):
    return str(code).zfill(4)

def main():
    st.set_page_config(page_title="Date-Based Code Generator", page_icon="📅")
    st.title("📅 Date-Based 4-Digit Code Generator")

    date_input = st.text_input("Enter a date (ddmmyyyy):", max_chars=8)

    if st.button("Generate Code"):
        if len(date_input) != 8 or not date_input.isdigit():
            st.error("Please enter a valid date in ddmmyyyy format.")
        else:
            code = seeded_random(date_input)
            formatted_code = format_code(code)
            st.success(f"Generated Code: **{formatted_code}**")

if __name__ == "__main__":
    main()
