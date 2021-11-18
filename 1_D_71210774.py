# Ronand Joy
# UG 10
# variable

a = int(input("Masukkan harga makanan sebesar Rp "))
b = int(input("Masukkan harga snack sebesar Rp "))
c = int(input("Masukkan harga minuman sebesar Rp "))
d = int(input("Masukkan uang yang anda bawa Rp "))

Total_Harga = a + b + c
utang = Total_Harga - d
kembalian = d - Total_Harga 
print("Total yang harus anda bayar sebesar Rp ", Total_Harga)

if d < Total_Harga :
 print("Uang Anda kurang! Anda memiliki utang sebesar Rp ", utang)

elif d == Total_Harga : 
 print("Uang anda pas! Tidak ada kembalian dan Utang :D")

elif d > Total_Harga :
 print("Anda memiliki kembalian sebesar Rp ", kembalian) 
