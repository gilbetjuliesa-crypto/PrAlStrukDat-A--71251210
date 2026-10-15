nilai_ujian = [80,75,70,90,81,84,92,71,65,80,70]
nama_pahlawan = ['Sukarno', 'Diponegoro', 'Jend. Sudirman', 'Cut Nya Dhien']
nilai_campuran = ['Javascript', 20, 34.4, True]
list_dalam_list = [23, [22, 20], 45] 

nilai_ujian.append(10)
print(nilai_ujian)

nilai_ujian.insert(0, 9)
print(nilai_ujian)

nilai_ujian[0] = 100
print(nilai_ujian)

del nilai_ujian[0]
print(nilai_ujian)

nilai_ujian.extend(list_dalam_list)
print(nilai_ujian)

print(list_dalam_list)

print(list_dalam_list[1][1])

list_baru = [[10], [1], [2], [3]]
for i in list_baru:
    
    for j in i:
        print(i)
        
