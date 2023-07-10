# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# +++++++++3----------10++++++++

inputuser = float(input('masukkan angka yang bernila\nkurang dari 3\natau \nlebih besar dari 10: '))

# ++++++3---------
# memerikasa angka kurang dari 3
iskurangdari = (inputuser < 3)
print("kurang dari 3 =",iskurangdari)

#-----------10+++++++++
# memeriksa angka lebih dari 10
islebihdari = (inputuser > 10)
print("lebih dari 10 =",islebihdari)

# ++++++++++3------------10+++++++++++
iscorrect = iskurangdari or islebihdari
print('angka yang anda masukkan: ', iscorrect)


# ----------3+++++++++++10-------
# ini adalah kasus irisan
print("\n",18*'=','\n')
inputuser = float(input('masukkan angka yang bernila\nlebih dari 3\ndan \nkurang dari 10: '))

#-------3++++++++++++
# lebih dari 3
islebihdari = inputuser > 3
print('lebih dari 3=',islebihdari)

# +++++++++10------------
# kurang dari 10
iskurangdari = inputuser < 10
print('kurang dari 10= ',iskurangdari)

# -------------3+++++++++10---------
iscorrect = iskurangdari and islebihdari
print('angka yang anda masukkan: ', iscorrect)




print("\n",18*'=','\ntugas')
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











