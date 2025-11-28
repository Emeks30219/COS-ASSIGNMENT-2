import streamlit as st

# page setup

st.title("Simple Arithmetic calculator")
st.write("Enter two numbers and choose an operation")
#input number section
num1= st.number_input("Enter first number", value=0.0)
num2= st.number_input("Enter second number",value=0.0)

operation=  st.selectbox("choose operation", [
"OPT_ADD",
"OPT_SUB",
"OPT_MUL",
"OPT_DIV"
])

#Functions
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return None
    return a/b

if st.button("Calculate"):
    result= None
    symbol = ""

    if operation=="OPT_ADD":
        result= add(num1, num2)
        symbol="+"
    elif operation=="OPT_SUB":
        result= subtract(num1, num2)
        symbol="-"
    elif operation=="OPT_MUL":
        result= multiply(num1, num2)
        symbol="*"
    elif operation=="OPT_DIV":
        symbol="/"
        if num2==0:
            st.error("Cant divide by ZERO!")
        else:
         result=divide(num1,num2)

    if result is not None:
         st.write(f"Result: {num1} {symbol} {num2} = {result}")
