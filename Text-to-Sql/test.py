
from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

connection = sqlite3.connect("students.db")
cursor = connection.cursor()
        
# Directly execute the query without modifying it
cursor.execute("Select * from students")
rows = cursor.fetchall()
connection.commit()
connection.close()
        
for row in rows:
    print(row)



connection.close()