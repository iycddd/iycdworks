###########
## setup ##
###########

import streamlit as st
import pandas as pd
import numpy as np

from streamlit_webrtc import (
    AudioProcessorBase,
    RTCConfiguration,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)

#widen page
st.set_page_config(layout="wide")

#sidebar
add_selectbox = st.sidebar.radio(
  "menu",
  ("main", "feed A", "feed B", "feed C"))







#############
## vidlist ##
#############

#just need to change these to get live videos working i think :)

vidlist = ["https://www.youtube.com/watch?v=CVHj7Wxhvdo",
          "https://www.youtube.com/watch?v=hG5i6XM6x7w",
          "https://www.youtube.com/watch?v=XLxToJ4mauY",
          "https://www.youtube.com/watch?v=9EJIH8kxTn8",
          "https://www.youtube.com/watch?v=W9wT8uOjv6A",
          "https://www.youtube.com/watch?v=cbP2N1BQdYc"]







#############
## display ##
#############

## main ##

if add_selectbox == 'main':
  
          firstcol, seccol = st.columns((12,1))
          with firstcol:
            st.title("CV DASHBOARD")
            st.subheader("next gen fusion 👌")
          with seccol:
            st.title(" ")
            clicked = st.button("⚠️")
            st.caption("this button doesnt do anything yet")
            
          #columns
          col1, col2, col3 = st.columns(3)
          
          #content
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
          
## feed A ##
         
elif add_selectbox == 'feed A':
          
          #zoomslider
          with st.expander("adjust zoom"):
            slideval = st.slider("", 1, 5, 3, None, None, 1)
          
          #columns
          col1, col2 = st.columns((3,slideval))
          
          #content
          with col1:
            st.header("feed A")    
            st.video(vidlist[0])
          with col2:
            st.header("anafi")
            st.video(vidlist[1])
          
## feed B ##
          
elif add_selectbox == 'feed B':
          
          #zoomslider
          with st.expander("adjust zoom"):
            slideval = st.slider("", 1, 5, 3, None, None, 2)
          
          #columns
          col1, col2 = st.columns((3,slideval))
          
          #content
          with col1:
            st.header("feed B")
            st.video(vidlist[2])
                    
          with col2:
            st.header("anafi")
            st.video(vidlist[3])
          
## feed C ##
          
elif add_selectbox == 'feed C':
          
          #zoomslider
          with st.expander("adjust zoom"):
            slideval = st.slider("", 1, 5, 3, None, None, 3)
          
          #columns
          col1, col2 = st.columns((3,slideval))
          
          #content
          with col1:
            st.header("feed C")
            st.video(vidlist[4])
                    
          with col2:
            st.header("anafi")
            st.video(vidlist[5])
