"""Fungsi dengan argumen"""

def hello_world(nama):
    """fungsi hello world menerima input dengan variabel nama"""
    print(f"Selamat datang {nama}")

hello_world("farid")
hello_world("eko")

# program tambah

def tambah(angka_1,angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}" )

tambah(1,5)
tambah(1000,5)

def absensi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Selamat datang {peserta}")

kelompok = ["farid","Muhammad","yulianto"]
absensi(kelompok)
kelompok[1] = "lalat"
absensi(kelompok)