#Data interger
print("===INTERGER===")
data_int = 9.9
print("data =", data_int,",type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika int = 0
print("data =", data_float, ",type =",type(data_float))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_bool, ",type =",type(data_bool) )

#Data float
print("===FLOAT===")
data_float = 0
print("data =", data_float, ",type =", type(data_float))

data_int = int(data_float) #Akan di bulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #Akan false jika nilai float = 0
print("data =", data_int, ",type =",type(data_int))
print("data =", data_str, ",type =",type(data_str))
print("data =", data_bool, ",type =",type(data_bool))

#Data boolean
print("===BOOLEAN===")
data_bool = 0
print("data =", data_bool, ",type =", type(data_bool))

data_int = int(data_bool) #Akan di bulatkan ke bawah
data_str = str(data_bool)
data_float = bool(data_bool) #Akan false jika nilai float = 0
print("data =", data_int, ",type =",type(data_int))
print("data =", data_float, ",type =",type(data_float))
print("data =", data_str, ",type =",type(data_str))

#Data string
print("===STRING===")
data_str = 1
print("data =", data_str, ",type =", type(data_str))

data_int = int(data_str) #Akan di bulatkan ke bawah
data_float = str(data_str) #String wajib angka
data_bool = bool(data_str) #Akan false jika string 0
print("data =", data_int, ",type =",type(data_int))
print("data =", data_float, ",type =",type(data_float))
print("data =", data_bool, ",type =",type(data_bool))


