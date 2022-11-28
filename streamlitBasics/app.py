# Core packages
import streamlit as st

# Load EDA packages
import pandas as pd
import numpy as np

# Load data visualisation packages
import plotly.express as px


# Functions
def main():
    st.title("Working with Plotly in Streamlit")
    df = pd.read_csv("./diabetes_data_upload.csv")
    st.dataframe(df)

if __name__ == '__main__':
    main()
