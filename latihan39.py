# operator directory

data_dict = {
    'cp':'ucup',
    'tg':'tongtong',
    'jan':'marjan'

}

# panjang direcroty
LENDICT = len(data_dict)
print(f"panjang direrectory: {LENDICT}")

# mengecek ket atau tidak
KEY = "cp"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cp"])
# print(data_dict["kis"]) error
print(data_dict.get("cp"))
print(data_dict.get("kis","key tidak dapat ditemukan")) # terbaik, cek key dengan massage key tidak diemukan

# mengupdate data
data_dict["cp"] = "ucuo karum"
print(data_dict)
data_dict["tg"] = "totong barontong"
print(data_dict)

data_dict.update({"cp":"ucup"})
print(data_dict)
data_dict.update({"agt":"masuk"}) # kalau tidak ada ditambah, jadi fungsi update ini fungsinya ada dua yaitu mengupdate dan menambah
print(data_dict)

# menghapus/delete data pada dictionery
del data_dict["agt"]
print(data_dict)
















