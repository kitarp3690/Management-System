import streamlit as st  #for UI
import psycopg2 #for postgres db connection
import hashlib  #for hashing password 
import time #for sleep function

class SignUI:
    """ This class is used for Signup and Signin operation """
    def __init__(self):
        pass
    
    def start_connection(self):
        """ This method is used to connect with Database"""
        try:
            self.connection = psycopg2.connect(
                dbname="streamlit_project",
                user="postgres",
                password="admin",
                host="localhost",
                port=5432
            )
            return self.connection.cursor() 
        except psycopg2.Error as e:
            st.error(f"Error connecting to PostgreSQL database: {e}")
            return None
    
    def hash_password(self, password):
        """ This method is used to generate hashed password"""
        hashed_password=hashlib.sha256(password.encode()).hexdigest()
        return hashed_password
    
    def check_user_existence(self,usname):
        """ This method is used to check whether username exist or not since username is the primary key in Database"""
        cursor=self.start_connection()
        if cursor:
            try:
                command="select * from users where username=%s"
                cursor.execute(command,(usname,))
                user=cursor.fetchone()

                if user:
                    return True
                else:
                    return False
            except psycopg2.Error as e:
                st.error(f"Error executing sql commands: {e}")
            finally:
                cursor.close()

    def signup_page(self):
        """ This method is used for Signup purpose"""
        st.subheader("Sign-Up ")
        username=st.text_input("Username")
        password=st.text_input("Password",type='password')
        confirm_password=st.text_input("Confirm password", type='password')
        if st.button("Submit"):
            if username == "" or password == "" or confirm_password == "":
                st.error("Fields can't be empty")
            elif password != confirm_password:  
                st.error("Password didn't match")
            elif len(password)<=8:
                st.error("Password can't be less than 8 characters")
            elif self.check_user_existence(username):
                st.error("Username already exist")
            else:
                password_hashed=self.hash_password(password)
                cursor=self.start_connection()
                if cursor:
                    try:
                        command="insert into users(username,password) values (%s,%s)"
                        cursor.execute(command,(username,password_hashed))
                        self.connection.commit()
                        st.success("Signup successful! ")
                        time.sleep(1.5)
                    except psycopg2.Error as e:
                        st.error(f"Error executing sql commands: {e}")
                    finally:
                        cursor.close()

    def signin_page(self):
        """ This method is used for Signin purpose """
        st.subheader("Signin ")
        username=st.text_input("Username")
        password=st.text_input("Password",type='password')
        if st.button("Login"):
            if username == "" or password == "":
                st.error("Fields can't be empty")
            else:
                password_hashed=self.hash_password(password)
                cursor=self.start_connection()
                if cursor:
                    try:
                        command1="select * from users where username=%s"
                        cursor.execute(command1,(username,))
                        exist1=cursor.fetchone()
                        if exist1:
                            command2="select * from users where username=%s and password=%s"
                            cursor.execute(command2,(username,password_hashed))
                            exist2=cursor.fetchone()
                            if exist2:
                                time.sleep(1.5)
                                st.success("Login successful! ")
                            else:
                                st.error("Password didn't matched")
                        else:
                            st.error("Username doesn't exist")
                    except psycopg2.Error as e:
                        st.error(f"Error executing sql commands: {e}")
                    finally:
                        cursor.close()
   
if __name__=="__main__":
    s1 = Signup()
    s1.signin_page()