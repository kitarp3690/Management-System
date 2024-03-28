import streamlit as st
import psycopg2
import hashlib

class User:
    def __init__(self):
        pass

    # def connect_to_db(self):
    #     try:
    #         self.connection = psycopg2.connect(
    #             dbname="streamlit_project",
    #             user="postgres",
    #             password="admin",
    #             host="localhost",
    #             port=5432
    #         )
    #         return self.connection.cursor() 
    #     except psycopg2.Error as e:
    #         st.error(f"Error connecting to PostgreSQL database: {e}")
    #         return None

    def front_page(self):
        st.sidebar.title("GOD Pratik")
        if st.sidebar.button("Login",key="front_login_button1"):
            self.login_page()
        if st.sidebar.button("Sigup",key="front_signup_button"):
            # self.signup_page()
            pass
        # st.title("The rise is god")
    
    def login_page(self):
        st.title("Login Page")
        with st.form(key='login_form'):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            st.write(submitted)

            if submitted:
                '''cursor = self.connect_to_db()
                if cursor:
                    sql = f"SELECT * FROM users WHERE username=%s "
                    values = (username,)
                    
                    try:
                        cursor.execute(sql, values)
                        result = cursor.fetchone()
                        if result:
                            hashed_password = hashlib.sha256(password.encode()).hexdigest()
                            if result[1] == hashed_password:
                                st.success("Login successful!")
                            else:
                                st.error("Incorrect password")
                        else:
                            st.error("User not found")
                    except psycopg2.Error as e:
                        st.error(f"Error verifying login: {e}")
                    cursor.close()'''
                if username=='admin' and password=='admin':
                    st.success("finally mf")
                else:
                    st.error("invalid usename and password")

    # def signup_page(self):
    #     st.title("Signup Page")
    #     with st.form(key="signup_form"):
    #         # submitted_signup=False
    #         new_username = st.text_input("New Username")
    #         new_password = st.text_input("New Password", type="password")
    #         confirm_password = st.text_input("confirm password",type="password")
    #         submitted_signup=st.button("Submit")
    #             # while submitted_signup==False:
    #         #     continue
    #         # if st.form_submit_button("Submit"):
    #     if submitted_signup:
    #             # check_name=self.check_username(new_username,new_password)
    #             # if not check_name:
    #             #     st.error('USername already exi("Submit")st')
    #         if new_password != confirm_password:
    #             st.error("Passwords don't match")
    #         elif len(new_password) < 8:
    #             st.error("Password must be at least 8 characters")
    #         else:
    #             self.create_user(new_username, new_password)
    #             # st.write(submitted_signup)
    #     # st.write(submitted_signup,len(new_password))

    # def check_username(self,username,password):
    #     """ This method will make sure that no user with same username is repeated """
    #     sql=f"select * from users where username=%s" 
    #     values = (username)
    
    #     cursor=self.connect_to_db()
    #     if cursor:
    #         try:
    #             cursor.execute(sql,values)
    #             result=cursor.fetchone()
    #             if result:
    #                 cursor.close()
    #                 return False
    #             else:
    #                 cursor.close()
    #                 return True
    #         except psycopg2.Error as e:
    #             st.error(f"Error verifying login: {e}")
    #         cursor.close()

    # def create_user(self,username,password):
        # hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # sql = f"INSERT INTO users (username, password) VALUES (%s, %s)"
        # values = (username, hashed_password)

        # cursor = self.connect_to_db()
        # if cursor:
        #     try:
        #         cursor.execute(sql, values)
        #         self.connection.commit()
        #         st.success("User account created successfully!")
        #     except psycopg2.Error as e:
        #         st.error(f"Error creating user account: {e}")
        #     cursor.close()

if __name__ == "__main__":
    user1=User()
    user1.front_page()