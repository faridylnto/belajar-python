# looping dari list

# Menggunakan for loop
print("Menggunakan for loop")
kumpulan_angka = [4,3,2,5,6,1]
for angka in kumpulan_angka:
    print(f"angka didalam list adalah {angka}")

peserta = ["ucup","otong","dadang","diding"]
for nama in peserta:
    print(f"Nama nama peserta {nama}")

# for loop dan range
print("\nMenggunakan for loop dan range")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# menggunakan while
print("\nMenggunakan while loop")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)
a = 0
while a < panjang:
    print(f"angka = {kumpulan_angka[a]}")
    a += 1

# list comprehension

print("\nMenggunakan list comprehension")
data = ["ucpu",1,2,3,"otong"]
[print(f"data = {i}") for i in data]
angka = [10,5,4,2,6,5]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)
# menggunakan enumerate
print("\nMenggunakan enumerate")
data = ["ucpu",1,2,3,"otong"]

for index,data in enumerate(data):
    print(f"index ke - {index}, data = {data}")