# format string


# contoh generic

#string

nama = "ucup"
format_str = f"hello {nama}"
print(format_str)


# boolean

boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

#bilangan bulat

angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)


# bilangan dengan ordo ribuan

angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)


# bilangan desimal

angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)


# menampilkan leading zero

angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)


# menampilkan tanda + atau -

angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# memformat persen

persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)