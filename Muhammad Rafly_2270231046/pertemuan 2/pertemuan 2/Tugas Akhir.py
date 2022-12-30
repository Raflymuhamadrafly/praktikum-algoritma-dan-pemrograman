# tugas akhir praktikum

# membuat program aplikasi kasir

print(">>>>>>>>>>>>>>>>> TOKO MOBIL BANG IPUL GANTENG <<<<<<<<<<<<<<<<")


menu = {
    "BMW 320i M Sport": 1.045000000,
    "Tesla Model Y"   : 1.036513405,
    "Hyundai ionic 5 ": 859000000,
    "Hyundai Palisade": 1.000000000,
    "BMW 520i"        : 909000000,
}
print("=====================PRICE LIST MOBIL IPUL==================== ")
for i in menu:
    print("PRICE LIST MOBIL IPUL : ", i ,"\t Harga : ", menu[i])
print("Pembelian diatas 100.000.000 diskon  15%")
print("=========================================")
beli = input("Pilih unit: ")
jumlah = int(input("Jumlah Pesanan"))
bayar = jumlah * menu[beli]

if bayar > 100000000:
    diskon = bayar*15/100
    total = bayar - diskon 
else:
    total = bayar


print("=====================DETAIL PEMBAYARAN, JON==================== ")
print("Menu yang dipesan         : ",beli)
print("Jumlah yang dipesan       : ",jumlah)
print("Total Biaya               : ",bayar)
print("Total yang harus dibayar  : ",total)