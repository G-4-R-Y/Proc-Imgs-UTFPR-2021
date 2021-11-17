from typing import no_type_check
import streamlit as st
import cv2
from PIL import Image, ImageEnhance

def load_img(img):
    im = Image.open(img)
    return im

def main():
    st.title("PDI Toolbox")
    st.header("Um WebApp para processamento digital de imagens.")
    
    activities = ["Conversão de cor", 
                  "Filtro", 
                  "Detector de borda", 
                  "Binarização", 
                  "Morfologia Matemática"]
    
    choice    = st.sidebar.selectbox("Select operation:", activities) 
    
    st.subheader("")
    st.subheader("Enviar imagem:")
    image_file = st.file_uploader("", type=['jpg', 'png', 'jpeg'])



if __name__ == "__main__":
    main()
