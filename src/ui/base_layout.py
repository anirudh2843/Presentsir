import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>

        /* Main Background */
        .stApp {
           background: linear-gradient(
    135deg,
    #FFF8E7,
    #FFE5B4,
    #FFD8A8
);
        }

        /* Remove default Streamlit spacing */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        /* Column Cards */
        div[data-testid="stColumn"] {
            background: rgba(255,255,255,0.85);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.5);
            border-radius: 24px;
            padding: 2rem !important;
            box-shadow: 0 8px 32px rgba(0,0,0,0.08);
        }

       h1 {
    color: #1E293B !important;
}

h2, h3 {
    color: #475569 !important;
}

        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>

                .stApp {
                    background: linear-gradient(
    135deg,
    #FFF8E7,
    #FFE5B4,
    #FFD8A8
);
                }

        </style>  

                """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    # asdasd
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Outfit', sans-serif !important;
                font-size: 4rem !important;
                font-weight: 800 !important;
                line-height: 1 !important;
                letter-spacing: -3px !important;
                margin-bottom: 0.5rem !important;
                color: #C2410C !important;
            }
                

            h2 {
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #C2410C !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """,
        unsafe_allow_html=True,
    )
