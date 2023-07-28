# modul matematika dengan inport

from latihan55_matematika import tambah as add
from latihan55_matematika import kali as k
from latihan55_matematika import pangkat as pg
# from matematika import * # "*"simbol bintang pada import berfungsi untuk mengambil semuanya yang berada pada latihan55_matematika.py

import latihan55_matematika as math # <--- bisa  dilakukan

hasil_tambah = add(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = k(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

pangkat = pg(5)
print(f"hasil pangkat = {pangkat(5)}")