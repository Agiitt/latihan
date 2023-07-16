# continue, pass, break

# pass -> berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass # ini tidak di eksekusi

    print(angka)

# continue

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("nise")
        continue # akan membuat loop meloncat ke awal dan meloncati aksi yang berada dibawah continue
    print("hallo")

print("finish")