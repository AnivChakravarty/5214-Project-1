#!/usr/bin/env python
# coding: utf-8
# %%

# %%

#cd OneDrive\SchoolFiles\CSCE\Graduate\"CSCE 5214 - Software for AI"


import streamlit as st
import sys
#import cnn_model
#from tkinter import Tk     # from tkinter import Tk for Python 3.x
#import tkinter 
#import askopenfilename
import easygui
import wx

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
    #place model function call here
    return True

def load_file():

    #filename = tkinter.filedialog.askopenfilename() # show an "Open" dialog box and return the path to the selected file
    #filename = tkinter.filedialog.open() # show an "Open" dialog box and return the path to the selected file
    #filename = easygui.fileopenbox(default='OneDrive\SchoolFiles\CSCE\Graduate\"CSCE 5214 - Software for AI"')
    filename = get_path("(*.txt)|*.txt")
    
    try:
        with open(filename) as input:
            #st.text(input.read())
            st.text("File opened. Running model")

            has_tumor = run_model(filename)
            if has_tumor:
                st.text("Tumor Positive")
            else:
                st.text("Tumor Negative")

    except FileNotFoundError:
        st.error('File not found.')

def main():
    #Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    st.title("MRI Brain Tumor Detection")
    st.write("An app made in **Python** with **Jupyter**")
    #file_path = st.text_input('Enter file path to MRI Scans:')
    st.button("Open File Explorer", on_click = load_file)
    #streamlit.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

if __name__ == '__main__':
    main()


# %%

