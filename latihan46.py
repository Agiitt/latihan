''' fungsi dengan kembalian'''

# template fungdi dengan kembalian
# def nama_fungsi(argumen):
#       badan fungsi
#       return output

# fungsi kuadrat

def kuadrat(input_angka):
    '''fungsi kuadrat'''
    output_angka = input_angka**2
    return output_angka

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# fungsi tambah

def fungsi_tambah(angka1,angka2):
    '''fungsi return dengan multi input'''
    return angka1 + angka2

a = fungsi_tambah(10,8)
print(a)

# fungsi dengan return banyak

def operasi_mtk(angka1,angka2):
    tambah = angka1 + angka2    
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_mtk(9,5)

print(f"hasil = {k}")
print(f"hasil = {l}")
print(f"hasil = {m}")
print(f"hasil = {n}")





















