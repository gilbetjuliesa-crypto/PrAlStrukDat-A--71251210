
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import requests

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}

st.set_page_config(page_title="Dashboard Katalog Buku", layout="wide")
st.title("Dashboard Katalog Buku")
st.write("Mengambil data buku melalui web scraping dan kurs GBP/IDR melalui REST API.")

jumlah_halaman = st.slider("Jumlah halaman katalog yang diambil", 1, 3, 2)

if st.button("Ambil Data dan Tampilkan Dashboard", type="primary"):

    data = []

    for halaman in range(1, jumlah_halaman + 1):
        url = f"https://books.toscrape.com/catalogue/page-{halaman}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for buku in soup.select("article.product_pod"):
            data.append({
                "Judul": buku.h3.a["title"],
                "Harga_GBP": float(buku.select_one(".price_color").text.replace("£", "")),
                "Rating": RATING_MAP[buku.select_one(".star-rating")["class"][1]],
                "Ketersediaan": buku.select_one(".availability").text.strip()
            })

    # Mengambil kurs GBP ke IDR
    api = requests.get("https://api.frankfurter.dev/v1/latest?base=GBP&symbols=IDR")
    kurs = api.json()["rates"]["IDR"]

    # Membuat DataFrame
    df = pd.DataFrame(data)
    df["Harga_IDR"] = df["Harga_GBP"] * kurs

    st.success(f"Berhasil mengambil {len(df)} buku")
    st.dataframe(df)

    st.subheader("Visualisasi")
    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots()
        ax1.hist(df["Harga_IDR"], bins=10, color="skyblue", edgecolor="black")
        ax1.set_title("Distribusi Harga Buku (IDR)")
        ax1.set_xlabel("Harga Rupiah")
        ax1.set_ylabel("Jumlah Buku")
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots()
        rating = df["Rating"].value_counts().reindex([1, 2, 3, 4, 5], fill_value=0)
        ax2.bar(rating.index, rating.values, color="orange")
        ax2.set_title("Jumlah Buku Berdasarkan Rating")
        ax2.set_xlabel("Rating")
        ax2.set_ylabel("Jumlah Buku")
        ax2.set_xticks([1, 2, 3, 4, 5])
        st.pyplot(fig2)
