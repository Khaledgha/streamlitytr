import streamlit as st
import pandas as pd

st.title('CSV File Viewer')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.write("Data from the CSV file:")
    st.dataframe(data)

    # Example of a simple filter
    if st.checkbox('Show only selected columns'):
        all_columns = data.columns.tolist()
        selected_columns = st.multiselect("Select columns", all_columns, all_columns[0])
        new_df = data[selected_columns]
        st.dataframe(new_df)

    # Example of a simple chart
    if st.button('Show Chart'):
        st.line_chart(data)
