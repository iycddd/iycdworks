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
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, JsCode

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
   "data"
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

#        df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
#        grid_return = AgGrid(df,
#                             editable=True,
#                             #gridOptions=gb.build(),
#                             #data_return_mode="filtered_and_sorted",
#                             #update_mode="no_update",
#                             #fit_columns_on_grid_load=True,
#                             #theme = light
#                            )
#        new_df = grid_return['data']
#        gridApi.applyTransaction({add: [{}]})
#        

        @st.cache(allow_output_mutation=True)
        def load_data():
            df = pd.DataFrame({'fruit':['Apple', 'Banana'], 'unit_price':[50,25], 'num_units':[0,0], 'total_price':[0,0]})
            return df

        loaded_data = load_data()

        num_units = st.slider('Select Number of Units', 0, 130, 1)
        loaded_data['num_units'] = num_units

        js_calculate_total = JsCode("""

            function (params) {

                 var unit_price = params.data.unit_price;
                 var num_units = params.data.num_units;
                 return (unit_price * num_units).toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0});

            }

        """)

        gb = GridOptionsBuilder.from_dataframe(loaded_data) #Infer basic colDefs from dataframe types
        # Grid Builder configurations
        gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=False)
        # Below, the first parameters are all the same as in the load_data dateframe, but the "header_name" is what is displayed and can be anything 
        gb.configure_column("fruit", header_name='Fruit', pivot=True, sort='asc')
        gb.configure_column("unit_price", header_name='Unit Price', sort='desc', type=["numericColumn","numberColumnFilter"], valueFormatter="data.estimatednotional_usd.toLocaleString(undefined, {minimumFractionDigits: 0, maximumFractionDigits: 0})", aggFunc='sum') # defines numeric column
        gb.configure_column("total_price", header_name='Total Price', type=["numericColumn","numberColumnFilter"], editable=False, valueGetter=js_calculate_total) # uses custom value getter for calculated column
        gridOptions = gb.build()

        grid_response = AgGrid(
                loaded_data,
                gridOptions = gridOptions,
                height=200,
                width='100%', # how much of the Streamlit page width this grid takes up
                update_mode=GridUpdateMode.MODEL_CHANGED,
                fit_columns_on_grid_load=True, # automatically fits all columns to be displayed in the grid in one view (doesn't always seem to work)
                allow_unsafe_jscode=True, # Set to True to allow the Javascript code to be injected
                enable_enterprise_modules=True, # enables right click and fancy features - can add license key as another parameter (license_key='string') if you have one
                key='select_grid', # stops grid from re-initialising every time the script is run
                reload_data=True, # allows modifications to loaded_data to update this same grid entity
                theme='light'
                )
            
            

main()
