import sys
import os

ROOT = os.path.abspath(os.path.dirname(__file__))
if ROOT not in sys.path:
  sys.path.insert(0, ROOT)

import streamlit as st
from src.app.LandingPage import LandingPage

st.set_page_config(
	page_title="Linear Algebra Calculator",
  layout="wide",
  initial_sidebar_state="collapsed"
)

def loadGlobalsCSS():
	with open("src/styles/globals.css", "r") as stylesheet:
		st.markdown(f"<style>{stylesheet.read()}</style>", unsafe_allow_html=True)

loadGlobalsCSS()

def main(): LandingPage()

if __name__ == "__main__": main()
