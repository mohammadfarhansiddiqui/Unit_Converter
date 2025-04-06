import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #d1cee0;
        color: black;
    }
    .stApp {
        background: linear-gradient(to right, #bcd1bc, #a1c4a1);
        color: black;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: black   
        } 
            
    .result-box {
        background-color: white;
        color: black;
        padding: 20px;
        border-radius: 10px;
        
    }
        
    .footer {
        text-align: center;
        margin-top: 20px;
        color: black;
    }
    
    .stButton > button {
        color: black;
        font-weight: bold;
        font-color: black;
        background-color: lightblue;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        transition: background-color 0.3s ease; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Unit Converter 🎰')

# Unit Convert types with emojis
conversion_types = ["Length 📏", "Weight ⚖️", "Temperature 🌡️"]
conversion_choice = st.selectbox("Select a conversion type", conversion_types)

input_value = st.number_input(f"Enter the value to be converted", min_value=0.0, format="%.2f")
from_unit = None
to_unit = None
result = None

if "Length" in conversion_choice:
    length_units = ["Meters", "Kilometers", "Centimeters", "Inches", "Feet"]
    from_unit = st.selectbox("From Units:", length_units)
    to_unit = st.selectbox("To Units:", length_units)
    length_conversions = {
        "meters": 1, "kilometers": 0.001, "centimeters": 100, "inches": 39.3701, "feet": 3.28084
    }
elif "Weight" in conversion_choice:
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_unit = st.selectbox("From Units:", weight_units)
    to_unit = st.selectbox("To Units:", weight_units)
    weight_conversions = {
        "kilograms": 1, "grams": 0.001, "pounds": 0.453592, "ounces": 0.0283495
    }
elif "Temperature" in conversion_choice:
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Units:", temperature_units)
    to_unit = st.selectbox("To Units:", temperature_units)

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return None

if st.button("Convert 🔄"): # Added an icon to the button
    if "Length" in conversion_choice and from_unit and to_unit:
        if from_unit == to_unit:
            st.info(f"The 'From' and 'To' units are the same. No conversion needed.")
        else:
            from_unit_lower = from_unit.lower()
            to_unit_lower = to_unit.lower()
            if from_unit_lower in length_conversions and to_unit_lower in length_conversions:
                result = input_value * length_conversions[from_unit_lower] / length_conversions[to_unit_lower]
            else:
                st.error("Invalid length units selected.")
    elif "Weight" in conversion_choice and from_unit and to_unit:
        if from_unit == to_unit:
            st.info(f"The 'From' and 'To' units are the same. No conversion needed.")
        else:
            from_unit_lower = from_unit.lower()
            to_unit_lower = to_unit.lower()
            if from_unit_lower in weight_conversions and to_unit_lower in weight_conversions:
                result = input_value * weight_conversions[from_unit_lower] / weight_conversions[to_unit_lower]
            else:
                st.error("Invalid weight units selected.")
    elif "Temperature" in conversion_choice and from_unit and to_unit:
        result = convert_temperature(input_value, from_unit, to_unit)
        if result is None:
            st.warning("No conversion needed or invalid temperature units.")
    else:
        st.warning("Please select a conversion type and units.")

if result is not None:
    st.success(f"✅ {input_value} {from_unit} is equal to {result:.2f} {to_unit}") # Added a success icon

st.markdown("<div class='footer'>Copyright © 2025 - Developed by M Farhan Siddiqui</footer>", unsafe_allow_html=True)
