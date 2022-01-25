#import libraries
import streamlit as st
import pandas as pd
import numpy as np

#header
st.title("CV DASHBOARD")
st.subheader("subheader <3")

#columns
col1, col2 = st.columns(2)
col1.header("video 1")
col2.header("video 2")

#define videos
vid1 = st.video("https://www.youtube.com/watch?v=cuG7GCXCi48")
vid2 = st.video("https://www.youtube.com/watch?v=CVHj7Wxhvdo")

#video
#st.video("https://www.youtube.com/watch?v=PoAeFpUB1hA")

#video2
#st.video("https://www.youtube.com/watch?v=CVHj7Wxhvdo")
