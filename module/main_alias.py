# module matematika dengan import

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as p

import matematika as math
hasil_tambah = add(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = k(1,2,3,4,5)
print(f"hasil kali = {hasil_kali}")

hasil_pangkat = p(3)(5)
print(f"Hasil pangkat 3 dari 5 = {hasil_pangkat}")