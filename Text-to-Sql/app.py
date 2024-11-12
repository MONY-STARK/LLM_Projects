
from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt, question])
    return response.text.strip()  # Strip extra whitespace/newlines from the response

def read_sql_query(sql, db):
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        
        # Directly execute the query without modifying it
        cursor.execute(sql)
        rows = cursor.fetchall()
        connection.commit()
        connection.close()
        
        for row in rows:
            print(row)
        return rows


prompt = [
    """
    you are expert in converting english to sql code!
    the sql database has the name students database within it , it has the table name student with the following column - name, class, section
    for example \n example 1 - how many entries of the record are present?
    the sql command will be something like this select count(*) from students ; 
    \n example 2 - Tell me how many student are in my datascience class
    the sql command will be something like this select * from students where class = 'data'; 
    also the sql code should not have --- in begining or end or sql word in output
    """
]
st.set_page_config(page_title="Retrieve data using texts")

st.header("SQL Retriever using Gemini Model")

question = st.text_input("Input: ", key="input")

submit = st.button("Get data")

if submit:
    response = get_gemini_response(question, prompt[0])
    print(f"Generated SQL Query: {response}")  # Debug the generated SQL query
    
    # Check if the query is already valid, and execute it directly
    response = read_sql_query(response, "students.db")
    
    st.subheader("Response is")
    for r in response:
        st.header(r)

