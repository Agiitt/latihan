# fungsi dengan aargument (input)


#def nama_fungsi(argumen):
#    badan fungsi


def hello_world(nama):
    ''' fungsi hello world menerima fungsi dengan nama'''
    print(f"selamat datang dunia wahai {nama}")

hello_world("udul") # dapat diisi dengan boolean, string, integer, dan sebagainya

# program tambah

def tambah(angka1,angka2):
    # fungsi tambah
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(1,5)
tambah(100000,1)

def say_hi(list_peserta):
    # fungsi say_hi
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")

anggota_boyband = ["ucup","otong","dudung"] # cara membacanya adalah: say_hi(anggota_boyband) naik ke def say_hi(list_peserta), data_peserta sama dengan list_peserta yang diduplikat, looping peserta pada data_peserta dengan dan tampilkan "yang terhormat {(nama yang berada pada list anggota_boyband)}". jadi apapun yang dimasukkan pada say_hi akan masuk kedalam def dan dieksekusi 
say_hi(anggota_boyband)


















