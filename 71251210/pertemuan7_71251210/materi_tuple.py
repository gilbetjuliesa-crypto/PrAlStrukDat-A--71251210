foo = ("Python", 200, 6.99, True, 'Struktur Data', 99j)
print(foo[0])
print(foo[1])
print(foo[2])
print(foo[2:5])
print(foo[:3])
print(foo[3:])
print(foo[:])

foo = list(foo)
foo.append(5)
foo = tuple(foo)
foo[1] = "naruto"
del foo["python"]
foo.insert(0, "naruto") 
print(foo)