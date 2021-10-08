#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import streamlit as st
import sys
#import cnn_model

def run_model(file_path) -> bool:
    #place model function call here
    return True

def load_file(file_path):
    try:
        with open(file_path) as input:
            st.text(input.read())
            st.text("File opened. Running model")
            has_tumor = run_model(file_path)
            if has_tumor:
                st.text("Tumor Positive")
            else:
                st.text("Tumor Negative")
                
                
    except FileNotFoundError:
        st.error('File not found.')

st.title("MRI Brain Tumor Detection",anchor="test")
st.write("An app made in **Python** with **Jupyter**")
file_path = st.text_input('Enter file path to MRI Scans:')
st.button("Submit File", on_click = load_file(file_path))
#streamlit.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')




# %%




