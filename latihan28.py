# latihan perulangan membuat segitiga

sisi = 10

# 1. menggunakan For

# dummy variable
print("awal dari for")

count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print("akhir dari for\n")

# 2. menggunakan while

print("awal dari while")

count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break


print("akhir dari while\n")

# 3. hanya ganjil saja

print("awal dari while ganjil")

count = 1
while True:
    if (count%2):
        # print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break


print("akhir dari while ganjil\n")

# 4. hanya ganjil saja

print("awal dari while ganjil")

count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        # print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break


print("\nakhir dari while ganjil\n")

# 5. hanya ganjil saja (tugas) *ngikut orang

print("awal dari while ganjil")

for i in range(0, 5):
    print(" " * (5 - i), end = "")
    for x in range(i):
        print("+ ", end = "")

    print()
for i in range(5, 0, -1):
    print(" "*(5-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()

print("\nakhir dari while ganjil\n")







