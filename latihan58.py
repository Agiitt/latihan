import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now: {data_waktu}")
print(f"tahun: {data_waktu.year}")
print(f"hari: {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a","c","d","e","f"]
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"jumlah = {data_count['a']}")
print(f"jumlah = {data_count['d']}")

import io

file = io.open("latihan58.txt","r") # membuka file latihan58.txt, "r" adalah perintah membuka
print(file.read())