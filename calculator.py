import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0, step=1)
num2 = st.number_input("Enter the second number", value=0, step=1)

# Dropdown for selecting operation
operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform calculation based on selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result is: {result}")
        else:
            st.error("Division by zero is not allowed.")