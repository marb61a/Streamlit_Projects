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

# Import Text Cleaning Packages
import neattext as nt
import neattext.functions as nfx

# Import utilities
from collections import Counter

# Functions
def text_analyzer(my_text):
    docx = nlp(my_text)

    allData = [(token.text, token.shape, token.tag, token.lemma, token.is_alpha, token.is_stopword)]
    df = pd.DataFrame(allData, columns=['Token', 'Shape', 'PoS', 'Tag', 'Lemma', 'IsAlpha', 'Is_Stopword'])

    return df

def get_entities(my_text):
    docx = nlp(my_text)
    entities = [(entity.text, entity.label) for entity in docx.ents]

    return entities

HTML_WRAPPER = """
    <div style="overflow-x: auto"; border: 1px solid #e6e9ef; border-radius: 1px;></div>
"""

def render_entities(rawtext):
    docx = nlp(rawtext)
    html = displacy.render(docx, style="ent") 
    html = html.replace("\n\n", "\n")
    result = HTML_WRAPPER.format(html)

    return result

# Get the most common tokens
def get_most_common_tokens(my_text, num=4):
    word_tokens = Counter(my_text.split(''))
    most_common_tokens = word_tokens.most_common(num)

    return most_common_tokens

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
                with st.expander("World Stats"):
                    st.info("Word Statistics")
                    docx = nt.TextFrame(raw_text)
                    st.write(docx.word_stats())
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