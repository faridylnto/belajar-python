print("hello world")

nama = "farid"
hobi = "makan"
umur = 28
laki = True

print("======Biodata======")
print("nama: %s"% (nama))
print("hobi: %s, umur:%d, laki: %r"% (hobi,umur,laki))

nama: str = "Winny"
hobi : str = "memasak"
umur : int = 29
laki : bool = False
nilai_ujian : float = 99.9

print("======Biodata======")
print("nama: %s"% (nama))
print("hobi: %s, umur:%d, laki: %r, nilai_ujian: %f"% (hobi,umur,laki,nilai_ujian))

from typing import final

PI : final = 3.14
print("PI:%f" %(PI))

string_multi_baris: str = """\
aku dan kamu
tinggal bersama
sampai tua nanti"""
print("%s"%(string_multi_baris))