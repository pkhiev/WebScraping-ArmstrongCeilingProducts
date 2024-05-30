import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px


st.set_page_config(
    page_title="Product Data for Armstrong Ceilings",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

df = pd.read_csv('ArmstrongProductList.csv')

print(df)