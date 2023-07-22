'''default argumen'''

# def fungsi(argument):
# def fungsi(argumrnt = nilai defaultnya):

# contoh 1
def say_hi(nama = "karep mu lah"): # jadi jika say_hi tidak memiliki isi makan akan mengambil string yag berada disampingnya
    '''fungsi dengan default argument'''
    print(f"{nama}")

say_hi("agit")
say_hi()

# contoh 2
def sapa_dia(nama, pesan = "apa kabar"):
    '''fungsi dengan input biasa, dan satu default argument'''
    print(f"hai {nama}, {pesan}")

sapa_dia("agit", "hai bobrok")
sapa_dia("agit")

# contoh 3
def hitung_pangkat(angka, pangkat=3):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
#hasil = hitung_pangkat(pangkat=3, 5) akan error
print(hasil)

# contoh 4
def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))






