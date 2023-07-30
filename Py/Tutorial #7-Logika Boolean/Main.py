#Logika or Boolean

#not, or, xor

# Not
print('===NOT===')
 
a = False # true or false, if is true b will false/ if is false b will true
b = not a

print('Data a:',a)

print('Data b:',b)

# Or
print('===OR===')

#1  
a = True
b = False
c = a or b

print(a,'Or',b,'=',c)

#2
a = False
b = True
c = a or b

print(a,'Or',b,'=',c)

#3
a = False
b = False
c = a or b

print(a,'Or',b,'=',c)

#4
a = True
b = True
c = a or b

print(a,'Or',b,'=',c)

# And
print('===And===')

#1  
a = True
b = False
c = a and b

print(a,'Or',b,'=',c)

#2
a = False
b = True
c = a and b

print(a,'Or',b,'=',c)

#3
a = False
b = False
c = a and b

print(a,'Or',b,'=',c)

#4
a = True
b = True
c = a and b

print(a,'And',b,'=',c)
