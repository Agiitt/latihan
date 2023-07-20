# looping dari list

# for loop
print("for loop\n")
kumpulan_angka = [1,4,5,6,8,5,3,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["ucup", 'otng',"karim","masup","rama"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("foor loop dan reange\n")
kumpulan_angka = [10,5,2,6,8,4]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

#while
print("\nwhile loop")
kumpulan_angka = [10,5,2,6,8,4]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehesion
print("\nlist comprehesion")
data = ["ucup",1,2,3,"otong"]

[print(f"data={i}") for i in data]

angka = [10,5,2,6,8,4]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\nenumerate")
data_list = ["ucup",1,2,3,"otong"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")













