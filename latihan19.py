# With and Multiline

# data

data_nama = "ucup"
data_umur = 17
data_tinggi = 160
data_nomor_sepatu = 44

#string standar
data_str = f"nama = {data_nama}, umut = {data_umur}, tinggi = {data_tinggi}, data nomer sepatu = {data_nomor_sepatu}"
print(5*"="+("data string")+"="*5)
print(data_str)

# string multiline (dengan menggunakan enter, newline,) \n
data_str = f"nama = {data_nama}, \numut = {data_umur}, \ntinggi = {data_tinggi}, \ndata nomer sepatu = {data_nomor_sepatu}"
print("\n"+5*"="+("data string")+"="*5)
print(data_str)

# string multiline (kutip triplest)

data_str = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
no_sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+("data string")+"="*5)
print(data_str)

# mengatur lebar
data_str = f"""
nama = {data_nama}
umur = {data_umur:>10} 
tinggi = {data_tinggi:>10}
no_sepatu = {data_nomor_sepatu}
""" # fungsi ">10" merapatkan kata ke kanan
print("\n"+5*"="+("data string")+"="*5)
print(data_str)


