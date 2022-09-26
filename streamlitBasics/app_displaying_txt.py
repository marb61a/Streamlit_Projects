# Core packages
import streamlit as st

# Additional packages

# Functions
def main():
    # All code goes here
    # pass
    # Show title
    st.title("Hi streamlit")

    # Show text
    st.text("Today is Monday")
    st.text("This is cool")

    # Header
    st.header("This is a header")

    # Subheader
    st.subheader("This is a subheader")

    # Markdown
    st.markdown("This is markdown")

    # Display colored text
    st.success("Successful")
    st.warning("Danger")
    st.info("Information")
    st.error("Error")
    st.exception("Exception")

    # Superfunction
    st.write("## This is text")
    st.write(1+2)

    st.write(dir(st))

    # Help info
    st.help(range)


if __name__ == '__main__':
    main()