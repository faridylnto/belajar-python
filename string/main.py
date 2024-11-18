# membuat string

data = "ini adalah string"
print(data)
print(type(data))

'''
1. dengan menggunakan single quote '....'
1. dengan menggunakan double quote "...."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"halo, apa kabar?"')
print("'halo, apa kabar?'")
print("ini adalah hari jum'at")

# menggunakan tanda \
# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it')

# backlash \
print("C:\\user\\ucup")

#tab
print("ucup\totong, jauhan")

#backspace
print("ucup \botong")

#newline
print("baris pertama. \nbaris kedua") #line feed -> unix, macos, linux
print("baris pertama. \rbaris kedua") #cr = carriage return -> commodore, lisp
print("baris pertama. \r\nbaris kedua") #crlf = line feed carriage return -> windows

# string literal atau raw

# hati - hati
print('C:\new folder') # akan salah

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string raw
print(r"""
Nama : Ucup
Kelas : 3 SD \new normal
website : www.ucup.com/newID
""")