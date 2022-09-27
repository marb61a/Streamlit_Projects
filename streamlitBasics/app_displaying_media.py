# Core packages
import streamlit as st

# Work with media files such as images, video etc
from PIL import Image
img = Image.open("./ignore.jpg")
# Displayes image using full width
st.image(img, use_column_width=True)

# Import image from url
st.image("https://www.simplilearn.com/ice9/free_resources_article_thumb/Why-get-certified-in-Artificial-Intelligence.jpg")

# Display videos
# video_file = open("", "rb").read()
# st.video(video_file)

# Display audio
audio_file = open("", "rb")
st.audio(audio_file.read(), format="audio/mp3")
