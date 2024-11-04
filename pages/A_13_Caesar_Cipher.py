import streamlit as st
import re
import string


st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 10px;
                    padding-left: 10px;
                    padding-right: 10px;
                }


        </style>,<h1 style='display:inline-block;text-align: center; background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);-webkit-background-clip: text;color: transparent; '>Project 13 - Caesar Cipher</h1>
        """, unsafe_allow_html=True)

ACTION = st.radio(
    "Select to ENCODE or DECODE",
    [":red[ENCODE]", ":green[DECODE]"],
)



key = st.slider("Select how many steps you want the encryption to jump in (the key).", min_value=0, max_value=26, value=0, step=1, key=int)
text = st.text_area("Enter some text to be encoded:", value="", key=str)


if ACTION == ":red[ENCODE]":
    key
elif ACTION == ":green[DECODE]":
    key = 26-key


def check_for_nums(string):
    if re.search(r'\d', string):
        return "disallow"
    else:
        return "allow"

def cipher(letter, key):
    if letter.isspace():
        return " "
    elif letter in string.punctuation:
        return letter
    else:
        if letter.isupper():
            max_ord = 90
        else:
            max_ord = 122

        if ord(letter) + key <= max_ord:
            return chr(ord(letter) + key)
        else:
            return chr(ord(letter) - (26 - key))


if check_for_nums(text) == "disallow":
    st.error("Please avoid using number")
else:
    encoded_text_lst = [cipher(letter, key) for letter in text]
    st.success("".join(encoded_text_lst))