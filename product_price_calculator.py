import streamlit as st
import json

# Set up title
st.title("Product Price Calculator Bot")

# Load product prices from JSON
with open("products.json", "r") as file:
    data = json.load(file) #reads the content and converts into python dictionary

product_list = list(data["products"].keys()) #takes the keys of the dictionary and stores as list type

# User selects product and quantity
selected_product = st.selectbox("Choose a product:", product_list)
quantity = st.number_input("Enter quantity:", min_value=0, step=1)

# Calculate total price
if st.button("Calculate Price"):
    unit_price = data["products"][selected_product]
    total_price = unit_price * quantity

    st.markdown(f"**Bill:**")
    st.write(f"Product: {selected_product}")
    st.write(f"Unit Price: {unit_price}")
    st.write(f"Quantity: {quantity}")
    st.success(f"Total Price: {total_price}")