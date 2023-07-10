"""
a = float(input("masukkan angka: "))
b = float(input("masukkan angka: "))

hasil = a * b
print("hasil yang ditermukan dari ",a,"*",b,"=",hasil," atau ", )
"""

print("\n",18*'=','\n')
#  ---------0++++++++5---------8+++++++11-------
# nomor 1: 
halo = float(input('masukkan angka: \nlebih dari 0 dan kurang dari 5\natau\nlebih dari 8 dan kurang dari 11: '))
a = halo > 0
b = halo < 5
c = halo > 8
d = halo < 11

laho = a and b 
hola = c and d 
loha = laho or hola
print('nilai yang beririsan dari 0-5:',laho,'\ndan nilai yang beririsan dari 8-11:',hola,'\nmaka kebenaran nilai yang beririsan dari 0-5 dan 8-11 adalah:',loha)


#+++++++0----------5++++++++++8-----------11+++++++
print("\n",18*'=','\n')
# nomor 2: 
halo = float(input('masukkan angka: \nkurang dari 0 dan lebih dari 11\natau\nkurang dari 8 dan lebih dari 5: '))
a = halo < 0
b = halo > 5
c = halo < 8
d = halo > 11

laho = a or d
hola = b and c
loha = laho or hola
print('nilai yang < 0 dan > 11:',laho,'\ndan nilai yang beririsan dari 5-8:',hola,'\nmaka kebenaran nilai yang < 0 tau > 11 dan nilai yang beririsan dari 8-11 adalah:',loha)


