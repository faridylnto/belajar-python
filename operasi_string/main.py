# operasi dan manipulasi string

# menyambung string (concatenate)
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari "+ nama_lengkap + " = " + str(panjang))

# operator untuk string
# mengecek apakah ada komponen char atau string di string
d = "D"
status = d in nama_lengkap
print(d + " ada di "+ nama_lengkap + " " + str(status))

d = "D"
status = d  not in nama_lengkap
print(d + " ada di "+ nama_lengkap + " " + str(status))

# mengulang string
print("wk"*10)
print(10*"wk")

# indexing = mengambil data dari string
print("index ke - 0 : " +nama_lengkap[0])
print("index ke - 6: " +nama_lengkap[6])
print("index ke - -1: " +nama_lengkap[-1])
print("index ke - [0:3]: " +nama_lengkap[0:3])
print("index ke - [3:8]: " +nama_lengkap[3:8])
print("index ke - [0,2,4,6,8,10]: " +nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : "+ min(nama_lengkap)) # paling kecil
print("paling besar : "+ max(nama_lengkap))

ascii_code = ord(" ")
print("ascii code untuk spasi : " + str(ascii_code))
data = 117
print("ascii code untuk 117 : " + chr(data))

# operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada data = " + str(jumlah))

## merubah case dari string

# merubah semua ke UpperCase
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lowercase
alay = "aKu KeCe AbieeeZzzzZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan menggunakan isX method
# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() #hasilnya boolean
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() untuk mengecek semuanya huruf
# isalnum() untuk mengecek huruf dan angka
# isdecimal() untuk mengecek semuanya angka
# isspace() untuk mengecek spasi, tab, newline \n
# istittle() untuk mengecek semua kata dimulai dengan huruf besar

judul = "It Is Ok Not To Be Orkay"
apakah_tittle = judul.istitle()
print(judul +" is tittle = " + str(apakah_tittle))

## cek komponen startswith() endswith()
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## penggabungan komponen joint() split()
pisah = ["aku", "sayang", "kamu"]
gabung = ",".join(pisah)
print(pisah)
print(gabung)
gabung = " ".join(pisah)
print(gabung)
gabung = " ehm ".join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung.split("ehm"))

# alokasi karakter rjust(), ljust(), center()
print(5*"="+"data"+"="*5)

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10,"-")
print("'"+"tengah".center(10,"-")+"'")

#kebalikannya -> strip()
tengah = tengah.strip( "-") # menghilangkan tanda -
print(tengah)