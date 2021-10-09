import wx

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


def run_model(filename) -> bool:
    if filename[-4:].lower() == ".jpg":
        print_result(model_2d(filename))
    elif filename[-4:].lower() == ".nii":
        print_result(model_3d(filename))
    else:
        st.error('Model error.')

    return True


def load_file():
    filename = get_path("(*.nii)|*.nii | (*.jpg)|*.jpg")
    try:
        with open(filename):
            st.text("File opened. Running model")
            has_tumor = run_model(filename)
            if has_tumor:
                st.text("Tumor Positive")
            else:
                st.text("Tumor Negative")
    except FileNotFoundError:
        st.error('File not found.')


def print_result(response):
    print("Tumor Positive" if response else "Tumor Negative")


def main():
    st.title("MRI Brain Tumor Detection")
    st.write("An app made in **Python** with **Jupyter**")
    st.button("Open File Explorer", on_click=load_file)


if __name__ == '__main__':
    main()
