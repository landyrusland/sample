import streamlit as st
import pandas as pd

st.title("Aplikasi Analisis Data Sederhana")
uploaded_file = st.file_uploader("Unggah file CSV Anda", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data yang diunggah:", df.head())
    st.line_chart(df.select_dtypes(include=['number']))
