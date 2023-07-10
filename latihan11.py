# operasi logika atau boolean

# not, or, and, xor

print('=====NOT====')
a = False
c = not a # 'not' pembalik keadaan dari false ke true
print('data a =', a)
print('-------- NOT')
print('data c =', c)

# jika salah satu true, maka hasilnya adalah true
#OR
print('=====OR====')
a = False
b = False
c = a or b
print(a,'OR ',b,'=', c)
a = False
b = True
c = a or b
print(a,'OR ',b,' =', c)
a = True
b = False
c = a or b
print(a,' OR ',b,'=', c)
a = True
b = True
c = a or b
print(a,' OR ',b,' =', c)

#jika dua buah nilai true, maka hasil true
# dan jika salah satu nilai False maka hasilnya false
#AND
print('=====AND====')
a = False
b = False
c = a and b
print(a,'and ',b,'=', c)
a = False
b = True
c = a and b
print(a,'and ',b,' =', c)
a = True
b = False
c = a and b
print(a,' and ',b,'=', c)
a = True
b = True
c = a and b
print(a,' and ',b,' =', c)

# akan True apabila salah satu terdapat True
#XOR
print('=====XOR====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=', c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =', c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=', c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,' =', c)
























