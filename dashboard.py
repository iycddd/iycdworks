showErrorDetails = False
hideTopBar = True

###########
## setup ##
###########

import streamlit as st
import numpy as np
import pandas as pd
import streamlit_authenticator as stauth
from streamlit_webrtc import webrtc_streamer


from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from st_aggrid.shared import GridUpdateMode, DataReturnMode, JsCode



#widen page
st.set_page_config(layout="wide")

###

#authentication system
def authenticate():
    login = False
    while login == False:
        names = ['tim']
        usernames = ['iycddd']
        passwords = ['123']

        hashed_passwords = stauth.hasher(passwords).generate()

        authenticator = stauth.authenticate(names,usernames,hashed_passwords,
            'some_cookie_name','some_signature_key',cookie_expiry_days=30)

        name, authentication_status = authenticator.login('Login','main')

        if authentication_status:
            st.write('okayyyyyyy')
            login = True
        elif authentication_status == False:
            st.error('Username/password is incorrect')
        elif authentication_status == None:
            st.warning('Please enter your username and password')
#    if st.session_state['authentication_status']:
#        st.write('Welcome *%s*' % (st.session_state['name']))
#        st.title('Some content')
#    elif st.session_state['authentication_status'] == False:
#        st.error('Username/password is incorrect')
#    elif st.session_state['authentication_status'] == None:
#        st.warning('Please enter your username and password')

#authenticate()

###

#sidebar
add_selectbox = st.sidebar.radio(
  "menu",
  ("main", "feed A", "feed B", "feed C",
   "data", "data2", "data3"
  ))

#############
## vidlist ##
#############

vidlist = ["https://www.youtube.com/watch?v=5qap5aO4i9A",
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
  elif add_selectbox == 'data':
    data()
  elif add_selectbox == 'data2':
    data2()
  elif add_selectbox == 'data3':
    data3()

def mainpage():

      #layout columns
      firstcol, blankcol, seccol, blankcol2, thirdcol = st.columns((3,2,6,2,3))

      #header column
      with firstcol:
        st.title("CV DASHBOARD")
        st.subheader("next gen fusion 👌")

      #sightings input column
      with thirdcol:
        st.title(" ")
        spotted = st.text_input("TARGET SIGHTED:", "clear")
        st.write("input 'clear' to clear")

      #sightings display column
      with seccol:
        st.title(" ")
        if spotted == "clear":
          st.empty()
        else:
          warn = st.write("⚠️ ", spotted, "has been spotted ⚠️")
          st.warning("targets sighted!")

      #columns
      col1, col2, col3 = st.columns(3)

      #vidcontent
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
        slideval = st.slider("", 1, 5, 3, None, None, 2)  

      #columns
      col1, col2 = st.columns((3,slideval))

      #vidcontent
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
        slideval = st.slider("", 1, 5, 3, None, None, 2)  

      #columns
      col1, col2 = st.columns((3,slideval))

      #vidcontent
      with col1:
        st.header("feed C")
        st.video(vidlist[4])

      with col2:
        st.header("anafi")
        st.video(vidlist[5])

## data ##
   
def data():    

        df = pd.DataFrame({'timestamp': [2120, 2125, 2136],
                           'vehicle': ['A', 'B', 'A'],
                           'quantity': ['1', '2', '1']
                          })
        grid_return = AgGrid(df,
                             editable=True,
                             #gridOptions=gb.build(),
                             #data_return_mode="filtered_and_sorted",
                             #update_mode="no_update",
                             #fit_columns_on_grid_load=True,
                             allow_unsafe_jscode=True
                             #theme=light
                            )
        new_df = grid_return['data']
        
        newrow = JsCode("""
        function(e) {
            let api = e.api;        
            let sel = api.getSelectedRows();

            api.applyTransaction({add: sel});
        };
        """)
        gb.configure_grid_options(onRowSelected=js) 
           
        if st.button('add'):
            newrow
        
def data2():

    @st.cache(allow_output_mutation=True)
    def get_data():
       return []

    col1 = st.text_input("Timestamp")
    col2 = st.text_input("Detected")
    col3 = st.text_input("Quantity")
    
    def addrow():
       get_data().append({"Timestamp": col1, "Detected": col2, "Quantity": col3})
    
    if st.button("Add row"):
       addrow()

    st.write(pd.DataFrame(get_data()))
            
def data3():
    
    def display_table(df: pd.DataFrame) -> AgGrid:
        # Configure AgGrid options
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_selection('single', use_checkbox=True)

        # Custom JS code for interactive rows deletion
        # For credits SEE: 
        # https://github.com/PablocFonseca/streamlit-aggrid/blob/1acb526ba43b5aac9c8eb22cc54eeb05696cd84d/examples/example_highlight_change.py#L21
        # https://ag-grid.zendesk.com/hc/en-us/articles/360020160932-Removing-selected-rows-or-cells-when-Backspace-or-Delete-is-pressed
        js = JsCode("""
        
        function(e) {
            let api = e.api;        
            let sel = api.getSelectedRows();

            api.applyTransaction({add: sel});
            
            alert(4);
            
            api.applyTransaction({update: sel})
            
        };
        """)
        gb.configure_grid_options(onRowSelected=js) 
        
        
        
        return AgGrid(
            df,
            gridOptions=gb.build(),
            # this override the default VALUE_CHANGED
            update_mode=GridUpdateMode.MODEL_CHANGED,
            # needed for js injection
            allow_unsafe_jscode=True
        )
    

    # Define dummy data
    df = pd.DataFrame({'timestamp': [2120, 2125, 2136],
                           'vehicle': ['A', 'B', 'A'],
                           'quantity': ['1', '2', '1']
                          })

    st.info("Select a row to remove it")
    response = display_table(df)
    st.write(f"Dataframe shape: {response['data'].shape}")
     
        
      
        
main()
