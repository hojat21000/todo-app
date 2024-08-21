import streamlit as st
from PIL import Image

with st.expander("start Camera"):

    camera_image=st.camera_input("Camera")

if camera_image:
    img=Image.open(camera_image)

    gray_img=img.convert("P")

    st.image(gray_img)