# latihan perulangan

# membuat segitiga
# print("menggunakan while")
# data_int = int(input("masukkan angka sisi ="))
# angka = 1
# while True:
#     print(angka*"*")
#     angka += 1
#     if angka > data_int:
#         break
# print("\n")

# print("Menggunakan for")
# sisi = int(input("Masukkan sisi untuk for = "))
# count = 1
# for i in range(sisi):
#     print("*"*count)
#     count += 1

# Hanya ganjil saja

print("menggunakan while")
data_int = int(input("masukkan angka sisi ="))
angka = 0
spasi = int(data_int/2)
while True:
    angka += 1
    if angka % 2 == 0:
        continue

    print(" "*spasi,angka*"+")

    if angka >= data_int:
        break
print("\n")

# print("Menggunakan for")
# sisi = int(input("Masukkan sisi untuk for = "))
# count = 0
# for i in range(sisi):
#     count += 1
#     if count % 2 == 0:
#         continue
#     print(count*"*")

# segitiga sama sisi
print("menggunakan while")
data_int = int(input("masukkan angka sisi ="))
angka = 0
spasi = int(data_int/2)
while True:
    angka += 1
    if angka % 2 == 0:
        spasi -= 1
        continue

    print(" "*spasi,angka*"+")

    if angka >= data_int:
        break
print("\n")

def buat_ketupat(ukuran):
  """
  Fungsi untuk membuat bentuk ketupat dengan ukuran tertentu.

  Args:
    ukuran: Panjang sisi ketupat.
  """

  # Membuat bagian atas ketupat
  for i in range(ukuran):
    spasi = " " * (ukuran - i - 1)
    bintang = "*" * (2 * i + 1)
    print(spasi + bintang)

  # Membuat bagian bawah ketupat
  for i in range(ukuran - 2, -1, -1):
    spasi = " " * (ukuran - i - 1)
    bintang = "*" * (2 * i + 1)
    print(spasi + bintang)

# Contoh penggunaan
ukuran_ketupat = 5
buat_ketupat(ukuran_ketupat)