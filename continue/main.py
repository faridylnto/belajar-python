# continue, pass, break

# pass --> berfungsi sebagai dummy, tidak akan dieksekusi

# angka = 0

# while angka <5:
#     angka += 1
#     if angka == 3:
#         pass # ini tidak kan di eksekusi
#     print(angka)

# continue
angka = 0
print(f"Angka sekarang --> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1
    
    if angka == 3:
        print("Nice")
        continue # akan membuat loop meloncat ke step selanjutnya

    print("whatsss") # aksi 2

print("Great")

# break

data_int = int(input("Hitung sampai ="))
number = 0

while True:
    number += 1
    print(f"count -> {number}")
    
    if number == data_int:
        print("Selesai Berhitung")
        break

    print("Lanjut")

print("Tutup Aplikasi")