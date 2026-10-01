import streamlit as st
import pandas as pd

st.header("Kalkulator Proyeksi Dana Pensiun")

st.subheader("Usia sekarang dan usia pensiun")
usia_sekarang = st.slider("Usia sekarang:", min_value=0, max_value=120, value=19)
usia_pensiun = st.slider("Usia pensiun:", min_value=usia_sekarang, max_value=120, value=55)

st.subheader("Dana awal dan kontribusi bulanan")
dana_awal = st.number_input("Dana awal:", min_value=0, value=0)
kontribusi_bulanan = st.number_input("Kontribusi bulanan:", min_value=0, value=1000000)

st.subheader("Tingkat pengembalian investasi (%):")
tingkat_pengembalian = st.number_input("Tingkat pengembalian:", min_value=0.0, value=5.0)

if st.button("Hitung!", type="primary"):

    jumlah_tahun = usia_pensiun - usia_sekarang
    dana_pensiun = dana_awal

    daftar_usia = []
    daftar_dana = []

    for i in range(jumlah_tahun):
        dana_pensiun = dana_pensiun + kontribusi_bulanan * 12
        dana_pensiun = dana_pensiun * (1 + tingkat_pengembalian / 100)

        daftar_usia.append(usia_sekarang + i + 1)
        daftar_dana.append(dana_pensiun)

    st.metric(label="Proyeksi dana pensiun Anda adalah:", value=f"{dana_pensiun:,.2f}")

    df = pd.DataFrame({
        "Tahun ke-": range(1, jumlah_tahun + 1),
        "Usia": daftar_usia,
        "Dana Pensiun": daftar_dana
    })

    st.subheader("Grafik Perkembangan Dana Pensiun")
    st.line_chart(df, x="Usia", y="Dana Pensiun")

    st.subheader("Tabel Perkembangan Dana Pensiun")
    st.dataframe(df)
