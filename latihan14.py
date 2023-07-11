# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assingment

a = 5 # adalah assingnment
print('nilai a =',a)

a += 1 # ini artinya adalah a = a + 1
print('nilai a += 1, nila a menjadi',a)

a -= 2 # artinya adalah a = a - 2
print('nilai a -= 2, nila a menjadi',a)

a *= 5 # artinya adalah a = a * 5
print('nilai a *= 5, nila a menjadi',a)

a /= 2 # artinya adalah a = a / 2
print('nilai a /= 2, nila a menjadi',a)


b = 10
print('\nnilai b =',b)

# mudulus dan floor division
b %= 3 # artinya adalah b = b % 3
print('nilai b %= 3, nila b menjadi',b)

b = 10
print('\nnilai b =',b)

b //= 10 # artinya adalah b = b // 10
print('nilai b //= 10, nila b menjadi',b)


a = 5
print('nilai a =',a)
a **= 3
print('nilai a **= 3, nila a menjadi',a)

# operasi bitwise
# OR
c = True
print('\nnilai c =',c)
c |= False
print('nilai c |= False, nila a menjadi',c)

c = False
print('\nnilai c =',c)
c |= False
print('nilai c |= Fasle, nila a menjadi',c)

# AND
c = True
print('\nnilai c =',c)
c &= False
print('nilai c &= False, nila a menjadi',c)

c = True
print('\nnilai c =',c)
c &= True
print('nilai c &= True, nila a menjadi',c)

# XOR
c = True
print('\nnilai c =',c)
c ^= False
print('nilai c ^= False, nila a menjadi',c)

c = True
print('\nnilai c =',c)
c ^= True
print('nilai c ^= True, nila a menjadi',c)

# Gser geser
d = 0b0100
print('\nnilai d =',format(d,'04b'))
d >>= 2
print('nilai d >>= 2, nilai d menjadi',format(d,'04b'))
d <<= 1
print('nilai d <<= 1, nilai d menjadi',format(d,'04b'))











