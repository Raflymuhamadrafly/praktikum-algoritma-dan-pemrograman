print("data =",data_str,",type =",type =(data_str)))

data_int = int(data_str) # string harus angka
data_float = float(data_str) # string harus angka
data_bool = bool(data_str) # false jika string kosong
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_bool, ",type =",type(data_bool))
# input user

# data yang dimasukan pasti string
data = input("Masukan data: ")

print("data = ",data,",type =",type(data))

# jika kita ingin mengambil int, maka
angka = float(input("masukan angka: "))
angka = int(input("masukan angka: "))

print("data = ",angka,",type =",type(angka))

#bagaimana dengan boolean
biner = bool(int(input("masukan nilai boolean: ")))

print("data = ",biner,",type =",type(biner))
