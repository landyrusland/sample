import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Penjualan")
st.title("📊 Dashboard Analisis Penjualan")

# Simulasi data jika belum ada file
data = {
    'Produk': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Terjual': [15, 80, 45, 20],
    'Keuntungan': [1500, 400, 900, 1200]
}
df = pd.DataFrame(data)

# Sidebar untuk filter
st.sidebar.header("Filter Data")
pilihan = st.sidebar.multiselect("Pilih Produk", df['Produk'].unique(), default=df['Produk'].unique())

df_filtered = df[df['Produk'].isin(pilihan)]

# Menampilkan Grafik
col1, col2 = st.columns(2)
with col1:
    st.subheader("Jumlah Terjual")
    st.bar_chart(df_filtered.set_index('Produk')['Terjual'])
with col2:
    st.subheader("Tabel Data")
    st.dataframe(df_filtered)