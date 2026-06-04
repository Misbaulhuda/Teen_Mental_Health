import streamlit as st

st.set_page_config(
    page_title="Teen Mental Health Dashboard",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Teen Mental Health Analytics Dashboard")

st.markdown("""
### Project Objective

Analyze the relationship between:

- Social Media Usage
- Sleep
- Stress
- Anxiety
- Academic Performance

and Depression Risk among Teenagers.
""")

st.image(
    "https://images.unsplash.com/photo-1506126613408-eca07ce68773",
    use_container_width=True
)
