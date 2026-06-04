import streamlit as st
import plotly.express as px
import numpy as np

from utils.load_data import load_data

df = load_data()

st.title("🔥 Correlation Analysis")

numeric_df = df.select_dtypes(include=np.number)

corr = numeric_df.corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Correlation Heatmap"
)

st.plotly_chart(fig, use_container_width=True)
