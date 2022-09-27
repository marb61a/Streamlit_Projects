# Core packages
import streamlit as st

# Working with widgets
# Includes buttons, radio buttons, checkboxes and selects
name = "Martin"
if st.button("Submit"):
    st.write("Name: {}".format(name.upper()))

# Removes error from using button with the same values
if st.button("Submit", key='new02'):
    st.write("Name: {}".format(name.lower()))

# Radio buttons
status = st.radio("What is your status", ("Active", "Inactive"))
if status == "Active":
    st.success("You are active")
else:
    st.warning("You are inactive")

# Checkboxes
if st.checkbox("Show/Hide"):
    st.text("Showing Info")

# Beta Expander
with st.expander("Python"):
    st.success("Hello Python")