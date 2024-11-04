import streamlit as st


st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 10px;
                    padding-left: 10px;
                    padding-right: 10px;
                }


        </style>,<h1 style='display:inline-block;text-align: center; background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);-webkit-background-clip: text;color: transparent; '>Project 16 - Kaprekar Checker</h1>
        """, unsafe_allow_html=True)

st.write("A Kaprekar number is a number whose square when divided into two parts and such that sum of parts is equal to the original number and none of the parts has value 0.")

st.markdown("###### Enter any number and it will check it is a Kaprekar number")

def chk_is_int(number):
    try:
        # Attempt to convert to an integer
        int_value = int(number)
        return "int"
    except ValueError:
        try:
            # Attempt to convert to a float
            float_value = float(number)
            return "notint-float"
        except ValueError:
            return "notint"


def check_kaprekar(number):
    numsquare = int(number) * int(number)
    st.write(f"{number} x {number} = {numsquare}")
    strnumsquare = str(numsquare)
    if int(number) == 1:
        return "yes"
    elif int(number) == 0 or int(number) == 2 or int(number) == 3:
        return "no"
    else:
        if len(strnumsquare) % 2 == 1:
            middle_index = int((len(strnumsquare) / 2) + 0.5)
            firsthalf = int(strnumsquare[0:middle_index:1])
            lasthalf = int(strnumsquare[middle_index::1])

            if lasthalf == 0:
                st.write("last half is 0")
                return "no"

            st.write(f"{firsthalf} + {lasthalf} = {firsthalf + lasthalf}")

            if firsthalf + lasthalf == int(number):

                return "yes"
            else:
                middle_index = int((len(strnumsquare) / 2) - 0.5)
                firsthalf = int(strnumsquare[0:middle_index:1])
                lasthalf = int(strnumsquare[middle_index::1])
                if lasthalf == 0:
                    st.write("last half is 0")
                    return "no"

                st.write(f"{firsthalf} + {lasthalf} = {firsthalf + lasthalf}")

                if firsthalf + lasthalf == int(number):
                    return "yes"
                else:
                    return "no"
        else:

            firsthalf = int(strnumsquare[0:int(len(strnumsquare) / 2):1])
            lasthalf = int(strnumsquare[int(len(strnumsquare) / 2)::1])
            if lasthalf == 0:
                st.write("last half is 0")
                return "no"

            st.write(f"{firsthalf} + {lasthalf} = {firsthalf + lasthalf}")

            if firsthalf + lasthalf == int(number):
                return "yes"
            else:
                return "no"


num = st.text_input("Enter your number below:", value=0, key=int)

if chk_is_int(num) == "notint-float":
    st.error("Enter a number without decimal points")
elif chk_is_int(num) == "notint":
    st.error("Please enter a number")
else:
    output = check_kaprekar(num)

    if output == "no":
        st.write("Your number was not a Kaprekar Number.")
    else:
        st.success(f"{num} is a Kaprekar Number!")