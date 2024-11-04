import streamlit as st


st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 10px;
                    padding-left: 10px;
                    padding-right: 10px;
                }


        </style>,<h1 style='display:inline-block;text-align: center; background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);-webkit-background-clip: text;color: transparent; '>Project 10 - Number to Name converter</h1>
        """, unsafe_allow_html=True)

# container1 = st.container(border=True)
# container1.write("This is inside the container 1")
# container1.write("This is inside too")

st.markdown("###### Give any number from 1 to 1,000,000 and it will convert this to text")


names = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000000: "one million"
}



#num = int(input("Enter a number between 0 and 1 million:\n"))
num = st.text_input ("Enter your number below:",value=0, key=int)



def two_digit(num):
    strnum = str(num)
    if num in names:
        return (names[num])
    else:
        return names[int(strnum[-2] + "0")] + " " + names[int(strnum[-1])]


def three_digit(num):
    strnum = str(num)
    if strnum[-2::1] == "00":
        return names[int(strnum[-3])] + " hundred"
    else:
        if int(strnum[-3]) == 0:
            return names[int(strnum[-3])] + "and " + two_digit(int(strnum[-2::1]))
        else:
            return names[int(strnum[-3])] + " hundred and " + two_digit(int(strnum[-2::1]))

def four_digit(num):
    strnum = str(num)
    last3 = strnum[-3::1]
    if last3 == "000":
        return names[int(strnum[-4])] + " thousand"
    elif len(str(int(last3))) == 3:
        return names[int(strnum[-4])] + " thousand, " + three_digit(int(last3))
    else:
        return names[int(strnum[-4])] + " thousand and " + two_digit(int(last3))

def five_digit(num):
    strnum = str(num)
    last3 = strnum[-3::1]
    first2 = strnum[-5:-3:1]
    if last3 == "000":
        return two_digit(int(first2)) + " thousand"
    elif len(str(int(last3))) == 3:
        return two_digit(int(first2)) + " thousand, " + three_digit(int(last3))
    else:
        return two_digit(int(first2)) + " thousand and " + two_digit(int(last3))

def six_digit(num):
    strnum = str(num)
    last3 = strnum[-3::1]
    first3 = strnum[-6:-3:1]
    if last3 == "000":
        return three_digit(int(first3)) + " thousand"
    elif len(str(int(last3))) == 3:
        return three_digit(int(first3)) + " thousand, " + three_digit(int(last3))
    else:
        return three_digit(int(first3)) + " thousand and " + two_digit(int(last3))

def number_to_names(num=0):
    if num == "0":
        return "zero"
    elif num in names:
        return names[num]
    else:
        strnum = str(num)
        if len(strnum) == 2:
            return two_digit(num)
        elif len(strnum) == 3:
            return three_digit(num)
        elif len(strnum) == 4:
            return four_digit(num)
        elif len(strnum) == 5:
            return five_digit(num)
        elif len(strnum) == 6:
            return six_digit(num)
        else:
            return "Number out of range."

#number_to_names(num)

#st


try:
    # Attempt to convert to an integer
    int_value = int(num)
    output = number_to_names(num)
    if output == "Number out of range.":
        st.error("Number out of range.")
    else:
        st.success(output)
except ValueError:
    try:
        # Attempt to convert to a float
        float_value = float(num)
        st.error("Enter a number without decimal points")
    except ValueError:

        st.error("Please enter a number")




