import streamlit as st
from LangChainHelper import generate_rest_name_and_items

st.title("Restaurant Name Generator 👩🏻‍🍳")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Filipino", "Korean", "Japanese", "Italian", "American", "Mexican"))


if cuisine:
  response = generate_rest_name_and_items(cuisine)
  st.header(response['restaurant_name'].strip())
  menu_items = response['menu_items'].strip().split(",")
  st.write("🍴 Menu Items 🍴")
  for item in menu_items:
    st.write("-",item)