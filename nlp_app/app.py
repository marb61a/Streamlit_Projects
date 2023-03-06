# Core Package
import streamlit as st
import streamlit.components.v1 as stc

# Additional Packages
# Import EDA packages
import pandas as pd

# Import NLP Packages
import spacy
nlp = spacy.load('en')
from spacy import displacy
from spacy import tokens

from textblob import TextBlob

# Import Text Cleaning Packages
import neattext as nt
import neattext.functions as nfx

# Import utilities
from collections import Counter
import base64
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

# Import Data Visualization Packages
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

# Import Wordcloud
from wordcloud import WordCloud

# File Processing Packages
import docx2txt
import pdfplumber
from PyPDF2 import PdfFileReader

# Functions
def text_analyzer(my_text):
    docx = nlp(my_text)

    allData = [(tokens.text, tokens.shape, tokens.tag, tokens.lemma, tokens.is_alpha, tokens.is_stopword)]
    df = pd.DataFrame(allData, columns=['Token', 'Shape', 'PoS', 'Tag', 'Lemma', 'IsAlpha', 'Is_Stopword'])

    return df

def get_entities(my_text):
    docx = nlp(my_text)
    entities = [(entity.text, entity.label) for entity in docx.ents]

    return entities

HTML_WRAPPER = """
    <div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 1px; padding: 1rem"></div>
"""

def render_entities(rawtext):
    docx = nlp(rawtext)
    html = displacy.render(docx, style="ent") 
    html = html.replace("\n\n", "\n")
    result = HTML_WRAPPER.format(html)

    return result

# Get the most common tokens
def get_most_common_tokens(my_text, num=5):
    word_tokens = Counter(my_text.split())
    most_common_tokens = word_tokens.most_common(num)

    return most_common_tokens

# Get the sentiment
def get_sentiment(my_text):
    blob = TextBlob(my_text)
    sentiment = blob.sentiment

    return sentiment

# Generate wordcloud
def plot_wordcloud(my_text):
    my_wordcloud = WordCloud().generate(my_text)
    fig = plt.figure()
    plt.imshow(my_wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(fig)

# Download results as a file
def make_downloadable(data):
    csvfile = data.to_csv(index=False)
    b64 = base64.b64encode(csvfile.encode()).decode()
    new_filename = 'nlp_result_{}_.csv'.format(timestr)
    st.markdown('Download CSV file')
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click here!</a>'
    st.markdown(href, unsafe_allow_html=True)

# Read PDF functions
def read_pdf(file):
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_page_text = ""

    for i in range(count):
        page = pdfReader.getPage(i)
        all_page_text += page.extractText()
    
    return all_page_text

def read_pdf2(file):
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        return page.extract_text()

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
                token_result_df = text_analyzer(raw_text)
                st.dataframe(token_result_df)
            
            with st.expander("Entities"):
                entity_result = render_entities(raw_text)
                stc.html(entity_result, height=1000,scrolling=True) 
            
            # Layouts
            # columns has moved out of beta
            col1,col2 = st.columns(2)
            with col1:
                with st.expander("Word Stats"):
                    st.info("Word Statistics")
                    docx = nt.TextFrame(raw_text)
                    st.write(docx.word_stats())

                with st.expander("Top Keywords"):
                    st.info("Top Keywords/Tokens")
                    processed_text = nfx.remove_stopwords(raw_text)
                    keywords = get_most_common_tokens(processed_text, num_of_most_common)
                    st.write(keywords)

                with st.expander("Sentiment"):
                    sent_result = get_sentiment(raw_text)
                    st.write(sent_result)
            
            with col2:
                with st.expander("Plot Word Freq"):
                    fig = plt.figure()
                    top_keywords = get_most_common_tokens(processed_text, num_of_most_common)
                    plt.bar(keywords.keys(), top_keywords.values())
                    # Rotates the x-axis valus to help with displaying
                    plt.xticks(rotation=45)
                    st.pyplot(fig)

                with st.expander("Plot Part of Speech"):
                    fig = plt.figure()
                    sns.countplot(token_result_df['PoS'])
                    # Rotates the x-axis valus to help with displaying
                    plt.xticks(rotation=45)
                    st.pyplot(fig)

                with st.expander("Plot Wordcloud"):
                    plot_wordcloud(raw_text)
            
            with st.expander("Download Text Analysis Results"):
                make_downloadable(token_result_df)

    elif choice == "NLP(files)":
        st.subheader("NLP Task")

        # Add file uploader and the type of files that can be uploaded
        text_file = st.file_uploader("Upload Files", type=['pdf', 'docx', 'txt'])
        if text_file is not None:
            if text_file.type == 'application/pdf':
                raw_text = read_pdf(text_file)
                # st.write(raw_text)
            elif text_file.type == 'text/plain':
                raw_text = str(text_file.read(), 'utf-8')
                # st.write(raw_text)
            else:
                raw_text = docx2txt.process(text_file)
                st.write(raw_text)

                # beta_expander has moved out of beta so becomes expander
                with st.expander("Original Text"):
                    st.write(raw_text)

                with st.expander("Text Analysis"):
                    token_result_df = text_analyzer(raw_text)
                    st.dataframe(token_result_df)
                
                with st.expander("Entities"):
                    entity_result = render_entities(raw_text)
                    stc.html(entity_result, height=1000,scrolling=True) 
                
                # Layouts
                # columns has moved out of beta
                col1,col2 = st.columns(2)
                with col1:
                    with st.expander("World Stats"):
                        st.info("Word Statistics")
                        docx = nt.TextFrame(raw_text)
                        st.write(docx.word_stats())

                    with st.expander("Top Keywords"):
                        st.info("Top Keywords/Tokens")
                        processed_text = nfx.remove_stopwords(raw_text)
                        keywords = get_most_common_tokens(processed_text, num_of_most_common)
                        st.write(keywords)

                    with st.expander("Sentiment"):
                        sent_result = get_sentiment(raw_text)
                        st.write(sent_result)
                
                with col2:
                    with st.expander("Plot Word Freq"):
                        fig = plt.figure()
                        top_keywords = get_most_common_tokens(processed_text, num_of_most_common)
                        plt.bar(keywords.keys(), top_keywords.values())
                        # Rotates the x-axis valus to help with displaying
                        plt.xticks(rotation=45)
                        st.pyplot(fig)

                    with st.expander("Plot Part of Speech"):
                        fig = plt.figure()
                        sns.countplot(token_result_df['PoS'])
                        # Rotates the x-axis valus to help with displaying
                        plt.xticks(rotation=45)
                        st.pyplot(fig)

                    with st.expander("Plot Wordcloud"):
                        plot_wordcloud(raw_text)
                
                with st.expander("Download Text Analysis Results"):
                    make_downloadable(token_result_df)

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()