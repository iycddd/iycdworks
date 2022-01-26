###########
## setup ##
###########

import streamlit as st
import numpy as np

#widen page
st.set_page_config(layout="wide")

#sidebar
add_selectbox = st.sidebar.radio(
  "menu",
  ("main", "feed A", "feed B", "feed C"))

#############
## vidlist ##
#############

vidlist = ["https://www.youtube.com/watch?v=CVHj7Wxhvdo",
          "https://www.youtube.com/watch?v=hG5i6XM6x7w",
          "https://www.youtube.com/watch?v=XLxToJ4mauY",
          "https://www.youtube.com/watch?v=9EJIH8kxTn8",
          "https://www.youtube.com/watch?v=W9wT8uOjv6A",
          "https://www.youtube.com/watch?v=cbP2N1BQdYc"]


#############
## display ##
#############

def main():
  if add_selectbox == 'main':
    mainpage()
  elif add_selectbox == 'feed A':
   feedA()
  elif add_selectbox == 'feed B':
    feedB()
  elif add_selectbox == 'feed C':
    feedC()


def mainpage():
          firstcol, seccol = st.columns((12,1))
          with firstcol:
            st.title("CV DASHBOARD")
            st.subheader("next gen fusion 👌")
          with seccol:
            st.title(" ")
            clicked = st.button("⚠️")
            if clicked == True:
              option = st.selectbox(
                "what was spotted?",
                ("one", "two", "three"))
              st.write(option)
            
            
            def cleaning_function():
              input_data == ''
              
            input_data = st.text_area("input")
            parsed_data = cleaning_function() # Some function you've made to clean the input data
            allow_editing = st.radio("Edit parsed data", [True, False])
            
            if allow_editing:
               output = st.text_area("parsed data", value=parsed_data)
            else:
                st.text(parsed_data)
            
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
         
def feedA():
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
          
def feedB():
          
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
          
def feedC():
          
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

main()
