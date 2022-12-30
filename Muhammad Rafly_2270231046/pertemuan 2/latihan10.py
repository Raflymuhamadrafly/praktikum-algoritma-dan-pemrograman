x=5 #ini adalah assignment membuat object
y=5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)
#NOT
print('====NOT====')
a=False
c=not a
print('data a=',a)
print('-------- NOT')
print('data c=',c)
#OR (jika salah satu true, maka hasilnya adalah true)
print('====OR====')
a=False
b=False
c=a or b
print(a,'OR',b,'=',c)
a=False
b=True
c=a or b
print(a,'OR',b,'=',c)
a=True
b=False
c=a or b
print(a,'OR',b,'=',c)
a=True
b=True
c=a or b

print(a,'OR',b,'=',c)
#AND (jika dua buah nilai true, maka hasil true)
print('====AND====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)

# XOR (akan true jika salah satu true, sisanya false)
print('====XOR====')
a = False
b = False