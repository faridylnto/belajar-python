# multi key dictionary

import datetime

mahasiswa = {
    "nama" : "farid",
    "nim" : "123456",
    "sks_lulus" : 130,
    "beasiswa" : False,
    "lahir" : datetime.datetime(2001,10,19)
}

mahasiswa1 = {
    "nama" : "muhammad",
    "nim" : "190293",
    "sks_lulus" : 143,
    "beasiswa" : True,
    "lahir" : datetime.datetime(2002,3,19)
}

mahasiswa2 = {
    "nama" : "yulianto",
    "nim" : "1983012",
    "sks_lulus" : 120,
    "beasiswa" : False,
    "lahir" : datetime.datetime(1994,10,19)
}

data_mahasiswa = {
    "MAH001" : mahasiswa,
    "MAH002" : mahasiswa1,
    "MAH003" : mahasiswa2
}


print("-"*50)
print(f"{"KEY":<6} {"NAMA" :<17} {"SKS" :<3} {"BEASISWA" :^9} {"LAHIR" :<10}")
print("-"*50)
for maha in data_mahasiswa:
    KEY = maha

    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS =data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA =data_mahasiswa[KEY]["beasiswa"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

    
    print(f"{KEY:<6} {NAMA :<17} {SKS :<3} {BEASISWA :^9} {LAHIR :<10}")
