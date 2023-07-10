# latihan konversi satuan temperatur

# program konversi celcius kesatuan lain

print("program konversi temperatur")

celcius = float(input('masukkan suhu dalam celcius: '))
print('suhu adalah ', celcius, 'celcius')

# reamur
reamur = (4/5) * celcius
print('suhu dalam reamur adalah', reamur, 'reamur')

# fahrenheit
fahrenheit = (9/5) * celcius + 32
print('suhu dalam fahrenheit adalah', fahrenheit, 'fahrenheit')

# kelvin
kelvin = celcius + 373
print('suhu dalam kelvin adalah', kelvin, 'kelvin')

# Fahrenheit to Kelvin
Fahrenheit = float(input('Masukkan suhu dalam Fahrenheit : '))
Kelvin = (Fahrenheit - 32) * (5/9) + 273
print('Kelvin : ', Kelvin, 'K')

# Kelvin to Fahrenheit
Kelvin = float(input('Masukkan suhu dalam Kelvin : '))
Fahrenheit = (Kelvin - 273) * (9/5) + 32
print('Fahrenheit : ', Fahrenheit, 'F')



