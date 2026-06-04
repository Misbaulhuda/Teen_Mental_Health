import streamlit as st
import plotly.express as px
from utils.load_data import load_data

df = load_data()

st.title("📈 Univariate Analysis")

fig = px.histogram(
    df,
    x="daily_social_media_hours",
    nbins=20,
    title="Daily Social Media Hours Distribution"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.histogram(
    df,
    x="sleep_hours",
    nbins=20,
    title="Sleep Hours Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

fig3 = px.pie(
    df,
    names="platform_usage",
    title="Platform Usage Distribution"
)

st.plotly_chart(fig3, use_container_width=True)
