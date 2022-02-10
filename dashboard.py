from st_aggrid.shared import GridUpdateMode, DataReturnMode, JsCode
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
# import chime
from streamlit_webrtc import webrtc_streamer
import pandas as pd
import numpy as np
import streamlit as st
import csv
import time
import requests

#showErrorDetails = False
#hideTopBar = True

###########
## setup ##
###########

# widen page
st.set_page_config(layout="wide")

# sidebar
add_selectbox = st.sidebar.radio(
    "dashboard selector",
    ("main", "feed A", "feed B", "feed C", "data"))

#############
## vidlistuwu ##
#############

vidlist = [  # "rtmp://13.251.140.213/live/hi",
    "https://www.youtube.com/watch?v=XWq5kBlakcQ",
    "https://www.youtube.com/watch?v=XLxToJ4mauY",
    "https://www.youtube.com/watch?v=9EJIH8kxTn8",
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

    # layout columns
    firstcol, blankcol, seccol, blankcol2, thirdcol = st.columns(
        (3, 2, 6, 2, 3))

    # header column
    with firstcol:
        st.title("CV DASHBOARD")
        st.subheader("next gen fusion 👌")

    # sightings input column
    with thirdcol:
        st.title(" ")

        spotted = st.text_input("TARGET SIGHTED:", "")

        if st.button("alert"):
            soundalert = True
        else:
            soundalert = False

    # sightings display column
    with seccol:
        st.title(" ")

        # warning system
        if soundalert == False or spotted == '':
            st.empty()
        else:
            # chime.success()
            st.write("⚠️ ", spotted, "has been spotted ⚠️")
            st.warning("targets sighted!")

    # columns
    col1, col2, col3 = st.columns(3)

    # vidcontent
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

############
## feed A ##
############


def feedA():

    # zoomslider
    with st.expander("adjust zoom"):
        slideval = st.slider("", 1, 5, 3, None, None, 2)

    # columns
    col1, col2 = st.columns((3, slideval))

    # vidcontent
    with col1:
        st.header("feed A")
        st.video(vidlist[0])
    with col2:
        st.header("anafi")
        st.video(vidlist[1])

############
## feed B ##
############


def feedB():

    # zoomslider
    with st.expander("adjust zoom"):
        slideval = st.slider("", 1, 5, 3, None, None, 2)

    # columns
    col1, col2 = st.columns((3, slideval))

    # content
    with col1:
        st.header("feed B")
        st.video(vidlist[2])

    with col2:
        st.header("anafi")
        st.video(vidlist[3])

############
## feed C ##
############


def feedC():

    # zoomslider
    with st.expander("adjust zoom"):
        slideval = st.slider("", 1, 5, 3, None, None, 2)

    # columns
    col1, col2 = st.columns((3, slideval))

    # vidcontent
    with col1:
        st.header("feed C")
        st.video(vidlist[4])

    with col2:
        st.header("anafi")
        st.video(vidlist[5])

##########
## data ##
##########


def data():

    st.title('data log')
    # state session
    if not 'testdf' in st.session_state:
        df = st.session_state['testdf'] = pd.DataFrame({'trackId': [], 'tags': [], 'score': [], 'firstDetected': [], 'lastDetected': []})
    df = st.session_state['testdf']

    # data live update
    # data = {'Timestamp': ['343', '2342'], 'Detected': [
    #     '343', '2342'], 'Quantity': ['343', '2342']}
    # dff = pd.DataFrame(data)
    # dff.to_pickle('my_data.pkl')

    data = {'trackId': [], 'tags': [], 'score': [], 'firstDetected': [], 'lastDetected': []}

    with open('MOCK_DATA.csv', mode='r') as infile:
        for line in infile:
            a, b, c = line.strip().split(",")
            if a == "trackId":
                continue
            data['trackId'].append(a)
            data['tags'].append(b)
            data['score'].append(c)
            data['firstDetected'].append(d)
            data['lastDetected'].append(d)

    # addrow() and delrow()
    def addrow():
        st.session_state['testdf'] = df.append(
            {"trackId": col1, "tags": col2, "score": col3, "firstDetected": col3, "lastDetected": col3}, ignore_index=True)

    def delrow():
        if df.empty == False:
            st.session_state['testdf'] = df.drop(
                index=st.session_state['testdf'].iloc[-1].name)

    def updatedata():
        df = st.session_state['testdf']

        # if df.empty == True:
        # st.session_state['testdf'] = df.append(
        # {"timestamp": '', "vehicle": '', "quantity": ''}, ignore_index=True)

        # append data from table
        for i in range(len(data['trackId'])):
            col1 = data['trackId'][i]
            col2 = data['tags'][i]
            col3 = data['score'][i]
            col4 = data['firstDetected'][i]
            col4 = data['lastDetected'][i]
            df = st.session_state['testdf']

            st.session_state['testdf'] = df.append(
                {"trackId": col1, "tags": col2, "score": col3, "firstDetected": col3, "lastDetected": col3}, ignore_index=True)

    # user input
    with st.expander("edit logs"):
        col1 = st.text_input("trackId")
        col2 = st.text_input("tags")
        col3 = st.text_input("score")
        col4 = st.text_input("firstDetected")
        col5 = st.text_input("lastDetected")

        if st.button("Add row"):
            addrow()
        if st.button("Remove row"):
            delrow()

    st.write(st.session_state['testdf'])

    # updatedata() button
    if st.button("Update Data"):
        updatedata()
        with st.spinner('Wait for it...'):
            time.sleep(1)
        st.success('Done!')


    # with st.empty():
    #     while True:
        # st.warning('hi')
        # read_df = pd.read_pickle('my_data.pkl')
        # read_df
        # for i in range(len(data['Timestamp'])):
        #     col1 = data['Timestamp'][i]
        #     col2 = data['Detected'][i]
        #     col3 = data['Quantity'][i]
        #     df = st.session_state['testdf']
        #     st.session_state['testdf'] = df.append(
        #         {"timestamp": col1, "vehicle": col2, "quantity": col3}, ignore_index=True)
main()
