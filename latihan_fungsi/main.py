"""latihan fungsi"""

import os

# program menghitung luas dan keliling persegi panjang

# Membuat header program
# os.system("cls")
# print(f"{"PROGRAM MENGHITUNG LUAS" : ^40}")
# print(f"{"DAN KELILING PERSEGI PANJANG": ^40}")
# print(f"{"-"*40 :^40}")

# # Mengambil user input
# LEBAR = int(input("Masukkan nilai lebar : "))
# PANJANG = int(input("Masukkan nilai panjang : "))

# # Program menghitung luas dan keliling
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# print(f"Hasil perhitungan luas = {LUAS}")
# print(f"Hasil perhitungan keliling = {KELILING}")

def header():
    os.system("cls")
    print(f"{"PROGRAM MENGHITUNG LUAS" : ^40}")
    print(f"{"DAN KELILING PERSEGI PANJANG": ^40}")
    print(f"{"-"*40 :^40}")

def input_user():
    """Fungsi input user"""
    lebar = int(input("Masukkan nilai lebar : "))
    panjang = int(input("Masukkan nilai panjang : "))
    return lebar, panjang

def hitung_luas(panjang, lebar):
    """Fungsi menghitung luas"""
    luas = panjang * lebar
    return luas

def hitung_keliling(panjang, lebar):
    """Fungsi menghitung keliling"""
    keliling = 2*(panjang+lebar)
    return keliling

def display(message, value):
    """fungsi display"""
    print(f"hasil perhitungan {message} = {value}")

# Programm utama
while True:
    header()
    LEBAR, PANJANG = input_user()
    LUAS= hitung_luas(LEBAR,PANJANG)
    KELILING= hitung_keliling(LEBAR,PANJANG)
    opsi = int(input("Ketik 1 untuk menghitung luas dan ketik 2 untuk menghitung keliling = "))
    if opsi == 1:
        display("luas", LUAS)
    elif opsi ==2:
        display("keliling", KELILING)
    elif opsi != 1 and opsi !=2:
        print("Pilihan tidak ada, silahkan pilih ulang")
        opsi = int(input("Ketik 1 untuk menghitung luas dan ketik 2 untuk menghitung keliling = "))
        continue

    is_continue = input("Apakah lanjut (y/n)?")
    if is_continue == "n":
        break

print("Program selesai")