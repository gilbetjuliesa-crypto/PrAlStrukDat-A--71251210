import streamlit as st

st.title("슫슬슭슮슯 Latihan Struktur Data Built-in: Kasir Minimarket")
st.markdown("""
Kasus barang pada **minimarket**. Silahkan menambah barang yang dijual!.
""")

# Tuple untuk SKU (id barang, nama barang)
produk_sku = (
    ("BRG001", "Roti Tawar"),
    ("BRG002", "Susu UHT"),
    ("BRG003", "Mi Instan"),
    ("BRG004", "Minyak Goreng"),
    ("BRG005", "Telur Ayam 1 Lusin"),
#silahkan tambahkan barang lainnya
)
# Dictionary: id -> dictionary detail produk
default_inventori = {
    "BRG001": {"nama": "Roti Tawar", "kategori": "Makanan", "harga": 18000, "stok": 20},
    "BRG002": {"nama": "Susu UHT", "kategori": "Minuman", "harga": 15000, "stok": 25},
    "BRG003": {"nama": "Mi Instan", "kategori": "Makanan", "harga": 3500, "stok": 100},
    "BRG004": {"nama": "Minyak Goreng", "kategori": "Bahan Pokok", "harga": 17000, "stok": 15},
    "BRG005": {"nama": "Telur Ayam 1 Lusin", "kategori": "Bahan Pokok", "harga": 27000, "stok": 10},
#sesuaikan dengan barang lain jika ditamhbahkan pada SKU
}


# masukan list default inventori dan sky disini
if "inventori" not in st.session_state:
    st.session_state["inventori"] = default_inventori.copy()
    inventori = st.session_state["inventori"]
else:
    inventori = st.session_state["inventori"]
if "transaksi" not in st.session_state:
    st.session_state["transaksi"] = default_inventori.copy()
if "transaksi" not in st.session_state["transaksi"]:
    st.session_state["transaksi"] = []
    transaksi = st.session_state["transaksi"]
else:
    transaksi = st.session_state["transaksi"]
st.table(inventori)
# List transaksi (bisa kosong di awal, pengguna menambah)
st.caption("**SKU tuple** ID dan nama produk.")
with st.expander("Lihat SKU (tuple) dan Inventori (dictionary)"):
    st.write("**Tuple SKU:**", produk_sku)
    st.write("**Inventori:**", inventori)

st.subheader("Tambah Transaksi Penjualan")
col_a, col_b, col_c = st.columns([2,2,1])
with col_a:
    sku_id = st.selectbox("Pilih SKU", options=[p[0] for p in produk_sku])
with col_b:
    qty = st.number_input("Qty", min_value=1, value=1, step=1)
with col_c:
    if st.button("Tambah"):
        if inventori[sku_id]["stok"] >= qty:
        # Kurangi stok
            inventori[sku_id]["stok"] -= qty
        # Catat transaksi
            transaksi.append({"id": sku_id, "nama": inventori[sku_id]["nama"],
"qty": int(qty)})
# Update session_state
            st.session_state["inventori"] = inventori
            st.session_state["transaksi"] = transaksi
            st.success(f"Barang berhasil ditransaksikan: {sku_id} x {qty}")
        else:
            st.error("Stok tidak mencukupi!")
                     
if transaksi:
    with st.expander("Lihat Daftar Transaksi"):
        st.table(transaksi)

if inventori:
    with st.expander("Lihat Daftar Inventori"):
        st.table(inventori)


