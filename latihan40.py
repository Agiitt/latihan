# looping dictionery

teman_teman = {
    "agt":"agit",
    "cp":"ucup",
    "dung":"dungdung surundung",
    "cuy":"ucuy surucuy"

}

# looping first try (yang keluar adalah key-nya)
# "agit":"juan" -> "agit" sebagai pembilang "juan" sebagai penyebut
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item/iterables
# 
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys(): # "keys" = mengambil pembilang (key) dari penyebut (value)
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for values in teman_teman.values(): # "values" = mengambil penyebut (values) dari pembilang (key)
    print(values)

item = teman_teman.items() 
print(item)

for item in teman_teman.items(): # "items" adalah gabungan dari "key" dan "value"
    print(item)

for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")



