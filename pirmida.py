def piramida_angka(x):
    for y in range(1, x + 1):
        print(" " * (x - y), end="")

        for z in range(1, y + 1):
            print(z, end="")

        for z in range(y - 1, 0, -1):
            print(z, end="")

        print()


piramida_angka(3)
