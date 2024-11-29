# program list

list_buku = []
while True :
    print("Masukkan data buku")
    judul = input("Masukkan Judul Buku \t: ")
    penulis = input("Masukkan nama penulis \t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    
    print("\n\n", "="*20, "Data Buku")
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n\n", "="*20,)
    is_lanjut = input("Apakah dilanjutkan?(y/n) ")

    if is_lanjut == "n":
        break


