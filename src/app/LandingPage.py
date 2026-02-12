import streamlit as st
from src.components.commons.CommonsUi import *

def LandingPage():
  with open("src/app/_html/LandingPage.html", "r") as content:
    st.markdown(f"{content.read()}", unsafe_allow_html=True)
  HeaderSection()
