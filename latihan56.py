import latihan56_sains.latihan56_matematika
from latihan56_sains import latihan56_fisika
from latihan56_sains.latihan56_fisika import gaya as force

hasil_tambah = latihan56_sains.latihan56_matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}")

gaya = latihan56_fisika.gaya(90,10)
print(f"gaya adalah = {gaya}")

gaya = force(90,10)
print(f"gaya adalah = {gaya}")
