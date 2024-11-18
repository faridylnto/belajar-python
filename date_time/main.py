#  Date and Time (latihan)

import datetime as dt

# hari_ini = dt.date.today()
# print(hari_ini)
# tanggal = dt.date(1995,7,10)
# print(tanggal)

print("silahkan masukkan tanggal, \nbulan dan tahun lahir anda")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir kamu: {tanggal_lahir}")
print(f"Kamu lahir pada hari {tanggal_lahir:%A}")

umur = (dt.date.today() - tanggal_lahir)
umur_tahun = umur.days // 365
umur_bulan = (umur.days % 365) // 30
print(umur_bulan)
print(f"Umur anda adalah : {umur_tahun} tahun, {umur_bulan} bulan")

