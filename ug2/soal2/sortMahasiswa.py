import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="nim",rev = False):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    key = maps[index] 
    n = len(data) 
    
    for i in range(n - 1): 
        for j in range(n - i - 1): 
            nilai_kiri = data[j][key] 
            nilai_kanan = data[j + 1][key] 
            
            if not rev:
                harus_tukar = nilai_kiri > nilai_kanan 
            else:
                harus_tukar = nilai_kiri < nilai_kanan  
            
            if harus_tukar:
                data[j], data[j + 1] = data[j + 1], data[j]  
    
    # Jangan Dihapus
    show_data(data)

sort_by(data, "")


    
