# a = 10, adalah variabel dengan 10

# tipe data: angka (integer)
i1 = 1
print("- data : ",i1,", bertipe : ", type(i1))

# type data: angka dengan koma (float)
i2 = 1.0
print("- data : ",i2,", bertipe : ", type(i2))

# type data: kumpulan karakter (string)
i3 = "saya ber10"
print("- data : ",i3,", bertipe : ", type(i3))

# type data: binary true/bool (boolean)
i4 = False
print("- data : ",i4,", bertipe : ", type(i4))

## tipe data khusus

# bilangan komplesk
datakomplec = complex(5,6)
print("- data : ",datakomplec,", bertipe : ", type(datakomplec))

# tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("- data : ",data_c_double,", bertipe : ", type(data_c_double))













