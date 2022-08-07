import streamlit as st
import mysql.connector
import pandas as pd
import requests

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from stock;")

# Print results.
for row in rows:
    st.write(f"There are {row[3]} {row[1]}s")
    if row[3] <= 0:
        url = 'https://notify-api.line.me/api/notify'
        token = 'An4nrpLh30uFvdyyBdscL6HAcI10v4mna7wIWpIzwOd'
        headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

        msg = f"{row[1]} out of stock"
        r = requests.post(url, headers=headers, data = {'message':msg})
        print (r.text)

if st.button('update'):
    run_query("UPDATE stock SET amount = amount - '1' WHERE id = '1' ")






