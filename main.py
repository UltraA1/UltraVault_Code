import streamlit as st


#----- PAGE SETUP
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",

)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 10px;
                    padding-left: 10px;
                    padding-right: 10px;
                }


        </style>,
        """, unsafe_allow_html=True)

#st.sidebar.page_link("main.py", label="ABOUT accounts")
#st.sidebar.page_link("pages\A_10_Number_Names.py", label="Number Names")
#st.sidebar.page_link("pages\A_13_Caesar_Cipher.py", label="Caesar_Cipher")
#st.sidebar.page_link("pages\A_16_Kaprekar_Number.py", label="Kaprekar_Number")




pages = {
    "Your account": [
        st.Page("home_page.py", title="ABOUT accounts")
    ],
    "GCSE Challenges": [
        st.Page("pages\A_10_Number_Names.py", title="Number_Names"),
        st.Page("pages\A_13_Caesar_Cipher.py", title="Caesar_Cipher"),
        st.Page("pages\A_16_Kaprekar_Number.py", title="Kaprekar_Number"),
    ],
}

pg = st.navigation(pages)
pg.run()

