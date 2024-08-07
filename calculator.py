import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Inputs for the two numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Selectbox for the operation
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

# Function to perform calculation
def calculate(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            return "Error! Division by zero."
        else:
            return num1 / num2

# Perform calculation and display result
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"Result: {result}")

# Optionally, provide a clear button
if st.button("Clear"):
    st.write("Enter new values for calculation.")
