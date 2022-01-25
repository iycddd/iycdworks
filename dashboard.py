#import libraries
import streamlit as st
import pandas as pd
import numpy as np

#widen page
st.set_page_config(layout="wide")

#header
st.title("CV DASHBOARD")
st.subheader("next gen fusion 👌")

#columns
col1, col2, col3 = st.columns(3)

#sidebar
add_selectbox = st.sidebar.radio(
  "menu",
  ("main", "feed A", "feed B", "feed C"))

def feedA():
  st.header("feed A")
  st.video("https://www.youtube.com/watch?v=CVHj7Wxhvdo")
  st.video("https://www.youtube.com/watch?v=hG5i6XM6x7w")

#contents
with col1:
  feedA()
with col2:
  st.header("feed B")
  st.video("https://www.youtube.com/watch?v=CVHj7Wxhvdo")
  st.video("https://www.youtube.com/watch?v=9EJIH8kxTn8")
with col3:
  st.header("feed C")
  st.video("https://www.youtube.com/watch?v=W9wT8uOjv6A")
  st.video("https://www.youtube.com/watch?v=cbP2N1BQdYc")
