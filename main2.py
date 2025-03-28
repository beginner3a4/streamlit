import streamlit as st
import numpy as np
import easyocr as ocr
from PIL import Image

reader=ocr.Reader(["en"],gpu=False)

st.title("ocr project")
image_uploaded=st.file_uploader("upload an image",type=["png","jpg","jpeg"])
if image_uploaded:
    img=Image.open(image_uploaded)
    st.image(img ,caption="uploaded")
    img_array=np.array(img)
    result=reader.readtext(img_array)
    for text in result:
        st.write(f"# {text[1]}")



