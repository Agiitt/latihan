data_angka = [1,3,4,6,4,3,2,1,5,7,3,1,4,3]

print(f"data angka = \n{data_angka}")

# count data

jumlah_data_3 = data_angka.count(3)
jumlah_data_4 = data_angka.count(4)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["ucup","otong","ujang","dudung"]

print(f"data = {data}")

index_dudung = data.index("dudung")
index_ujang = data.index("ujang")

print(f"index si dudung = {index_dudung}")
print(f"index si ujang = {index_ujang}")

#data.index("usep") error terjadi karena tidak ditemukan usep dalam posisi data index 

# mengurutkan list
print(f"data angka sebelum diurutkan = {data_angka}")
data_angka.sort()
print(f"data angka sort = {data_angka}")

data.sort()
print(f"data string sort = {data}")

# balik list
data_angka.reverse()
print(f"data angka reverse = {data_angka}")

data.reverse()
print(f"data string reverse = {data}")






