# Data mahasiswa dan 5 nilai UG
mahasiswa = [
    {"nama": "Andi", "nilai": [80, 75, 90, 70, 85]},
    {"nama": "Budi", "nilai": [60, 65, 70, 55, 60]},
    {"nama": "Citra", "nilai": [90, 85, 95, 88, 92]},
    {"nama": "Deni", "nilai": [70, 75, 65, 72, 68]},
    {"nama": "Eka", "nilai": [85, 80, 78, 90, 87]},
    {"nama": "Fajar", "nilai": [65, 70, 68, 60, 72]},
    {"nama": "Gina", "nilai": [88, 92, 85, 90, 87]},
    {"nama": "Hadi", "nilai": [75, 80, 70, 78, 72]},
    {"nama": "Intan", "nilai": [55, 60, 65, 58, 62]},
    {"nama": "Joko", "nilai": [78, 82, 75, 80, 85]}
]


# Menghitung rata-rata nilai setiap mahasiswa
for rata_rata_mahasiswa in mahasiswa:
    rata_rata_mahasiswa["rata-rata"] = sum(rata_rata_mahasiswa["nilai"]) / len(rata_rata_mahasiswa["nilai"])


# Divide and Conquer - Merge Sort
def merge_sort(data):
    if len(data) <= 1:  
        return data 
    
    mid = len(data) // 2 
    left = data[:mid]  
    right = data[mid:]

    left = merge_sort(left)  
    right = merge_sort(right)

    return merge(left, right)

def merge(kiri, kanan):
    result = []
    i = 0
    j = 0 
    while i < len(kiri) and j < len(kanan):  
        if kiri[i]["rata-rata"] >=  kanan[j]["rata-rata"]:  
            result.append(kiri[i])
            i += 1  
        else:  
            result.append(kanan[j])  
            j += 1

    while i < len(kiri):
        result.append(kiri[i])
        i += 1 

    while j < len(kanan):
        result.append(kanan[j])
        j += 1 

    return result


# Menghitung rata-rata keseluruhan
total_rata2 = 0
for rata_rata_mahasiswa in mahasiswa:
    total_rata2 += rata_rata_mahasiswa["rata-rata"]

rata_k = total_rata2 / len(mahasiswa)


# Mengurutkan mahasiswa menggunakan Merge Sort
mahasiswa_urut = merge_sort(mahasiswa)
atas = []
bawah = []

for rata_rata_mahasiswa in mahasiswa_urut:
    if rata_rata_mahasiswa["rata-rata"] >= rata_k:
        atas.append(rata_rata_mahasiswa)
    else:
        bawah.append(rata_rata_mahasiswa)

# Menampilkan hasil rata-rata keseluruhan
print("rata-rata keseluruhan: ", rata_k)

print("\n=== DI ATAS / SAMA DENGAN RATA-RATA ===")

# Tampilkan List di atas / sama dengan rata-rata
nomor = 1 
for rata_rata_mahasiswa in atas:
    print(
        nomor,
        ".",
        rata_rata_mahasiswa["nama"],
        "-nilai: ",
        rata_rata_mahasiswa["nilai"],
        "-Rata-rata: ",
        rata_rata_mahasiswa["rata-rata"]
    )
    nomor += 1

print("\n=== DI BAWAH RATA-RATA ===")

# Tampilkan List di bawah rata-rata
nomor = 1
for rata_rata_mahasiswa in bawah:
    print(
        nomor,
        ".",
        rata_rata_mahasiswa["nama"],
        "-nilai: ",
        rata_rata_mahasiswa["nilai"],
        "-Rata-rata: ",
        rata_rata_mahasiswa["rata-rata"]
    )
    nomor += 1
