# Bitwise

a = 9
b = 5

# Bitwise  or (|)
print('===Or (|)')

print('-----------------------(OR)--')

c = a | b
print('Nilai :',c,'Binary :',format(c,'08b'))

print('Nilai :',a,'Binary :',format(a,'08b'))
print('Nilai :',b,'Binary :',format(b,'08b'))

# Bitwise  and (&)
print('===And (&)')

print('-----------------------(AND)--')

c = a & b
print('Nilai :',c,'Binary :',format(c,'08b'))

print('Nilai :',a,'Binary :',format(a,'08b'))
print('Nilai :',b,'Binary :',format(b,'08b'))

# Bitwise  xor (^)
print('===And (&)')

print('-----------------------(AND)--')

c = a ^ b
print('Nilai :',c,'Binary :',format(c,'08b'))

print('Nilai :',a,'Binary :',format(a,'08b'))
print('Nilai :',b,'Binary :',format(b,'08b'))

# Bitwise  not (~)
print('===And (&)')

print('-----------------------(AND)--')

c =  ~a
print('Nilai :',c,'Binary :',format(c,'08b'))

print('Nilai :',b,'Binary :',format(b,'08b'))
print('Nilai :',a,'Binary :',format(a,'08b'))

d = 0b0000001001
e = 0b1111111111

print('Nilai :',e^d,'Binary :',format(e^d,'08b'))