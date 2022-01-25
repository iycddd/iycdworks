echo "# iycdworks" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/iycddd/iycdworks.git
git push -u origin main

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title("CV DASHBOARD")

st.markdown(' ## Key Metrics')

col1, col2, col3 = st.columns(3)
col1.metric(label = "SPDR S&P 500", value = '%.2f'
col2.metric("FTEC", "$121.10", "0.46&")
col3.metric("BTC, "$46,583.91", "+4.87%")

st.markdown('## Detailed Charts')

chart1, chart2 = st.columns(2)
