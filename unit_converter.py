import streamlit as st
# icon change 
st.set_page_config(page_title="Unit Converter", page_icon="🔄")


# function to convert value with parameter and calculation
def conver_unit(value, unit_form, Unit_to):
    conversions = {
        "meters_kilometers":0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams":1000,    
    }
    
    key = f"{unit_form}_{Unit_to}" # generate a key based on the input and output units
    
    if key in conversions:
        conversion =  conversions[key]
        return value * conversion
    else:
        return "Conversion Not Supported"
#---------- function end here-------------


# unit converter layout
st.title("Unit Converter")

value  =st.number_input("Enter The value to Convert : ",min_value=1.0,step=1.0)

unit_from = st.selectbox("Convert from:" ,["Select an option","meters","kilometers","grams","kilograms"],index=0)
unit_to = st.selectbox("Convert to:" ,["Select an option","meters","kilometers","grams","kilograms"], index=0)

if st.button("Convert"):
    if unit_from == "Select an option" or unit_to == "Select an option":
        st.write("Please select valid units before converting.")
    result = conver_unit(value,unit_from,unit_to)
    # st.write(f"Converted Value : {result} ")
    st.markdown(
            f'<p style="background-color:#ff4d4d; color:black; font-weight:bold; padding:10px; border-radius:5px;">'
            f'Converted Value: {result} '
            f'</p>',
            unsafe_allow_html=True
        )