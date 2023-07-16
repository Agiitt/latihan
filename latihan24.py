# perulangan (loop)

# for kondisi:
#       aksi

# ini dengan list
angka2 = [0,2,3,4,6,8,10] #ini adalah list
print(angka2)
for i in angka2:
    print(f"i sekarang -> {i}")

print("akhir dari program 1\n")

# ini adalah range
angka = range(5) # mulain dari angka 0 sampai 4

for i in angka:
    print(f"i sekarang -> {i}")
    
print("akhir dari program 2\n")


angka = range(1,5) # mulai dari 1 sampai 5

for i in angka:
    print(f"i sekarang -> {i}") # contoh dalam angka
    print(f"saya mager {i}") # contoh dalah kalimat

print("akhir dari program 3\n")

# menggunakan string

data_str = "saya mager abis"

for huruf in data_str: # menampilkan huruf satu persatu kearah bawah
    print(huruf)

print("akhir dari program 4\n")


