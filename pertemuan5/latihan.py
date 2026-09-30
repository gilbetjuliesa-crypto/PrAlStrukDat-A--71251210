import streamlit as st
import qrcode

st.header("QR Code Generator")
data = st.text_input("URL:")
if st.button("Generate QR Code"):
    if data:
        qr = qrcode.make(data)
        qr.save("qrcode.png")
        st.image("qrcode.png")
    else:
        st.error("Please enter a valid URL to generate QR Code.")
