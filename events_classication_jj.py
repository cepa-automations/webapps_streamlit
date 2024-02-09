# app.py
import streamlit as st

def main():
    st.title("My Streamlit App")
    st.write("This is a basic Streamlit app.")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

if __name__ == "__main__":
    main()
