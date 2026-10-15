foo = { 1: "Belajar", 
        2: "Python", 
        3: "di Struktur Data" 
}
bar = {"mengapa": "Belajar", "apa": "Python", "dimana": "di Struktur Data"}
baz = { 1: "Belajar", "apa": "Python", "dimana": "di Struktur Data" }
print(type(foo))
print(type(bar))
print(type(baz))
print(foo)
print(bar)
print(baz)

foo["wooo"] = 123
foo[1] = 234567
del foo[1]
print(foo["wooo"])
print(foo)