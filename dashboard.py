#import libraries
import streamlit as st
import pandas as pd
import numpy as np

#header
st.title("CV DASHBOARD")
st.subheader("subheader <3")

#columns
col1, col2 = st.columns(2)

#col 1
with col1:
  st.header("video 1")
  st.image("https://www.youtube.com/watch?v=cuG7GCXCi48")
  
#col 2
with col2:
  st.header("video 2")
  st.image("https://www.youtube.com/watch?v=CVHj7Wxhvdo")
