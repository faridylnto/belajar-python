import datetime
import os
import string
import random
# os.system("cls")

# data_mahasiswa= []


# while True:
#     nama = input("Masukkan nama lengkap : ")
#     nim = input("Masukkan NIK : ")
#     sks = int(input("Masukkan total sks :"))
#     TAHUN_LAHIR = int(input("Tahun lahir (YYYY) : "))
#     BULAN_LAHIR = int(input("Bulan lahir (1-12) : "))
#     TANGGAL_LAHIR = int(input("Tanggal lahir (1-31) : "))
 
#     mahasiswa ={
#     "nama" : nama,
#     "nim" : nim,
#     "sks_lulus" : sks,
#     "lahir" : datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
# }

#     data_mahasiswa.append(mahasiswa)
#     print("-"*60)
#     print(f"{"Nama" :<30} {"NIM" :<20} {"Lahir" :<10} {"SKS" :<10}")
#     for index, value in enumerate(data_mahasiswa):
#         print(f"{data_mahasiswa[index]["nama"] :<30} {data_mahasiswa[index]["nim"] :<20} {data_mahasiswa[index]["lahir"] :<10} {data_mahasiswa[index]["sks_lulus"] :<10}")
#     print(data_mahasiswa)
#     selesai = input("Selesai? (y/n)")

#     if selesai == "n" :
#         break

data_mahasiswa = {}

template = {
    "nama" : "aaaa",
    "nim" : "0000",
    "sks_luls" : 0,
    "lahir": datetime.datetime(1888,11,21)
}
while True:
    os.system("cls")
    print(f"{"SELAMAT DATANG":^20}")
    print(f"{"DATA MAHASISWA":^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(template.keys())
    mahasiswa["nama"] = input("Masukkan nama lengkap : ")
    mahasiswa["nim"] = input("Masukkan NIM : ")
    mahasiswa["sks_lulus"] = int(input("Masukkan total sks :"))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY) : ")) 
    BULAN_LAHIR = int(input("Bulan lahir (1-12) : "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31) : "))
    mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY : mahasiswa})

    print(f"{"KEY":<10} {"NAMA" :<30} {"NIM":<20} {"SKS" :<10} {"LAHIR" :<10}")
    print("-"*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]["nama"]
        NIM = data_mahasiswa[KEY]["nim"]
        SKS = data_mahasiswa[KEY]["sks_lulus"]
        LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")
        print(mahasiswa)
        print(f"{KEY : <10}{NAMA :<30} {NIM :<20} {SKS :<10} {LAHIR :<10}")
    
    print("\n")
    is_done = input("Sudah selesai (y/n)? ")

    if is_done == "y":
        break

print("akhir dari program")