# Core Package
import streamlit as st

# Additional Packages
# Import EDA packages
import pandas as pd

# Import NLP Packages
import spacy
nlp = spacy.load('en')

# Import Text Cleaning Packages
import neattext as nt
import neattext.functions as nfx

# Functions
def text_analyzer(my_text):
    docx = nlp(my_text)

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
            # beta_expander has moved out of beta so becomes expander
            with st.expander("Original Text"):
                st.write(raw_text)

            with st.expander("Text Analysis"):
                st.write(raw_text)
            
            with st.expander("Entities"):
                st.write(raw_text)
            
            # Layouts
            # columns has moved out of beta
            col1,col2 = st.columns(2)
            with col1:
                with st.expander("World Stats"):
                    pass
                with st.expander("Top Keywords"):
                    pass
                with st.expander("Sentiment"):
                    pass
            
            with col2:
                with st.expander("Plot Word Freq"):
                    pass
                with st.expander("Plot Part of Speech"):
                    pass
                with st.expander("Plot Wordcloud"):
                    pass
            
            with st.expander("Download Text Analysis Results"):
                pass

    elif choice == "NLP(files)":
        st.subheader("NLP Task")
    else:
        st.subheader("About")

if __name__ == "__main__":
    main()