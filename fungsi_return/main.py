"""fungsi dengan return (nilai kembali)"""

# template fungsi dengan nilai return
# def nama_fungsi(argument):
    #badan fungsi
    # return output

# fungsi kuadrat

def kuadrat(input_angka):
    output_kuadrat = input_angka**2
    return output_kuadrat

print(kuadrat(4))
y = 5
print(y)

z = 10 + kuadrat(7)
print(z)

# fungsi tambah

def tambah(angka_1,angka_2):
    """fungsi return dengan multi output"""
    return angka_1 + angka_2
a = tambah(10,9)
print(a)

# fungsi dengan return banyak
def operasi_matematika(angka_1,angka_2):
    kali = angka_1*angka_2
    bagi = angka_1/angka_2
    plus = angka_1 + angka_2
    kurang = angka_1 - angka_2
    return kali, bagi, plus, kurang

times, div, plus, minus, = operasi_matematika(5,19)
print(f"hasil kali = {times}") 
print(f"hasil bagi = {div}")  
print(f"hasil tambah = {plus}")  
print(f"hasil kurang = {minus}")  
