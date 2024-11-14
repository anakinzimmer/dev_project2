import streamlit as st
from Main import process_city_info  # Importing the function from Main.py

# Title for the web app
st.title("City Information Form")

# Input fields for the city, state, and area
city = st.text_input("Enter the City")
state = st.text_input("Enter the State")
area = st.number_input("Enter the Area (in KM)", min_value=0.0)

# Button to submit the form
if st.button("Submit"):
    if city and state and area > 0:
        # Call the function from Main.py and pass the inputs
        output_message = process_city_info(city, state, area)
        st.success(output_message)  # Display the result from Main.py
    else:
        st.error("Please fill in all the fields correctly.")
