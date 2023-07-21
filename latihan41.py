# copy dictionary

teman_teman = {
    "agt":"agit",
    "cp":"ucup",
    "dung":"dungdung surundung",
    "cuy":"ucuy surucuy",
    "tg":"totong surotong"
}

# friends = teman_teman
friends = teman_teman.copy() # dengan perintah copy() membuat duahal yang berbeda

print(f"teman teman: {teman_teman}\n")
print(f"friend: {friends}\n")

teman_teman["cp"]=["ucup sikeren"]
print(f"teman teman: {teman_teman}\n")
print(f"friend: {friends}\n")

# pop dictionary (fungsinya mentransfer / memindahkan dari friends ke pop), (berdasarkan key(pembilang / sebelum ":"))

dataagit = friends.pop("agt")
print(f"data agit: {dataagit}\n")

# popitem dictionary (yang terakhir ajah)
dataakhir = friends.popitem()
print(f"data agit: {dataakhir}\n")
print(f"friend: {friends}\n")











