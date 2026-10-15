n=int(input("Masukan jumlah elemen yang akan diinputkan: "))
a=[]
for i in range(0,n):
    elem=int(input("Masukan element: "))
    a.append(elem)

avg=sum(a)/n
print("Rata-rata elements pada list adalah ",round(avg,2))


d={'A':1,'B':2,'C':3}
key=input("Masukan key yang ingin dicari:")

print(d.keys())
print(d.values())
print(d.items())

if key in d.keys():
    print("Key ditemukan, nilainya adalah :")
    print(d[key])
else:
    print("Key tidak ditemukan!")

