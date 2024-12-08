"""**kwargs"""

def fungsi(nama,tinggi, berat):
    """fungsi biasa"""
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("farid",175,79)

def fungsi(**kwargs):
    """fungsi kwargs"""
    nama = kwargs["nama"]
    berat = kwargs["berat"]
    tinggi = kwargs["tinggi"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama = "faris",tinggi = 170, berat = 69)

# studi kasus

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    return output
    

hasil = math(1,2,3,4,5,6, option = "tambah")
print(hasil)
hasil = math(1,2,3,4,5,6, option = "kali")
print(hasil)