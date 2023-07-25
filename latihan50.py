''' *args '''

# masukkan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat badannya {berat}")

fungsi("ucup",178,40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0] 
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat badannya {berat}")
    
fungsi(["otong",100,120])

# kenalan dengan *args

def fungsi(*args):
    nama = args[0] 
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat badannya {berat}")

fungsi("dadang",120,120)

# studi kasus

def tambah(*data):
    # data tipenya adalah tuple, dia bisa diiterasi
    output = 0
    for angka in data:
        output += angka
    
    return output

hasil = tambah(1,2)
print(f"hasil = {hasil}")

hasil = tambah(12,13,14,15,16)
print(f"hasil = {hasil}")

































