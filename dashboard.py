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
   "data", "data2"
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

        import numbers
        import pandas as pd
        import streamlit as st
        from streamlit.hashing import _CodeHasher
        from streamlit.report_thread import get_report_ctx
        from streamlit.server.server import Server


        def main():
            state = get_state()
            if state.data is None:
                state.data = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

            editor = TableEditor("table1", state.data)

            # Check for button interactions and updates the internal data state
            editor.interact()
            state.data = editor.data

            st.table(state.data)

            state.sync()


        class TableEditor:
            """Encapsulates editable tables using streamlit.
            Usage:
            >>> original_df = pd.DataFrame(...)
            >>> editor = TableEditor("editor uid", original_df)
            >>> editor.interact()
            >>> edited_df = editor.data
            """
            def __init__(self, uid, dataframe, layout=None):
                """Initialize TableEditor instance.
                Args:
                    uid (str): Table unique identifier to avoid widget key conflict.
                    dataframe (pandas.DataFrame): Data to be edited.
                    layout (list, optional): List of column proportions. See
                    https://docs.streamlit.io/en/stable/api.html#streamlit.beta_columns.
                    Defaults to None.
                """
                self._uid = uid
                self._data = dataframe.copy()
                self._n_rows = dataframe.shape[0]
                self._n_cols = dataframe.shape[1]
                self._cells = {}
                self._update_button = None
                self._add_row_button = None
                self._delete_buttons = {}
                if layout is None:
                    # If layout not defined the dataframe columns will be 5 times bigger
                    # than Delete buttons column
                    layout = st.beta_columns(
                        [5 if col < self._n_cols else 1 for col in range(self._n_cols + 1)]
                    )
                self._layout = layout
                self._create_table()
                self._create_buttons()

            @property
            def data(self):
                return self._data

            def interact(self):
                if self._update_button:
                    self._update()

                if self._add_row_button:
                    self._add_row()

                for key, button in self._delete_buttons.items():
                    if button:
                        # key[1] is always the row index
                        self._delete_row(key[1])
                        break

            def _create_table(self):
                # Gets only layout columns to put actual data from dataframe - indices [0:n_cols]
                data_columns = self._layout[:self._n_cols]

                for col_index, column in enumerate(data_columns):
                    # Writes column names
                    column.markdown(f"**{self._data.columns[col_index]}**")
                    for row_index in range(self._n_rows):
                        key = (self._uid, col_index, row_index)
                        with column:
                            self._add_cell(key, self._data.iloc[row_index, col_index])

            def _create_buttons(self):
                # Always the last column in column layout
                button_del_column = self._layout[self._n_cols]

                # The buttons are not horizontally aligned with input widgets, so we need this little hack
                button_del_column.markdown("<div style='margin-top:4.2em;'></div>", unsafe_allow_html=True)

                for row_index in range(self._n_rows):
                    key = (self._uid, row_index)
                    self._delete_buttons[key] = button_del_column.button("Delete", key=str(key))
                    button_del_column.markdown(
                        "<div style='margin-top:2.43em;'></div>", unsafe_allow_html=True
                    )

                self._add_row_button = st.button("Add Row", key=f"add_row_button_{self._uid}")
                self._update_button = st.button(label="Update Data", key=f"update_button_{self._uid}")

            def _update(self):
                for col_index in range(self._n_cols):
                    for row_index in range(self._n_rows):
                        new_value = self._cells[(self._uid, col_index, row_index)].value
                        self._data.iloc[row_index, col_index] = new_value
                self._data = self._data.sort_values(by=self._data.columns.to_list(), ignore_index=True)

            def _add_row(self):
                columns = self._data.columns.to_list()
                values = [[1] for _ in columns]
                row = pd.DataFrame(dict(zip(columns, values)))
                self._data = self._data.append(row).reset_index(drop=True)

                for col_index in range(self._n_cols):
                    row_index = self._n_rows
                    key = (self._uid, col_index, row_index)
                    with(self._layout[col_index]):
                        self._add_cell(key, self._data.iloc[row_index, col_index])

            def _delete_row(self, row_index):
                self._data = self._data.drop([row_index]).reset_index(drop=True)
                for col_index in range(self._n_cols):
                    key = (self._uid, col_index, row_index)
                    self._delete_cell(key)

            def _add_cell(self, key, value):
                new_cell = _Cell(key)
                new_cell.value = value
                self._cells[key] = new_cell

            def _delete_cell(self, key):
                del self._cells[key]


        class _Cell:
            def __init__(self, uid):
                self._uid = uid
                self._value = None
                self._widget = st.empty()

            @property
            def value(self):
                return self._value

            @value.setter
            def value(self, value):
                if isinstance(value, numbers.Integral):
                    self._value = self._widget.number_input(
                        label="",
                        value=value,
                        min_value=1,
                        step=1,
                        key=self._uid
                    )
                elif isinstance(value, float):
                    self._value = self._widget.number_input(
                        label="",
                        value=value,
                        min_value=0.,
                        step=0.001,
                        format="%.3f",
                        key=self._uid
                    )
                else:
                    self._value = self._widget.text_input(
                        label="",
                        value=value,
                        key=self._uid
                    )

        #
        # Code below is from https://gist.github.com/okld/0aba4869ba6fdc8d49132e6974e2e662.
        #


        class _SessionState:

            def __init__(self, session, hash_funcs):
                """Initialize SessionState instance."""
                self.__dict__["_state"] = {
                    "data": {},
                    "hash": None,
                    "hasher": _CodeHasher(hash_funcs),
                    "is_rerun": False,
                    "session": session,
                }

            def __call__(self, **kwargs):
                """Initialize state data once."""
                for item, value in kwargs.items():
                    if item not in self._state["data"]:
                        self._state["data"][item] = value

            def __getitem__(self, item):
                """Return a saved state value, None if item is undefined."""
                return self._state["data"].get(item, None)

            def __getattr__(self, item):
                """Return a saved state value, None if item is undefined."""
                return self._state["data"].get(item, None)

            def __setitem__(self, item, value):
                """Set state value."""
                self._state["data"][item] = value

            def __setattr__(self, item, value):
                """Set state value."""
                self._state["data"][item] = value

            def clear(self):
                """Clear session state and request a rerun."""
                self._state["data"].clear()
                self._state["session"].request_rerun()

            def sync(self):
                """Rerun the app with all state values up to date from the beginning to fix rollbacks."""

                # Ensure to rerun only once to avoid infinite loops
                # caused by a constantly changing state value at each run.
                #
                # Example: state.value += 1
                if self._state["is_rerun"]:
                    self._state["is_rerun"] = False

                elif self._state["hash"] is not None:
                    if self._state["hash"] != self._state["hasher"].to_bytes(self._state["data"], None):
                        self._state["is_rerun"] = True
                        self._state["session"].request_rerun()

                self._state["hash"] = self._state["hasher"].to_bytes(self._state["data"], None)


        def _get_session():
            session_id = get_report_ctx().session_id
            session_info = Server.get_current()._get_session_info(session_id)

            if session_info is None:
                raise RuntimeError("Couldn't get your Streamlit Session object.")

            return session_info.session


        def get_state(hash_funcs=None):
            session = _get_session()

            if not hasattr(session, "_custom_session_state"):
                session._custom_session_state = _SessionState(session, hash_funcs)

            return session._custom_session_state


        if __name__ == "__main__":
            main()


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

        def data2():

            # https://gist.githubusercontent.com/tvst/036da038ab3e999a64497f42de966a92/raw/f0db274dd4d295ee173b4d52939be5ad55ae058d/SessionState.py

            # Create an empty dataframe
            data = pd.DataFrame(columns=["Random"])
            st.text("Original dataframe")

            # with every interaction, the script runs from top to bottom
            # resulting in the empty dataframe
            st.dataframe(data) 

            # persist state of dataframe
            session_state = SessionState.get(df=data)

            # random value to append; could be a num_input widget if you want
            random_value = np.random.randn()

            if st.button("Append random value"):
                # update dataframe state
                session_state.df = session_state.df.append({'Random': random_value}, ignore_index=True)
                st.text("Updated dataframe")
                st.dataframe(session_state.df)

            # still empty as state is not persisted
            st.text("Original dataframe")
            st.dataframe(data)
    
    
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

        df = pd.DataFrame({'timestamp': [2120, 2125, 2136],
                           'vehicle': ['A', 'B', 'A'],
                          })
        grid_return = AgGrid(df,
                             editable=True,
                             #gridOptions=gb.build(),
                             #data_return_mode="filtered_and_sorted",
                             #update_mode="no_update",
                             #fit_columns_on_grid_load=True,
                             #theme = light
                            )
        new_df = grid_return['data']
        
        newrow = JsCode(
             """
             gridApi.applyTransaction({ add:[{ }] })
       
             """)
           
        if st.button('add'):
            newrow
           
            
main()
