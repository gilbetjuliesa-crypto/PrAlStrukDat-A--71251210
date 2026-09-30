import streamlit as st

st.title("Demo Streamlit")
st.header("_streamlit_ is :red[easy] :heart_eyes:")

usia = st.slider("Berapa usia?", 0, 120, 15)

kategori = ""

if usia > 59:
    kategori = "lansia"
elif 18 <= usia <= 59:
    kategori = "Dewasa"
elif 13 <= usia <= 17:
    kategori = "remaja"
elif 6 <= usia <= 12:
    kategori = "anak anak"
else:
    kategori = "bayi dan balita"

nama = st.text_input("siapa nama anda?")
alamat = st.text_input("alamatmu dimana?")
data = st.text_input("URL:")
pesan = st.text_input("Tulis pesan:")
warna = st.color_picker("Pilih warna pesan:", "#000000")


if st.button("Kirim Pesan"):
    st.markdown(
        f"<h3 style='color:{warna};'>{pesan}</h3>",
        unsafe_allow_html=True
    )

