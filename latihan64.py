## Tutorial membaca file eksternal

print(3*"=", " Membaca file txt ", 3*"=")
file = open("latihan64.txt",mode="r") # "r" read "w" write
 
print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

## baca seluruh file
print(file.read())

## baca per baris
# print(file.readline(),end="") # baca baris pertama, fungsi "end=""" adalah menghapus "\n" pada akhir baris 
# print(file.readline(),end="") # baca baris kedua

## baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah diclose : {file.closed}")
file.close() # swtiap kali membuka file harus ditutup menggunakan command disamping
print(f"apakah file sudah diclose : {file.closed}")


## salah satu teknik membuka file di python yang manjur

print("\n",3*"=", " Membaca file txt dengan with", 3*"=")

with open("latihan64.txt",mode="r") as file: # "with" dengan saat ini dibuka(open("latihan64.txt",mode="r")) yang dipanggil sebagai/alias(as) file: apa yang akan kita lakukan
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah diclose : {file.closed}")

print(f"apakah file sudah diclose : {file.closed}")