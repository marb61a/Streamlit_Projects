# Core packages
import streamlit as st

# Configuring page, this must be the first activity of streamlit
# Emojis can also be added directly, some work however some may not
# Sidebars can also be added with different state for example some may want the 
# sidebar collapsed. There is also a second method which may be used to configure a page and
# that is to use a dictionary to pass in various options
st.set_page_config(page_title='hello', page_icon=':smiley:', Layout='wide', initial_sidebar_state='collapsed')

# Functions
def main():
    st.title("Hi streamlit")
    st.sidebar.success("Menu")

if __name__ == '__main__':
    main()