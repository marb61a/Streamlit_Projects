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

            with st.beta_expander("Text Analysis"):
                st.write(raw_text)
            
            with st.beta_expander("Entities"):
                st.write(raw_text)
            
            # Layouts
            col1,col2 = st.beta_columns(2)
            with col1:
                with st.beta_expander("World Stats"):
                    pass
                with st.beta_expander("Top Keywords"):
                    pass
                with st.beta_expander("Sentiment"):
                    pass
            
            with col2:
                with st.beta_expander("Plot Word Freq"):
                    pass
                with st.beta_expander("Plot Part of Speech"):
                    pass
                with st.beta_expander("Plot Wordcloud"):
                    pass
            
            with st.beta_expander("Download Text Analysis Results"):
                pass

    elif choice == "NLP(files)":
        st.subheader("NLP Task")
    else:
        st.subheader("About")

if __name__ == "__main__":
    main()