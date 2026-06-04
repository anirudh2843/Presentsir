import streamlit as st


def header_home():
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image("assets/Logo.png", width=100)

    with col2:
        st.markdown(
            """
            <div style="display:flex; align-items:center; height:100px;">
                <h1 style="color:black; margin:0;">
                    Present Sir
                </h1>
            </div>
            """,
            unsafe_allow_html=True,
        )


def header_dashboard():
    st.image("assets/Logo.png", width=100)
