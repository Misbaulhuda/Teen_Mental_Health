import streamlit as st
import plotly.express as px
from utils.load_data import load_data

df = load_data()

st.title("📊 Bivariate Analysis")

fig = px.scatter(
    df,
    x="stress_level",
    y="anxiety_level",
    color="depression_label",
    title="Stress vs Anxiety"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.scatter(
    df,
    x="daily_social_media_hours",
    y="sleep_hours",
    color="depression_label",
    title="Social Media vs Sleep"
)

st.plotly_chart(fig2, use_container_width=True)

fig3 = px.box(
    df,
    x="gender",
    y="daily_social_media_hours",
    title="Gender vs Social Media Usage"
)

st.plotly_chart(fig3, use_container_width=True)
