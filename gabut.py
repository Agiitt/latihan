def harga_setelah_pajak(harga_dasar):
    return harga_dasar + 500

harga_cilok = 5000
harga_final_cilok = harga_setelah_pajak(harga_cilok)
print("Harga cilok 1 porsi Rp.", harga_final_cilok)