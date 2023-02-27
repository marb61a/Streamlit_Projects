# Core Package
import streamlit as st

# Any additional packages

def main():
    # A simple summarisation app
    st.title("Summarising App")

    # Add menu options
    menu=["Home", "About"]
    #  Adds menu options to dropdown menu sde panel
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Summarisation")
        # Create an area to enter text
        raw_text = st.text_area("Enter Text Here")
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
