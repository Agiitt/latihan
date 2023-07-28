# globala dan local scope

nama_global = "otong" # <- ini varibel global

# akses variasi global dalam fungsi
def fungsi():
    print(f"fungsi menampilakan {nama_global}")

fungsi()

# akses variabel global dlam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabanga
if True:
    print(f"if menampilakan {nama_global}")

## variabel label scope

def fungsi2():
    nama_local = "ucup" # <- variabel local scope

fungsi2()
# print(nama_local) # tidak dapat dilakukan 

## contoh 1: penggunaan akses variable
def say_otong():
    print(f"hello {nama}")

nama = "otong"
say_otong()

# contoh 2: merupakan variabel global
angka = 0

def ubah(nilai_baru,nama_baru):
    global angka # fungsi ini dapat mengakses dan merubah angka
    global nama
    angka = nilai_baru
    nama = nama_baru

print(f"sebelum {angka,nama}")
ubah(10,"otong")
print(f"sebelum {angka,nama}")


# contoh 3:
for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)