# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari >
print('=========== Lebih besar dari >')
hasil = a > 3
print(a,' > ',3,'=',hasil)
hasil = b > 3
print(a,' > ',3,'=',hasil)
hasil = b > 2
print(a,' > ',2,'=',hasil)

# kurang dari <
print('=========== kurang dari <')
hasil = a < 3
print(a,' < ',3,'=',hasil)
hasil = b < 3
print(a,' < ',3,'=',hasil)
hasil = b < 2
print(a,' < ',2,'=',hasil)

# lebih dari sama dengan >=
print('=========== lebih dari sama dengan >=')
hasil = a >= 3
print(a,' >= ',3,'=',hasil)
hasil = b >= 3
print(a,' >= ',3,'=',hasil)
hasil = b >= 2
print(a,' >= ',2,'=',hasil)

# Kurang dari sama dengan <=
print('=========== Kurang dari sama dengan <=')
hasil = a >= 3
print(a,' >= ',3,'=',hasil)
hasil = b >= 3
print(a,' >= ',3,'=',hasil)
hasil = b >= 2
print(a,' >= ',2,'=',hasil)

# sama dengan ==
print('=========== sama dengan ==')
hasil = a == 3
print(a,' == ',3,'=',hasil)
hasil = b == 3
print(a,' == ',3,'=',hasil)
hasil = b == 2
print(a,' == ',2,'=',hasil)

# tidak sama dengan !=
print('=========== tidak sama dengan !=')
hasil = a != 3
print(a,' != ',3,'=',hasil)
hasil = b != 3
print(a,' != ',3,'=',hasil)
hasil = b != 2
print(a,' != ',2,'=',hasil)

# komperasi > < <= >= == != dapat bekerja pada syntax literal
# contoh literal: a == 4

print('=========== object identity (is)')
# 'is' membandingkan objeck, dan tidak bisa literal
# "is" sebagai komperasi bjeck identity
x = 5 # ini adalah assighment membuat object
y = 5 
print("nilai x = ",x,'id = ',hex(id(x)))
print("nilai y = ",y,'id = ',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)

print('=========== object identity (is not)')
x = 5 # ini adalah assighment membuat object
y = 6 
print("nilai x = ",x,'id = ',hex(id(x)))
print("nilai y = ",y,'id = ',hex(id(y)))
hasil = x is not y
print('x is not y = ',hasil)





