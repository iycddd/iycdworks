#import libraries
import streamlit as st
import pandas as pd
import numpy as np

#header
st.title("CV DASHBOARD")
st.subheader("subheader <3")

#columns
col1, col2, col3 = st.columns(3)

#col 1
with col1:
  st.header("feed A")
  st.video("https://www.youtube.com/watch?v=cuG7GCXCi48")
  st.video("https://www.youtube.com/watch?v=hG5i6XM6x7w")
  
#col 2
with col2:
  st.header("feed B")
  st.video("https://www.youtube.com/watch?v=CVHj7Wxhvdo")

#col 3
with col2:
  st.header("feed C")
  st.video("https://www.youtube.com/watch?v=W9wT8uOjv6A")
