from typing import no_type_check
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import cv2
from PIL import Image, ImageEnhance
import pandas as pd

from transformations import Transformation
from image import LoadedImage

def main():    
    # START
    
    if "transformations_pipeline" not in st.session_state:
        st.session_state["transformations_pipeline"] = []
    transformation = Transformation()
    selected_transformation = st.sidebar.selectbox("Select operation:", 
                                           transformation.transformations) 
    
    # UPLOAD IMAGE
    im = LoadedImage()
    
    st.subheader("")
    image_file = st.file_uploader("Upload de imagem", type=['jpg', 'png', 'jpeg'])
    
    if image_file is not None:
        image = im.load_img(image_file)
        st.image(image)

    st.title("PDI Toolbox")
    st.header("Um WebApp para processamento digital de imagens.")

    # CHOOSE TRANSFORMATIONS
    if selected_transformation=="Conversão de cor":
        op = st.radio("Selecione o espaço de cores da imagem:", 
                      transformation.transformations[selected_transformation])
    
    elif selected_transformation=="Filtro":
        op = st.radio("Selecione o filtro:", 
                      transformation.transformations[selected_transformation])

    elif selected_transformation=="Detector de borda":
        op = st.radio("Selecione o detector de borda:", 
                      transformation.transformations[selected_transformation])
        
    elif selected_transformation=="Binarização":
        op = st.radio("Selecione o filtro:", 
                      transformation.transformations[selected_transformation])
        
    elif selected_transformation=="Morfologia matemática":
        op = st.radio("Selecione o filtro:", 
                      transformation.transformations[selected_transformation])
    
    # ADD/DEL TRANSFORMATIONS TO/FROM THE PIPELINE
    add    = st.button("Adicionar ao pipeline",        key="add")
    delete = st.button("Remover última transformação", key="del")
    
    if delete:
        remove_last_from_pipeline(st.session_state.transformations_pipeline)
    elif add:
        append_to_pipeline(st.session_state.transformations_pipeline, 
                           selected_transformation, 
                           op)
        
    with st.empty():
        st.write(pd.DataFrame(st.session_state["transformations_pipeline"], 
                              columns=["Transformation class", "Transformation"]))
    
    
    # APPLY
    if image_file is not None:
        transform = st.button("Transformar")
        
        if transform:
            im = transformation.run(im, 
                                    st.session_state.transformations_pipeline)
            st.image(im.image)
        

# Add/Del from pipeline
def append_to_pipeline(transformations_pipeline, 
                       transformation_class, 
                       transformation):
    transformations_pipeline.append((transformation_class, 
                                     transformation))
    
def remove_last_from_pipeline(transformations_pipeline):
    transformations_pipeline.pop()

if __name__ == "__main__":
    main()
