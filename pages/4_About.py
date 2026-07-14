
import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")

st.title("ℹ️ About Industrial Powder Filling AI")

st.markdown("""
## Project Overview

This application demonstrates how Machine Learning can support tablet manufacturing by predicting tablet weight from industrial process parameters.

### Technologies Used
- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly

### Machine Learning Model
- Algorithm: Linear Regression
- Target: Tablet Weight
- Features: 8 Process Variables

### Process Parameters
- Powder Density
- Moisture Content
- Particle Size
- Compression Force
- Machine Speed
- Fill Depth
- Ambient Temperature
- Relative Humidity

---

### Developed By

**Afzal Shaik**

Master's Student  
Business Management (Data Analytics & AI)  
Berlin, Germany

---

### Future Improvements
- Real-time IoT sensor integration
- Predictive maintenance
- Process optimization
- Quality control dashboard
- Live production monitoring
""")

st.success("Industrial Powder Filling AI Dashboard • Version 2.0")
