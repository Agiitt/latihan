# date and time (latihan)

import datetime as dt # penjelasannya : mengimpor "datetime" menjadi "dt". jadi sebagai penganti nama

print("silahkan masukkan tanggal, \nbulan dan tahun lahir anda\n")
tanggal = int(input("tanggal \t:"))
Bulan = int(input("Bulan \t\t:"))
Tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(Tahun, Bulan, tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")
print(f"harinya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
#umur_hari_sisa = (umur_hari.days % 365) // 24
print(f"umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan, ") #{umur_hari_sisa} hari


