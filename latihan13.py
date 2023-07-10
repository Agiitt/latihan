# operasi bitwise, operasi biner, binary

# bitwise = operasi masing masing bit

a = 9
b = 5 

# bitwise OR (|)
c = a | b 
print('\n=================OR======')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('--------------------------------(|)')
print('nilai :',c,', binary :',format(c,'08b'))

# bitwise AND (&)
c = a & b 
print('\n=================OR======')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('--------------------------------(&)')
print('nilai :',c,' , binary :',format(c,'08b'))

# bitwise XOR (^)
c = a ^ b 
print('\n=================xOR======')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('--------------------------------(^)')
print('nilai :',c,', binary :',format(c,'08b'))

# bitwise NOT (~)
c = ~a
print('\n=================NOT======') # jadi untuk sistem not sendiri adalah memiror nilai dari positif menjadi negatif, contohnya dari positif 9 menjadi negatif 10 (9 menjadi -10). penghitunganya mulai dari -1 bukan dari 0, jadi -1 dianggap 0
print('nilai :',a,' , binary :',format(a,'08b'))
print('--------------------------------(~)')
print('nilai :',c,', binary:',format(c,'08b'))
print('--------------------------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,' , binary :',format(e^d,'08b'))

# shifring

# shift right (>>)
c = a >> 2
print('-\n------------->>----------------')
print('nilai :',a,' , binary :',format(a,'08b'))
print('--------------------------------(>>)')
print('nilai :',c,' , binary :',format(c,'08b'))

#shift left (<<)
c = a << 2
print('-\n-------------<<----------------')
print('nilai :',a,' , binary :',format(a,'08b'))
print('--------------------------------(<<)')
print('nilai :',c,', binary :',format(c,'08b'))








