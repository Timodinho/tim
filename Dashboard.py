import streamlit as st 
import plotly.express as pl
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Superstore!!!",page_icon=":bar_chart:",layout="wide")

#creating and designing the Dashboard Title
st.title(" :bar_chart: Sample Superstore EDA")

# Designing the Title position to be at the top of the page
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
