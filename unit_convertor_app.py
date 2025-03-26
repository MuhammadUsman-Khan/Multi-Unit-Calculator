import streamlit as st

st.set_page_config(page_title="Multi-Unit Convertor", layout="centered")
st.title("Multi-Unit Convertor")

option = st.sidebar.selectbox("Choose Category", ["Length Conversion", "Mass Conversion", "Temperature Conversion", "Time Conversion"])

if option == "Length Conversion":
    length_units = ["Centimeters", "Kilometers", "Meters", "Inches", "Miles"]
    st.subheader("Length Conversion")
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("Convert From", length_units)
    to_unit = st.selectbox("Convert To", length_units)

    if st.button("Convert"):
        if from_unit == "Centimeters":
            if to_unit == "Kilometers":
                result = value / 100000

            elif to_unit == "Meters":
                result = value / 100

            elif to_unit == "Inches":
                result = value / 2.54

            elif to_unit == "Miles":
                result = value / 160900

            else:
                result = value
        
        if from_unit == "Kilometers":
            if to_unit == "Centimeters":
                result = value * 100000

            elif to_unit == "Meters":
                result = value * 1000

            elif to_unit == "Inches":
                result = value * 39370.0787

            elif to_unit == "Miles":
                result = value * 0.621371

            else:
                result = value

        if from_unit == "Meters":
            if to_unit == "Centimeters":
                result = value * 100

            elif to_unit == "Inches":
                result = value * 39.3700787

            elif to_unit == "Kilometers":
                result = value / 1000

            elif to_unit == "Miles":
                result = value / 1609.344

            else:
                result = value

        if from_unit == "Inches":
            if to_unit == "Centimeters":
                result = value * 2.54

            elif to_unit == "Meters":
                result = value / 39.3700787

            elif to_unit == "Kilometers":
                result = value / 39370.0787

            elif to_unit == "Miles":
                result = value / 63360

            else:
                result = value
   
        if from_unit == "Miles":
            if to_unit == "Centimeters":
                result = value * 160900

            elif to_unit == "Meters":
                result = value * 1609.344

            elif to_unit == "Kilometers":
                result = value * 1.609344

            elif to_unit == "Inches":
                result = value * 63360

            else:
                result = value

        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
       
if option == "Mass Conversion":
    mass_units = ["Grams", "Kilograms", "Ounce", "Pounds"]
    st.subheader("Mass Conversion")
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("Convert From", mass_units)
    to_unit = st.selectbox("Convert To", mass_units)

    if st.button("Convert"):
        if from_unit == "Grams":
            if to_unit == "Kilograms":
                result = value / 1000

            elif to_unit == "Ounce":
                result = value / 28.3495

            elif to_unit == "Pounds":
                result = value / 453.592

            else:
                result = value
        
        if from_unit == "Kilograms":
            if to_unit == "Grams":
                result = value * 1000

            elif to_unit == "Ounce":
                result = value * 35.274

            elif to_unit == "Pounds":
                result = value * 2.20462

            else:
                result = value
        
        if from_unit == "Ounce":
            if to_unit == "Grams":
                result = value * 28.3495

            elif to_unit == "Kilograms":
                result = value / 35.274

            elif to_unit == "Pounds":
                result = value / 16

            else:
                result = value
        
        if from_unit == "Pounds":
            if to_unit == "Grams":
                result = value * 453.592

            elif to_unit == "Kilograms":
                result = value / 2.20462

            elif to_unit == "Ounce":
                result = value * 16

            else:
                result = value
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

if option == "Temperature Conversion":
    temperature_units = ["Celcius", "Fahrenheit", "Kelvin"]
    st.subheader("Temperature Conversion")
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("Convert From", temperature_units)
    to_unit = st.selectbox("Convert To", temperature_units)

    if st.button("Convert"):
        if from_unit == "Celcius":
            if to_unit == "Fahrenheit":
                result = (value * 1.8) + 32 

            elif to_unit == "Kelvin":
                result = value + 273.15

            else:
                result = value
        
        if from_unit == "Fahrenheit":
            if to_unit == "Celcius":
                result = (value - 32) / 1.8 

            elif to_unit == "Kelvin":
                result = ((value - 32) / 1.8 ) + 273.15

            else:
                result = value
        
        if from_unit == "Kelvin":
            if to_unit == "Celcius":
                result = value - 273.15 

            elif to_unit == "Fahrenheit":
                result = ((value - 253.15) * 1.8) + 32

            else:
                result = value

        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")

if option == "Time Conversion":
    time_units = ["Seconds", "Minutes", "Hours", "Days"]
    st.subheader("Time Conversion")
    value = st.number_input("Enter value:", min_value=1.0, format="%.2f")
    from_unit = st.selectbox("Convert From", time_units)
    to_unit = st.selectbox("Convert To", time_units)

    if st.button("Convert"):
        if from_unit == "Seconds":
            if to_unit == "Minutes":
                result = value / 60

            elif to_unit == "Hours":
                result = value / 3600

            elif to_unit == "Days":
                result = value / 86400

            else:
                result = value
        
        if from_unit == "Minutes":
            if to_unit == "Seconds":
                result = value * 60

            elif to_unit == "Hours":
                result = value / 60

            elif to_unit == "Days":
                result = value / 1440

            else:
                result = value
        
        if from_unit == "Hours":
            if to_unit == "Seconds":
                result = value * 3600

            elif to_unit == "Minutess":
                result = value * 60

            elif to_unit == "Days":
                result = value / 24

            else:
                result = value
       
        if from_unit == "Days":
            if to_unit == "Seconds":
                result = value * 86400

            elif to_unit == "Minutes":
                result = value * 1440

            elif to_unit == "Hours":
                result = value * 24

            else:
                result = value
                
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

st.markdown("---")
st.markdown("<h5 style='text-align: center;'>⚙️ Made by Muhammad Usman Khan ⚙️</h5>", unsafe_allow_html=True)