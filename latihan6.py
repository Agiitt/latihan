# Belajar Casting
# merubah dari satu tipe ke tipe lain
# tipe daa = int, float, str, bool

## INTEGER
print("====integer")
data_int = 9
print("data = ", data_int, "type =",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data = ", data_float, "type =",type(data_float))
print("data = ", data_str, "type =",type(data_str))
print("data = ", data_bool, "type =",type(data_bool))

## FLOAT
print("====float")
data_float = 9.8
print("data = ", data_float, "type =",type(data_float))

data_int = int(data_float)# akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai float = 0
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_str, "type =",type(data_str))
print("data = ", data_bool, "type =",type(data_bool))

## BOOLEAN
print("====BOOLEAN")
data_bool = False
print("data = ", data_bool, "type =",type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool) # akan berubah menjadi teks biasa
data_float = float(data_bool)
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_str, "type =",type(data_str))
print("data = ", data_float, "type =",type(data_float))

## STRING
print("====STRING====")
data_str = "False"
print("data = ", data_str, "type =",type(data_str))

data_int = int(data_str) # string harus angka
data_float = float(data_float) # string harus angka
data_bool = bool(data_bool) # false jika kosong (tidak ada kalimat dalam tanda kutip)
print("data = ", data_int, "type =",type(data_int))
print("data = ", data_bool, "type =",type(data_bool))
print("data = ", data_float, "type =",type(data_float))
