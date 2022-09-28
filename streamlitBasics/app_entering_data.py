# Core packages
import streamlit as st

# Text input
fname = st.text_input("Enter Firstname", max_chars=10)
st.title(fname)

# Text area
message = st.text_area("Enter Message")
st.write(message)

# Number input
# Can be floating point numbers and can be added to so the
# number increases in set stages eg 5
number = st.number_input("Enter Number", 1, 25)

# Date Input
my_appointment = st.date_input("Appointment")

# Time Input
my_time = st.time_input("My Time")

# Color Picker
color = st.color_picker("Select color")
