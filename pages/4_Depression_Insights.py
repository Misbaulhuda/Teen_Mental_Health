import streamlit as st
import plotly.express as px
from utils.load_data import load_data

df = load_data()

st.title("🧠 Depression Insights")

fig = px.histogram(
    df,
    x="depression_label",
    title="Depression Distribution"
)

st.plotly_chart(fig, use_container_width=True)

risk_features = [
    "stress_level",
    "anxiety_level",
    "addiction_level",
    "sleep_hours"
]

for feature in risk_features:
    fig = px.box(
        df,
        x="depression_label",
        y=feature,
        title=f"{feature} vs Depression"
    )

    st.plotly_chart(fig, use_container_width=True)
