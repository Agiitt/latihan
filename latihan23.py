# latihan

# membuat kalkulator sederhana


angka_1 = float(input("masukkan angka pertama = "))
operator = input("operator (+, -, *, /) = ")
angka_2 = float(input("masukkan angka kedua = "))

# percabangannya
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasinnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasinnya adalah {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print(f"hasinnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasinnya adalah {hasil}")
else: print("error, fungsi operator tersebut belum ada dalam aplikasi ini")