import sys
import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
sys.path.append("/Users/yutowilliam/AI_house/Machine_Learning/Final_Project/")

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()