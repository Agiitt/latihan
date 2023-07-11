# operasi dan manipulasi string (part 1)

# 1. mwnyambung string (concatenate)
nama_pertama = "ucup"
nama_tenggah = "D"
nama_akhir = "fame"

nama_lengkap = nama_pertama + " " + nama_tenggah + "'" + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))
# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

d = "D"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print("string " + d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(10*"wk")

# indexing
print('index ke-0 :' + nama_lengkap[0])
print('index ke-6 :' + nama_lengkap[6])
print('index ke-(-1) :' + nama_lengkap[-1]) # angka mines menghitung dari belakang
print('index ke-[0:3] :' + nama_lengkap[0:4]) # huruf ketiga tidak dimasukkan jadi yang seharusnya "ucup" malah menjadi "ucu", jadi tambahakan satu angka untuk menambah batas
print('index ke-[3:7] :' + nama_lengkap[3:8])
print('index ke-[0,2,4,6,8,10] :' + nama_lengkap[0:11:2])


# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ascii code untuk spasi adalah " + str(ascii_code))
data = 177
print("char untuk ascii 177 adalah " + chr(data))

# 4. operator dalam benruk methode

data = "otong surotong parotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))