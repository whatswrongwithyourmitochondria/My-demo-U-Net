"""Creating a streamlit web app to upload images"""
import streamlit as st  # pylint: disable=import-error
from PIL import Image  # pylint: disable=import-error
import numpy as np  # pylint: disable=import-error
from demo import demo_main

st.title("Demo Web APP")
st.write("Check")


def main():
    """main function to upload an image"""
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        result = demo_main(image_file=img_array, show=False)
        st.image(result, caption="")


if __name__ == "__main__":
    main()
