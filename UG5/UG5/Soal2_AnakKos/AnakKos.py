import streamlit as st
import pandas as pd

# --- Title ---
st.header("Pengelujaran Anak Kost: 71251210")


# --- Input Uang Bulanan ---
st.subheader("Uang Bulanan")
dana_awal = st.number_input("Masukan Uang Bulanan:", value=None, placeholder="type a number")

# --- Input Pengeluaran ---
st.subheader("Pengeluaran Bulanan")
makanan = st.number_input("pengeluaran untuk makan: ", value=None, placeholder="Masukan pengeluaran untuk makan: ")
kos = st.number_input("penegeluaran untuk kos: ", value=None, placeholder="Masukan penegeluaran untuk kos: ")
transportasi = st.number_input("penegeluaran untuk transportasi: ", value=None, placeholder="Masukan penegeluaran untuk transportasi: ")
internet = st.number_input("penegeluaran untuk internet: ", value=None, placeholder="Masukan penegeluaran untuk internet: ")
hiburan = st.number_input("penegeluaran untuk hiburan: ", value=None, placeholder="Masukan penegeluaran untuk hiburan: ")

# --- Tombol Ngitung Pengeluaran ---
if st.button("hitung pengeluaran"): # if jangan dihapus, cuman nambahin tombol disini 

    # --- Ngitung Total Pengeluaran ---
    total_pengeluaran = makanan + kos + transportasi + internet + hiburan

    # --- Ngitung Sisa Uang ---
    sisa_uang = dana_awal - total_pengeluaran 


    # --- Menampilkan Hasil Perhitungan ---
    st.subheader("Ringkasan Keuangan")
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.metric(
            # Tampilin uang bulanan di sini
            "Uang Bulanan", dana_awal
        )
    with kolom2:
        st.metric(
            # Tampilin total pengeluaran di sini
            "Total pengeluaran", total_pengeluaran
        )
    with kolom3:
        st.metric(
            # Tampilin sisa uang di sini
            "Sisa Uang", sisa_uang
        )


    # --- Kondisi Keuangan ---
    st.subheader("Kondisi Keuangan")

    # Kondisi 1
    if sisa_uang > 0:
        st.success("keuanganmu masih aman bulan ini!")
        

    # Kondisi 2
    elif sisa_uang == 0:
        st.warning("uangmu habis")

    # Kondisi 3
    else:
        st.error("pengeluaranmu melebihi batas")


    # --- Data Pengeluaran ---
    # Ini gausah diubah! 
    # Udah kubantu bikinin, tinggal dipake aja
    data_pengeluaran = {
        "Kategori": [
            "Makanan",
            "Kos",
            "Transportasi",
            "Internet/Pulsa",
            "Hiburan"
        ],
        "Pengeluaran": [
            makanan,
            kos,
            transportasi,
            internet,
            hiburan
        ]
    }

    df_pengeluaran = pd.DataFrame(data_pengeluaran)

    # --- Pengeluaran Terbesar ---
    # Cari pengeluaran terbesar
    pengeluaran_terbesar = ()
    nilai_terbesar = max(
        makanan,
        kos,
        transportasi,
        internet,
        hiburan
    )
    if makanan == nilai_terbesar:
        pengeluaran_terbesar.append("makanan")
    if kos == nilai_terbesar:
        pengeluaran_terbesar.append("kos")
    if transportasi == nilai_terbesar:
        pengeluaran_terbesar.append("transportasi")
    if internet == nilai_terbesar:
        pengeluaran_terbesar.append("internet")
    if hiburan == nilai_terbesar:
        pengeluaran_terbesar.append("hiburan")


    st.subheader("Pengeluaran Terbesar")
     # Tampilin pengeluaran terbesar di sini
    st.write("Pengeluaran terbesar anda: ", pengeluaran_terbesar)

    # --- Grafik Pengeluaran ---
    st.subheader("Grafik Pengeluaran")
    st.bar_chart(df_pengeluaran)
    # Tampilin grafik pengeluaran di sini