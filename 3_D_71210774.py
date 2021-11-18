# Ronand Joy
# UG 10
# variable

a = input("Masukkan daftar belanja Anda : ")
b = a.title() 

print("Daftar belanja : [ ",b,"]")
c = input("Masukkan barang yang ingin ditambahkan : ")

d = c.upper()
e = b + " ",d

if b != c : 
   print("Hasil penambahan pada daftar belanja : ",e )


elif b == c : 
  print("Barang",d.upper(),"sudah berada dalam daftar belanja")   
