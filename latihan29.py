## ------list------

# kumpulan data number
angka = [1,2,3,4,5]
print(angka)

# kumpulan data string
data = ["agit","juan","kurniawan"]
print(data)

# kumpulan boolean
boolean = [True, False,True,False]
print(boolean)

#kumpulan campuran
campuran = [1, "bal", 2,"[halo]",3]
print(campuran)

## cara alternatif membuat list
data = range(0,10,2)
print(data)
data = list(data)
print(data)

# membuat list dengan for loop, list comprehensiet
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i !=5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 !=0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 !=0]
print(list_pake_for_if)








