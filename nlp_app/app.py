# Core Package
import streamlit as st

# Additional Packages
def main():
    st.title("NLP Streamlit App")

    # Add menu items
    menu = ["Home", "NLP(files)", " About"]

    # Add sidebar
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home: Analyse Text")

        # Add a text area
        raw_text = st.text_area("Enter Text Here")
        st.write(raw_text)

        # Add sidebar selection for most common words (Tokens)
        num_of_most_common = st.sidebar.number_input("Most Common Tokens", 5, 15)

        # Add button under text area
        if st.button("Analyse"):
            with st.beta_expander("Original Text"):
                st.write(raw_text)
                
    elif choice == "NLP(files)":
        st.subheader("NLP Task")
    else:
        st.subheader("About")

if __name__ == "__main__":
    main()