"""type hints untuk fungsi"""

# studi kasus
# def fungsi(parameter):
#     print(parameter**2)

# fungsi(1)
# fungsi("Ucup")
# fungsi(True)

# Penggunaan type hints

def fungsi_dengan_hints(argument:int) -> int:
    output = 10**argument
    return output

hasil = fungsi_dengan_hints(2)
print(hasil)

# def display(argument:string):
#     print(argument)

# display("ucup")

import os

hasil = os.system("cls")
print(hasil)