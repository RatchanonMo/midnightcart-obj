import streamlit as st
import pandas as pd

# DB
import sqlite3
conn = sqlite3.connect('data/data.sqlite')
c = conn.cursor()

# Fxn make Execution
def sql_executor(raw_code):
    c.execute(raw_code)
    data = c.fetchall()
    return data


def main():
    st.title("SQLPlayground");
   

    col1,col2 = st.columns(2)

    with col1:
        with st.form(key='query_form'):
            raw_code = st.text_area("SQL Code Here")
            submit_code = st.form_submit_button("Execute")

        # Test
        fetch = "SELECT * FROM stock "
        all = sql_executor(fetch)
        st.dataframe(all)

        if st.button("- ppl"):
            sql_executor("UPDATE stock  SET amount = '100' WHERE id = '1' ")
        
        
    
    # Results Layouts
    with col2:
        if submit_code:
            st.info("Query Submitted")
            st.code(raw_code)

            # Result 
            query_results = sql_executor(raw_code)
            with st.expander("Result"):
                    st.write(query_results)
            with st.expander("Pretty Table"):
                    query_df = pd.DataFrame(query_results)
                    st.dataframe(query_df)


if __name__ == '__main__':
    main()
