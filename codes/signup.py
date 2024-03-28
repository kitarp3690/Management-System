import streamlit as st
import psycopg2
import hashlib

class Signup:
    def __init__(self):
        pass
    
    def start_connection(self):
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
        hashed_password=hashlib.sha256(password.encode()).hexdigest()
        return hashed_password
    
    def check_user_existence(self,usname):
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
                    except psycopg2.Error as e:
                        st.error(f"Error executing sql commands: {e}")
                    finally:
                        cursor.close()
   
if __name__=="__main__":
    s1 = Signup()
    s1.signup_page()