# format string


# contoh generik
# string
nama = "marlena"
format_str = f"hello {nama}"

print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}" 
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# bilangaan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"# otomatis memberikan koma setelah tiga angka
print(format_str)

# bilangan desimal
angka = 2005.5321
format_str = f"desimal = {angka:.2f}" # "..f" huruf ini menandakan bahwa huruf tersebut adalah float
print(format_str)

# menampilkan leading zero
angka = 2005.5321
format_str = f"desimal = {angka:09.3f}"
print(format_str)

# menapilkan tanda + atau -
angka_minus = -10
angka_plus = -10.23423
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# menformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi didalam placeholde
harga = 10000
jumlah = 5

format_str = f"harga total = {harga*jumlah:,}"
print(format_str)

# format angka lain (liberary, octal, hexadecilam)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)



