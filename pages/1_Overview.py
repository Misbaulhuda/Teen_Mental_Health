import streamlit as st
from utils.load_data import load_data
from utils.analysis import dataset_summary

df = load_data()

st.title("📊 Dataset Overview")

summary = dataset_summary(df)

c1,c2,c3,c4 = st.columns(4)

c1.metric("Rows", summary["Rows"])
c2.metric("Columns", summary["Columns"])
c3.metric("Missing", summary["Missing Values"])
c4.metric("Duplicates", summary["Duplicate Rows"])

st.subheader("Sample Data")

st.dataframe(df.head())

st.subheader("Statistical Summary")

st.dataframe(df.describe())
