buku = [
    {"judul": "Algoritma Pemrograman", "tahun": 2022, "penulis": "Andi Wijaya", "stok": 5},
    {"judul": "Basis Data", "tahun": 2020, "penulis": "Andi Wijaya", "stok": 3},
    {"judul": "Pemrograman Python", "tahun": 2023, "penulis": "Tono Pratama", "stok": 7},
    {"judul": "Struktur Data", "tahun": 2021, "penulis": "Rina Putri", "stok": 4},
    {"judul": "Jaringan Komputer", "tahun": 2019, "penulis": "Andi Wijaya", "stok": 2},
    {"judul": "Rekayasa Perangkat Lunak", "tahun": 2022, "penulis": "Deni Kurniawan", "stok": 6},
    {"judul": "Sistem Operasi", "tahun": 2020, "penulis": "Maya Sari", "stok": 3},
    {"judul": "Kecerdasan Buatan", "tahun": 2024, "penulis": "Tono Pratama", "stok": 5}
]


def merge_penulis(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["penulis"] > right[j]["penulis"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort_penulis(buku):
    if len(buku) <= 1:
        return buku

    mid = len(buku) // 2

    left = buku[:mid]
    right = buku[mid:]

    left = merge_sort_penulis(left)
    right = merge_sort_penulis(right)

    return merge_penulis(left, right)


hasil_merge = merge_sort_penulis(buku.copy())

print("Merge Sort berdasarkan penulis Z-A")

for item in hasil_merge:
    print(
        f'{item["penulis"]:<20} '
        f'{item["judul"]:<30} '
        f'{item["tahun"]} '
        f'Stok: {item["stok"]}'
    )


def quick_sort_tahun(buku):
    if len(buku) <= 1:
        return buku

    pivot = buku[-1]

    left = []
    right = []

    for item in buku[:-1]:
        if item["tahun"] > pivot["tahun"]:
            left.append(item)
        else:
            right.append(item)

    return quick_sort_tahun(left) + [pivot] + quick_sort_tahun(right)


hasil_quick = quick_sort_tahun(buku.copy())

print("\nQuick Sort berdasarkan tahun terbaru-terlama")

for item in hasil_quick:
    print(
        f'{item["tahun"]} '
        f'{item["judul"]:<30} '
        f'{item["penulis"]:<20} '
        f'Stok: {item["stok"]}'
    )


def merge_penulis_tahun(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["penulis"] < right[j]["penulis"]:
            result.append(left[i])
            i += 1

        elif left[i]["penulis"] > right[j]["penulis"]:
            result.append(right[j])
            j += 1

        else:
            if left[i]["tahun"] <= right[j]["tahun"]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort_penulis_tahun(buku):
    if len(buku) <= 1:
        return buku

    mid = len(buku) // 2

    left = buku[:mid]
    right = buku[mid:]

    left = merge_sort_penulis_tahun(left)
    right = merge_sort_penulis_tahun(right)

    return merge_penulis_tahun(left, right)


hasil_penulis_tahun = merge_sort_penulis_tahun(buku.copy())

print("\nUrut berdasarkan penulis dan tahun ascending")

for item in hasil_penulis_tahun:
    print(
        f'{item["penulis"]:<20} '
        f'{item["tahun"]} '
        f'{item["judul"]:<30} '
        f'Stok: {item["stok"]}'
    )