# Core packages
import streamlit as st

# Working with widgets
# Includes selects, sliders and multi sliders
# Select and multiple select
my_lang = ["Python", "JavaScript", "Java", "C#", "SQL"]
choice = st.selectbox("Language: ", my_lang)
st.write("You selected {}".format(choice))

# Multiple selection
my_lang_multi = ["Python", "JavaScript", "Java", "C#", "SQL"]
multi_choice = st.multiselect("Multiple languages ", my_lang_multi , default="JavaScript")

# Slider
# Numerical datatypes only
age = st.slider("Age", 1, 100)

# Select Slider
# Any datatype
color = st.select_slider("Choose Color", options=["Red", "Blue", "Green", "Yellow", "Black", "Purple"])