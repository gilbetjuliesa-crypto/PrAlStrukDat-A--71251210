import random
from datetime import datetime 

data = [random.randint(1, 100) for _ in range(1000)]
print("data awal")
print(data)
print("================================================")
#selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
hasil_selection = selection_sort(data.copy())
print("Selection Sort :", data.datetime())
print("================================================")

#Bubble Sort 
def bubble_sort(arr):
    n = len(arr) #jumlah data arry 
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
hasil_bubble = bubble_sort(data.copy())
print("Bubble Sort :", hasil_bubble)
print("================================================")

#insert sort
def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j>=0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
hasil_bubble = insert_sort(data.copy())
print("Insert Sort :", hasil_bubble)
print("================================================")
            
    
        
        
           
    