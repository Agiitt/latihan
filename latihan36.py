# program list buku

list_buku = []
while True:
    print("\nMasukan data buku")
    judul = input("judul buku\t: ")
    penulis = input("penulis buku\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print("\n\n","="*10,"data buku","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n\n","="*20)
    islanjut = input("apakah masi lanjut (y/n)")

    if islanjut == "n":
        break
    elif islanjut == "y":
        continue
print("program selesai")



















