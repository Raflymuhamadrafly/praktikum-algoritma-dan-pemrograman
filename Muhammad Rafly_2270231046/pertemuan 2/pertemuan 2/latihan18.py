#ELIF = else if statement

nama = input("Nama kamyu siapa?")


if nama=="ucup": #kondisi 1

    print("Hai ganteeeeeeng beuds!") # aksi true 1

elif nama =="otong": # kondisi 2

    print("Hai si kece bangeeeets!") # aksi true 2

elif nama == "mario": # kondisi 3
    print("Hai humooooooreeeesh!") #aksi true 3

else: 
    print("au ah gak kenal!!!") #aksi false


print("ini adalah akhir dari program")


# Latihan 

#kalkulator sederhana 

print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")


angka_1 = float(input("masukan angka 1="))
operator = input("operator(+,-,x,/):")
angka_2 = float(input("masukan angka 2 ="))


# percabangannya

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")

elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah hasil {hasil}")

elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")

elif operator == "/":
    hasil = angka_1/angka_2 
    print(f"hasilnya adalah {hasil}")

else:
    print("masukan yang bener dong!, aku pusying")


print("Akhir dari program, terima gajih!")


