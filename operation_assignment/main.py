# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a =  5 # adalah assignment
print("nilai a =", a)

a += 1 # artinya a = a + 1
print("nilai a =", a)

a -= 2 # artinya a = a - 2
print("nilai a =", a)

a *= 5 # artinya a = a * 5
print("nilai a =", a)

a /= 2 # artinya a = a / 2
print("nilai a =", a)

b = 10
print("\nnilai b =",b)

b %= 3
print("nilai b%= 3 adalah ", b)

b //= 3
print("nilai b//= 3 adalah ", b)

a = 5
print('nilai a =', a)
a **= 3
print("nilai a**= 3 adalah ", a)

# operasi bitwise
c = True
print('\nnilai c =',c)
c != False
print("nilai c != false, nilai ce menjadi", c)
c = False
print('\nnilai c =',c)
c != False
print("nilai c != false, nilai ce menjadi", c)

#or
c = True
print('\nnilai c =',c)
c |= False
print("nilai c |= false, nilai ce menjadi", c)
c = False
print('\nnilai c =',c)
c |= False
print("nilai c |= false, nilai ce menjadi", c)

#AND
c = True
print('\nnilai c =',c)
c &= False
print("nilai c &= false, nilai ce menjadi", c)
c = True
print('\nnilai c =',c)
c &= True
print("nilai c &= false, nilai ce menjadi", c)

#xor
c = True
print('\nnilai c =',c)
c ^= False
print("nilai c ^= false, nilai ce menjadi", c)
c = True
print('\nnilai c =',c)
c ^= True
print("nilai c ^= false, nilai ce menjadi", c)

# geser
d = 0b0100
print("\nnilai d =", format(d, '04b'))
d >>=2
print('nilai d >>=2, nilai d menjadi',format(d,'04b'))
d <<=1
print('nilai d <<=1, nilai d menjadi',format(d,'04b'))