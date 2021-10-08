#!/usr/bin/env python
# coding: utf-8
# %%

# %%

import streamlit as st
import sys
import easygui
import wx
#import cnn_model

def get_path(wildcard):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path


def run_model(filename) -> bool:
    # TODO: place model function call here
    offset = 4
    if filename[-4:].lower() == ".jpg":
        pass
    elif filename[-4:].lower() == ".nii":
        pass
    else:
        st.error('File not found.')
    
    
    return True

def load_file():

    filename = get_path("(*.nii)|*.nii | (*.jpg)|*.jpg")
    
    try:
        with open(filename) as input:
            st.text("File opened. Running model")
            has_tumor = run_model(filename)
            if has_tumor:
                st.text("Tumor Positive")
            else:
                st.text("Tumor Negative")

    except FileNotFoundError:
        st.error('File not found.')

def main():
    st.title("MRI Brain Tumor Detection")
    st.write("An app made in **Python** with **Jupyter**")
    st.button("Open File Explorer", on_click = load_file)

if __name__ == '__main__':
    main()


# %%
filename = "picture.jpg"
offset = 4
#if filename[len(filename-3):len(filename)] == "*.jpg":
if filename[-4:] == ".jpg":
    print("True")
else:
    print("False")
    print(filename[len(filename)-offset:len(filename)])
    



# %%
