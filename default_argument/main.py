"""Default Argument"""

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):

# contoh 1
def say_hello(nama = "Disana"):
    """fungsi dengan default argument"""
    print(f"Hallo {nama}")

say_hello("farid")
say_hello()

# contoh 2
def sapaan(pesan, nama = "kamu"):
    """fungsi dengan input biasa dan default argumen"""
    print(f"hai {nama}, pesannya adalah {pesan}")

sapaan("jangan tidur malam", "farid")
sapaan("Jangan kemana mana")

# contoh 3
def hitung_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil
print(hitung_pangkat(4,2))

hasil = hitung_pangkat(pangkat=2,angka=9)
print(hasil)

# contoh 4
def fungsi(input1=1, input2=2,input3=3,input4=4):
    hasil = input1+input2+input3+input4
    return hasil

print(fungsi())
print(fungsi(input3=6))