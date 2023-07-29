#Test komprasi

# Komprasi < (lebih kecil dari)
a = 4
b = 7
c = 8

print("-Lebih kecil dari-")
hasil = a < b
print(a,'<',b,'=',hasil)
hasil = a < c
print(a,'<',c,'=',hasil)
hasil = c < a 
print(c,'<',a,'=',hasil)

# Komprasi > (lebih besar dari)
a = 4
b = 7
c = 8

print("-Lebih besar dari-")
hasil = a > b
print(a,'>',b,'=',hasil)
hasil = a > c
print(a,'>',c,'=',hasil)
hasil = c > a
print(c,'>',a,'=',hasil)


# Komprasi >= (lebih sama dari)
a = 4
b = 8
c = 8

print("-Lebih sama dari-")
hasil = a >= b
print(a,'>=',b,'=',hasil)
hasil = b >= c
print(b,'>=',c,'=',hasil)
hasil = c <= a
print(c,'<=',a,'=',hasil)

# Komprasi >= (lebih kurang dari)
a = 4
b = 8
c = 7

print("-Lebih kurang dari-")
hasil = a <= b
print(a,'<=',b,'=',hasil)
hasil = b <= c
print(b,'<=',c,'=',hasil)
hasil = c <= a
print(c,'<=',a,'=',hasil)

# Komprasi == (Sama dari)
a = 4
b = 8
c = 8

print("-Sama dari-")
hasil = a == b
print(a,'==',b,'=',hasil)
hasil = b == c
print(b,'==',c,'=',hasil)
hasil = c == a
print(c,'==',a,'=',hasil)

# Komprasi != (Tidak Sama dari)
a = 4
b = 8
c = 8

print("-Tidak sama dari-")
hasil = a != b
print(a,'!=',b,'=',hasil)
hasil = b != c
print(b,'!=',b,'=',hasil)
hasil = c != a
print(c,'!=',a,'=',hasil)

# Komprasi (objective identify)
a = 5
b = 5

print("-idk wtf is this but ok-")
hasil = a is b
print(a,'is',b,'=',hasil)