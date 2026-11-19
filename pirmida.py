import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# Konversi rating teks menjadi angka
RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Katalog Buku",
    layout="wide"
)

st.title("Dashboard Katalog Buku")
st.write(
    "Mengambil data buku melalui web scraping "
    "dan mengonversi harga GBP ke IDR."
)

# Slider jumlah halaman
jumlah_halaman = st.slider(
    "Jumlah halaman katalog yang diambil",
    1, 3, 2
)

# Tombol mengambil data
if st.button("Ambil Data dan Tampilkan Dashboard", type="primary"):

    try:
        # 1. Web Scraping
        daftar_buku = []

        with st.spinner("Sedang mengambil data buku..."):

            for halaman in range(1, jumlah_halaman + 1):

                url = (
                    f"https://books.toscrape.com/catalogue/"
                    f"page-{halaman}.html"
                )

                response = requests.get(url, timeout=20)
                response.raise_for_status()

                soup = BeautifulSoup(
                    response.text,
                    "html.parser"
                )

                buku_list = soup.select("article.product_pod")

                for buku in buku_list:

                    # Judul buku
                    judul = buku.h3.a["title"]

                    # Harga GBP
                    harga_text = buku.select_one(
                        ".price_color"
                    ).get_text(strip=True)

                    harga_gbp = float(
                        harga_text.replace("£", "").replace("Â", "")
                    )

                    # Rating
                    rating_class = buku.select_one(
                        ".star-rating"
                    )["class"]

                    rating_teks = rating_class[1]
                    rating = RATING_MAP[rating_teks]

                    # Ketersediaan buku
                    ketersediaan = buku.select_one(
                        ".availability"
                    ).get_text(strip=True)

                    daftar_buku.append({
                        "Judul Buku": judul,
                        "Harga GBP": harga_gbp,
                        "Rating": rating,
                        "Ketersediaan": ketersediaan
                    })

        # 2. Mengambil kurs GBP ke IDR
        with st.spinner("Mengambil kurs GBP ke IDR..."):

            kurs_url = (
                "https://api.frankfurter.dev/v1/latest"
                "?base=GBP&symbols=IDR"
            )

            kurs_response = requests.get(
                kurs_url,
                timeout=20
            )

            kurs_response.raise_for_status()

            data_kurs = kurs_response.json()
            kurs_gbp_idr = data_kurs["rates"]["IDR"]

        # 3. Mengolah Data
        df = pd.DataFrame(daftar_buku)

        df["Harga IDR"] = (
            df["Harga GBP"] * kurs_gbp_idr
        )

        st.success(
            f"Berhasil mengambil {len(df)} buku!"
        )

        # Informasi jumlah buku dan kurs
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Jumlah Buku",
                len(df)
            )

        with col2:
            st.metric(
                "Kurs GBP ke IDR",
                f"Rp {kurs_gbp_idr:,.2f}"
            )

        # 4. Menampilkan Tabel Data
        st.subheader("Data Katalog Buku")

        st.dataframe(
            df.style.format({
                "Harga GBP": "£{:.2f}",
                "Harga IDR": "Rp {:,.2f}"
            }),
            use_container_width=True
        )

        # 5. Visualisasi
        st.subheader("Visualisasi Data")

        col1, col2 = st.columns(2)

        # Grafik Histogram
        with col1:

            st.write("Distribusi Harga Buku (IDR)")

            fig1, ax1 = plt.subplots()

            ax1.hist(
                df["Harga IDR"],
                bins=10,
                edgecolor="black"
            )

            ax1.set_xlabel("Harga (IDR)")
            ax1.set_ylabel("Jumlah Buku")
            ax1.set_title("Histogram Harga Buku")

            st.pyplot(fig1)
            plt.close(fig1)

        # Grafik Bar Chart
        with col2:

            st.write("Jumlah Buku Berdasarkan Rating")

            jumlah_rating = (
                df["Rating"]
                .value_counts()
                .reindex([1, 2, 3, 4, 5], fill_value=0)
                .sort_index()
            )

            fig2, ax2 = plt.subplots()

            ax2.bar(
                jumlah_rating.index,
                jumlah_rating.values
            )

            ax2.set_xlabel("Rating")
            ax2.set_ylabel("Jumlah Buku")
            ax2.set_title("Jumlah Buku per Rating")
            ax2.set_xticks([1, 2, 3, 4, 5])

            st.pyplot(fig2)
            plt.close(fig2)

    except requests.exceptions.RequestException as e:
        st.error(f"Gagal mengambil data dari website/API: {e}")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
