## teknik menduplikat list

a = ["ucup", "dudung", "asep",]
print(f"a = {a}")

b = a # pass by reference (memberikan referensi ke b)
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list
print(f"address a = {hex(id(a))}")
print(f"address a = {hex(id(b))}")

# menduplikat list dengan copy

print("membuat list c dengan a.copy()")

c = a.copy() # full duplikat / data baru / address baru

print(f"address a = {hex(id(a))}")
print(f"address a = {hex(id(b))}")
print(f"address a = {hex(id(c))}")


print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[0] = "dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
a[0] = "ramly"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")



















