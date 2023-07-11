# operasi dalam bentuk methode

## merubah cara dari string

# merubah semua ke upper case

salam = 'bro!'
print('normal = ' + salam)
salam = salam.upper()
print('upper = ' + salam)

# merubah semua ke lower case
alay = "aKu KeCe Abieeezzzz"
print('normal = ' + alay)
alay = alay.lower()
print('lower = ' + alay)

## pengecekan menggunaka "isX" methode
 
# contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <--- untuk mengecek semua huruf
# isalnum() <--- huruf dan angka
# isdecima() <--- angka saja
# isspace() <--- spasi, tab, newline \n
# istitle <--- semua kata dimulai dengan huruf besar

judul = "It's Okey To Be Orkay" # salah
judul = "It is Okey To Be Orkay" # salah
judul = "It Is Okey To Be Orkay" # benar

cek_judul = judul.istitle() # hasilnya boolean

print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() 
cek_start = "Sangjangnim Oppa".startswith("sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## menggabungkan komponen join() split
pisah = ['aku',"sayang",'kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gedung = ' ehm '.join(pisah)
print(gabung)

gabung = "akueumsayangehmkamu"
print(gabung.split('eham'))

#alokasi karakter
print(5*"=" + "data " + "="*5)

#alokasi karakter rjust(), ljust() center() 
print(5*"=" + "data " + "="*5)

kanan = "kanan".rjust(10)
print("''" + kanan + "'")
kiri = "kiri".ljust(10)
print("''" + kiri + "'")

tengah = "tengah".center(28,":")
print("'"+tengah+"'")

# kebalikannya ---> strip()
tengah = tengah.strip(":") #menghilangkan tanda 1
print("'"+tengah+"'")





