import streamlit as st
# import re  # Import the regular expression module
# from database import create_connection, create_tables, insert_user, delete_user, authenticate_user
# from main import display_dashboard

def main():
    session_state = st.session_state

    if 'authenticated' not in session_state:
        session_state.authenticated = False

    # conn = create_connection()
    # create_tables(conn)

    if session_state.authenticated:
        st.write('showing dashboard ')
    else:
        # Use st.tabs to create tabs for Login and Register
        # tabs = st.tabs(["Login", "Register"])

        # Initially, hide the Register tab
        # tabs[1].visible = False

        # Login tab content
        # with tabs[0]:
        st.subheader("Login")
        username = st.text_input("Username1")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")
        if login_button:
            if authenticate_user( username, password):
                session_state.authenticated = True
                st.success("Login successful!")
                st.rerun()
            # else:
                st.error("Invalid username or password")

def authenticate_user(username,password):
    if username=='admin' and password=="admin":
        return True
    else:
        return False
if __name__=="__main__":
    main()