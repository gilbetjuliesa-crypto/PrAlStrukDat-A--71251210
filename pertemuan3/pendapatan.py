produk = [
 {"nama": "Headset", "harga": 150000, "stok": 12},
 {"nama": "Mouse", "harga": 85000, "stok": 25},
 {"nama": "Keyboard", "harga": 250000, "stok": 8},
 {"nama": "Webcam", "harga": 200000, "stok": 15},
 {"nama": "Flashdisk", "harga": 75000, "stok": 30}
]
print("=============================================================")
print("Data Awal Produk yang dimiliki perusahaan:")
for item in produk:
    print(item["nama"], item["harga"])
def bubble_sort(produk):
    n = len(produk)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if produk[j]["harga"] > produk[j + 1]["harga"]:
                produk[j], produk[j + 1] = produk[j + 1], produk[j]
    return produk
print("=====================")
print("Hasil Pengurutan berdasarkan Harga dengan Bubble Sort")
hasil_bubble = bubble_sort(produk.copy())
for item in hasil_bubble:
    print(item["nama"], item["harga"]) 
print("=============================================================")

def selection_sort(produk):
    n = len(produk)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if produk[j]["nama"] < produk[min_index]["nama"]:
                min_index = j
        produk[i], produk[min_index] = produk[min_index], produk[i]
    return produk
print("\nHasil Pengurutan berdasarkan Nama dengan Selection Sort")
hasil_selection = selection_sort(produk.copy()) 
for item in hasil_selection:
    print(item["nama"], item["harga"])
print("=============================================================")

def insertion_sort(produk):
    n = len(produk)
    for i in range(1, n):
        key = produk[i]
        j = i - 1
        while j >= 0 and produk[j]["stok"] < key["stok"]:
            produk[j + 1] = produk[j]
            j -= 1
        produk[j + 1] = key
    return produk
print("\nHasil Pengurutan berdasarkan Nama dengan InsertionSort")
hasil_insertion = insertion_sort(produk.copy())
for item in hasil_insertion:
    print(item["nama"], item["stok"])
print("=============================================================")

for item in produk:
    item['pendapatan'] = item['harga'] * item['stok']

def bubble_sort_pendapatan(produk):
    n = len(produk)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if produk[j]["pendapatan"] > produk[j + 1]["pendapatan"]:
                produk[j], produk[j + 1] = produk[j + 1], produk[j]
    return produk

print("\nHasil Pengurutan berdasarkan Pendapatan dengan Bubble Sort (Ascending)")
hasil_pendapatan = bubble_sort_pendapatan(produk.copy())
for item in hasil_pendapatan:
    print(f"{item['nama']} - Pendapatan: Rp {item['pendapatan']:,}")
print("=============================================================")
    