data = [38, 12, 27, 43, 9, 31, 18, 25]
print("Data Awal: ", data)

mid = len(data) // 2
left = data[:mid]
right = data[mid:]
print("Left :", left)
print("Right:", right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

sorted_data = merge_sort(data)
print("Data Setelah Merge Sort: ", sorted_data)