data = 'ini adalah string'
print(data)
print(type(data))


# 1. cara membuat string

'''
    1. dengan menggunakan singel quote ' . . . '
    2. dengan menggunakan double quote " . . . "

'''

data = 'menggunakan singel quote'
print(data)

data = "menggunakan singel quote"
print(data)

print('"hALLO, apakabar"') # didalam kutip satu terdapat kutip dua, kutip dua di baca sebagai string
print("'hallo apa kabae'")
print("ini hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')


# backlash
print("C:\\user\\Ucup")

# TAB
print("ucup\totong, jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama,\nbaris kedua.") # LF -> line feed -> unix, linux
print("baris pertama,\rbaris kedua.") # CR -> carriage return -> commodore, acore, lips
print("baris pertama,\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

# 3. string literal atau raw

# hati hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder') # ini berana

# multiline literal string
print("""
Nama : ucup
kelas : 3 sd
""")

# multiline literal string dan RAW
print(r"""
Nama : ucup
kelas : 3 sd\new normal
website : www.ucup.com/newID
""")





