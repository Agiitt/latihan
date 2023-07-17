## operasi

# index  0(-3)  1(-2)   2(-1) ~~ jika angka minus terhitung dari akhir ke awal, sebaliknya angka positif dari awal ke akhir
data = ["ucup","otong","dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir (index -1) = {data_terakhir}")

data_ucup  = [-2]
print(f"data pertengahan (index -2) = {data_ucup}")

# mengambil info jumlah data list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## manipulasi data list

# menamahkan item pada list
print(f'data sebelum ditambah = \n{data}')
data.insert(1,"asep")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list
data.append("jajang")
print(f"data ditambah lagi = \n{data}")

# menambahakan list dengan list
data_baru = ["ujang", "usep", "dedeng"]
data.extend(data_baru)
print(f"data gabungan =\n{data}")

# menrubah data
# kita ubah data 2 menjadi micael
data[2] = "michael"
print(f'data rubah =\n{data}')

# menghapus data
data.remove("jajang")
print(f"data remove =\n{data}")
#data.remove("user") akan error karena huruf harus sesuai yaitu "asep"

# remove data paling belakang
data.pop()
print(f"data akhir = {data}")










