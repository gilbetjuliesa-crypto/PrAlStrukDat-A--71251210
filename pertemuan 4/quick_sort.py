data = [38, 12, 27, 43, 9, 31, 18, 25]
print("Data Awal: ", data)

pivot = data[-1]
print("Pivot ", pivot)

left = []
right = []
for x in data[:-1]:
    if x < pivot:
        left.append(x)
    else:
        right.append(x)
print("Left :", left)
print("Pivot :", pivot)
print("Right :", right)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []
    for x in arr[:-1]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)
datamerge = quick_sort(data)
print("Data Setelah Quick Sort: ", datamerge) 