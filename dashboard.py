import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title("CV DASHBOARD")

st.markdown(' ## Key Metrics')

col1, col2, col3 = st.columns(3)
col1.metric(label = "SPDR S&P 500", value = '%.2f'

st.markdown('## Detailed Charts')

chart1, chart2 = st.columns(2)
