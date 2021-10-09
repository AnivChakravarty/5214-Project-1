import wx
import os

import streamlit as st

from v2.model_train.model_prod import load_model as model_2d
from v1.model_train.model_prod import load_model as model_3d


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


def run_model(filename):
    st.text(os.getcwd())
    if filename.lower().endswith("jpg"):
        print_result(model_2d(filename))
    elif filename.lower().endswith("nii.gz"):
        print_result(model_3d(filename))
    else:
        st.error('Wrong file extension.')


def load_file():
    filename = get_path("(*.gz)|*.gz | (*.jpg)|*.jpg")
    try:
        with open(filename):
            st.text("File opened. Running model")
            run_model(filename)
    except FileNotFoundError:
        st.error('File not found.')


def print_result(response):
    st.text("Tumor Positive" if response else "Tumor Negative")


def main():
    st.title("MRI Brain Tumor Detection")
    st.write("An app made in **Python** with **Jupyter**")
    st.button("Open File Explorer", on_click=load_file)


if __name__ == '__main__':
    main()
