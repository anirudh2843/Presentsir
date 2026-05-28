import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from PIL import Image
import numpy as np


def student_screen():
    style_background_dashboard()
    style_base_layout()
    col1, col2 = st.columns(2, vertical_alignment="center", gap="xlarge")
    with col1:
        header_dashboard()
    with col2:
        if st.button(
            "Go Back to Home",
            type="secondary",
            key="loginbackbtn",
            shortcut="control+backspace",
        ):
            st.session_state["login_type"] = None
            st.rerun()

    st.space()
    st.space()

    st.header("Login Using Face Recognition", text_alignment="center")
    photo_source = st.camera_input("Look into the camera and click the button to login")

    if photo_source:
        np.array(Image.open(photo_source))

    footer_dashboard()
