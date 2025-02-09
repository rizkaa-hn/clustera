import mysql.connector
import streamlit as st

def connect_to_app_database():
    try:
        conn = mysql.connector.connect(
            host=st.secrets["database"]["host"],
            user=st.secrets["database"]["user"],
            password=st.secrets["database"]["password"],
            database=st.secrets["database"]["database"],
            auth_plugin='mysql_native_password'
        )
        print("Connected to the database successfully.")
        return conn
    except mysql.connector.Error as e:
        st.error(f"Error connecting to application database: {e}")
        return None
