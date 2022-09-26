# Core packages
import streamlit as st

# Additional packages
import pandas as pd

# Display data
df = pd.read_csv("./diabetes_data_upload.csv")

# Show entire dataframe
st.dataframe(df, 200)

# Add a color style from pandas
st.dataframe(df.style.highlight_max(axis=0))

# Static Table
# st.table(df)

# Using superfunction st.write
st.write(df.head())

# Display Json
st.json({'data':'name'})
