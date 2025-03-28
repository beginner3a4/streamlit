import streamlit as st
import easyocr
import numpy as np
from PIL import Image

# Cache the EasyOCR reader to avoid reloading
@st.cache_resource
def load_reader():
    return easyocr.Reader(['en'], gpu=False)

reader = load_reader()

st.title("OCR App Using NumPy")
uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

   
    img_array = np.array(image)

  
    results = reader.readtext(img_array)

   
    st.subheader("Extracted Text:")
    for  text in results:
        st.write(f"- {text}")
