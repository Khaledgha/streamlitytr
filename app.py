import streamlit as st
import pandas as pd
import requests
from io import BytesIO

st.title('Large File Processor')

# User inputs the download link
file_url = st.text_input("Enter the URL of the CSV file")

if file_url:
    # Downloading the file
    st.write("Downloading the file...")
    response = requests.get(file_url)
    response.raise_for_status()

    # Assume the file is a CSV
    data = pd.read_csv(BytesIO(response.content))
    st.write(data)

    # Example of a simple filter
    if st.checkbox('Show only selected columns'):
        all_columns = data.columns.tolist()
        selected_columns = st.multiselect("Select columns", all_columns, all_columns[0])
        new_df = data[selected_columns]