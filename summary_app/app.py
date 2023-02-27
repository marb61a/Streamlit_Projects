# Core Package
import streamlit as st

# Any additional packages
# TextRank Algorithm
from gensim.summarization import summarize

# LexRank Algorithm
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# EDA Pakages
import pandas as pd

# data Visualisation
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use("Agg")

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

        if st.button("Summarise"):
            # st.write(raw_text)
            with st.beta_expander("Original Text"):
                st.write(raw_text)
            
            # Layout
            
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
