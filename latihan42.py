import datetime

mahasiswa1 = {
    "nama":"agit",
    "nim":"1234567",
    "sks":123,
    "beasiswa":True,
    "lahir":datetime.datetime(2001,4,10)
}

mahasiswa2 = {
    "nama":"otong",
    "nim":"123342",
    "sks":132,
    "beasiswa":True,
    "lahir":datetime.datetime(2002,5,20)
}

mahasiswa3 = {
    "nama":"asep",
    "nim":"12745567",
    "sks":110,
    "beasiswa":False,
    "lahir":datetime.datetime(2000,2,29)
}

data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(".-------.------------------.----.----------.----------.")
print(f"{'|KEY':<7} {'|Nama':<18} {'|SKS':<4} {'|Beasiswa':<10} {'|Lahir':<11}|") # simbol baru ":<3" rata kiri, ":>3" rata kanan, ":^" rata tengah
print("+-------+------------------+----+----------+----------+")

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x") # "%x" menandakan tahun, bulan, tanggal. "%X" menandakan jam menit detik

    print(f"|{KEY:<6} |{NAMA:<17} |{SKS:^3} |{BEASISWA:^9} |{LAHIR:<10}|") # simbol baru ":<3" rata kiri, ":>3" rata kanan, ":^" rata tengah
    print("+-------+------------------+----+----------+----------+")

