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

# Function for Sumy Summarization
def sumy_summarizer(docx, num=2):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, num)
    summary_list = [str(sentence) for sentence in summary]
    result = ''.join(summary_list)
    return result

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
            c1, c2 = st.beta_columns(2)
            with c1:
                with st.beta_expander("LexRank Summary"):
                    my_summary = sumy_summarizer(raw_text)
                    st.write(my_summary)
                    
            with c2:
                with st.beta_expander("TextRank Summary"):
                    my_summary = summarize(raw_text)
                    st.write(my_summary)    
            
    else:
        st.subheader("About")

if __name__ == '__main__':
    main()
