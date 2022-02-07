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
from st_aggrid.shared import GridUpdateMode, DataReturnMode

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

        vpth = “your path” # path that contains the csv file
        csvfl = “tst.csv” # I used a small csv file containing 2 columns: Name & Amt
        tdf = pd.read_csv(vpth + csvfl) # load csv into dataframe

        gb = GridOptionsBuilder.from_dataframe(tdf)
        gb.configure_column(“Name”, header_name=(“F Name”), editable=True)
        gb.configure_column(“Amt”, header_name=(“Amount”), editable=True, type=[“numericColumn”,“numberColumnFilter”,“customNumericFormat”], precision=0)

        gridOptions = gb.build()
        dta = AgGrid(tdf,
        gridOptions=gridOptions,
        reload_data=False,
        height=200,
        editable=True,
        theme=“streamlit”,
        data_return_mode=DataReturnMode.AS_INPUT,
        update_mode=GridUpdateMode.MODEL_CHANGED)

        st.write(“Please change an amount to test this”)

        if st.button(“Iterate through aggrid dataset”):
        for i in range(len(dta[‘data’])): # or you can use for i in range(tdf.shape[0]):
        st.caption(f"df line: {tdf.loc[i][0]} | {tdf.loc[i][1]} || AgGrid line: {dta[‘data’][‘Name’][i]} | {dta[‘data’][‘Amt’][i]}")

            # check if any change has been done to any cell in any col by writing a caption out
            if tdf.loc[i]['Name'] != dta['data']['Name'][i]:
                st.caption(f"Name column data changed from {tdf.loc[i]['Name']} to {dta['data']['Name'][i]}...")
                # consequently, you can write changes to a database if/as required

            if tdf.loc[i]['Amt'] != dta['data']['Amt'][i]:
                st.caption(f"Amt column data changed from {tdf.loc[i]['Amt']} to {dta['data']['Amt'][i]}...")

        tdf = dta['data']    # overwrite df with revised aggrid data; complete dataset at one go
        tdf.to_csv(vpth + 'file1.csv', index=False)  # re/write changed data to CSV if/as required
        st.dataframe(tdf)    # confirm changes to df

main()
