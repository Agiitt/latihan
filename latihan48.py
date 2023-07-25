''' latihan fungsi'''

import os

# program menghitung luas dan keliling persegi panjang

# membuat header program
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{' DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # mengambil input user
# LEBAR = int(input("masukkan nilai lebar: "))
# PANJANG = int(input("masukkan nilai panjang: "))

# # program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # tampilkan hasilnya
# print(f"hasil perhitungan luas= {LUAS}")
# print(f"hasil perhitungan keliling= {KELILING}")

def header():
    '''fungsi Header'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{' DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    # mengambil input user
    lebar = int(input("masukkan nilai lebar: "))
    panjang = int(input("masukkan nilai panjang: "))

    return lebar, panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)

def display(massage,value):
    '''ini adalah fungsi display'''
    print(f"hasil perhitungan {massage} = {value}")

# program utama
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    opsi = input("pilih perhitungan luas/keliling (l/k): ")
    if opsi == "l":
        display("luas", LUAS)
    elif opsi == "k":
        display("keliling", KELILING)
    else:
        display("luas", LUAS)
        display("keliling", KELILING)

    iscontinue = input("apakah lanjut(y/n)? ")
    if iscontinue == "n":
        break

print("program selesai")









