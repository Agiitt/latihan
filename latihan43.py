import datetime
import os # directory python
import string
import random

# tamplate dict mahasiswa
mahasiswa_template = {
    "nama":"nama",
    "nim":"00000000",
    "sks":0,
    "lahir":datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("cls") #perintah untuk windows
    #os.system("clear") #perintah untuk linux, unix, Mac

    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama: ")
    mahasiswa['nim'] = input("nim: ")
    mahasiswa['sks'] = input("sks: ")
    TAHUN_LAHIR = int(input("TAHUN lahir (YYYY): "))
    BULAN_LAHIR = int(input("BULAN lahir (MM): "))
    TANGGAL_LAHIR = int(input("TANGGAL lahir (DD): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6))) # kita akan menggunakan key, dengan menggunakan random kemudian memilih string dengan kode ascii_uppercase terus mau bikin 6 kali i
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n.-------.------------------.----.----------.")
    print(f"{'|KEY':<7} {'|Nama':<18} {'|SKS':<4} {'|Lahir':<11}|") # simbol baru ":<3" rata kiri, ":>3" rata kanan, ":^" rata tengah
    print("+-------+------------------+----+----------+")

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x") # "%x" menandakan tahun, bulan, tanggal. "%X" menandakan jam menit detik

        print(f"|{KEY:<6} |{NAMA:<17} |{SKS:^3} |{LAHIR:<10}|") # simbol baru ":<3" rata kiri, ":>3" rata kanan, ":^" rata tengah
        print("+-------+------------------+----+----------+")

    print('\n')
    isdone = input("mau nambah bang (y/n)? ")
    if isdone == "n":
        break

print("ini akhir dari program terimakasih")