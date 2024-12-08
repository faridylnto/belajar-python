# Global and local scope
nama_global = "Muhammad Farid Yulianto" # <-- ini adalah variabel global

# akses variabel global dalam function
def fungsi():
    print(f"fungsi menghasilkan {nama_global}")


fungsi()

# akses variable global dalam loop
for i in range(0,5):
    print(f"loop ke {i+1} tampilkan {nama_global}")

# Percabangan
if True :
    print(f"if menampilkan nama global {nama_global}")

## variable local scope

def fungsi_2():
    nama_local = "Bolet" #<-- variabel local scope
    print(nama_local)

fungsi_2()
# print(nama_local) tidak bisa dilakukan

## contoh 1: penggunaan akses variabel

def say_nama():
    print(f"hello {nama}")

nama = "Julian"
say_nama()

## Contoh 2 : Mengubah variable global
angka = 0
name = "Lola"
def ubah(nilai_baru, nama_baru):
    global angka, name # fungsi ini mendapat akses merubah angka``
    angka = nilai_baru
    name = nama_baru

print(f"Sebelum {angka} dan {name}")
ubah(10,"Lili")
print(f"Sesudah = {angka} dan {name}")

## Contoh 3
angka = 0
for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)