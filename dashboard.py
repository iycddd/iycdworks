import streamlit as st
import pandas as pd
import numpy as np

#widen page
st.set_page_config(layout="wide")

#vidlist
vidlist = ["https://www.youtube.com/watch?v=CVHj7Wxhvdo",
          "https://www.youtube.com/watch?v=hG5i6XM6x7w",
          "https://www.youtube.com/watch?v=XLxToJ4mauY",
          "https://www.youtube.com/watch?v=9EJIH8kxTn8",
          "https://www.youtube.com/watch?v=W9wT8uOjv6A",
          "https://www.youtube.com/watch?v=cbP2N1BQdYc"]

#sidebar
add_selectbox = st.sidebar.radio(
  "menu",
  ("main", "feed A", "feed B", "feed C"))

#############
## display ##
#############

if add_selectbox == 'main':
          st.title("CV DASHBOARD")
          st.subheader("next gen fusion 👌")
          #columns
          col1, col2, col3 = st.columns(3)
          #contents
          with col1:
            st.header("feed A")
            st.video(vidlist[0])
            st.video(vidlist[1])
          with col2:
            st.header("feed B")
            st.video(vidlist[2])
            st.video(vidlist[3])
          with col3:
            st.header("feed C")
            st.video(vidlist[4])
            st.video(vidlist[5])
          
elif add_selectbox == 'feed A':
          with st.expander(
            num = st.slider('zoom slider', 1, 5, 3))
          #columns
          col1, col2 = st.columns((num,3))
          with col1:
            st.header("feed A")    
            st.video(vidlist[0])
          with col2:
            st.header("anafi")
            st.video(vidlist[1])
          
elif add_selectbox == 'feed B':
          #columns
          col1, col2 = st.columns((num,3))
          with col1:
            st.header("feed B")
            st.video(vidlist[2])
          with col2:
            st.header("anafi")
            st.video(vidlist[3])
          
elif add_selectbox == 'feed C':
          #columns
          col1, col2 = st.columns((num,3))
          with col1:
            st.header("feed C")
            st.video(vidlist[4])
          with col2:
            st.header("anafi")
            st.video(vidlist[5])
