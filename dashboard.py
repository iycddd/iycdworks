import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title("CV DASHBOARD")

st.markdown(' ## Key Metrics')

col1, col2, col3 = st.columns(3)
col1.metric(label = "SPDR S&P 500", value = '%.2f'
col3.metric("BTC, "$46,583.91", "+4.87%")

st.markdown('## Detailed Charts')

chart1, chart2 = st.columns(2)
