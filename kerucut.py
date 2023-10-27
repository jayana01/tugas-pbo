print("Program Python Hitung Volume dan Luas Permukaan Kerucut")
"""
Programmer : Jayana
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""

pi    = 22/7
jari   = float(input("Masukan Jari-jari Lingkaran : "))
tinggi   = float(input("Masukan Tinggi Kerucut : "))
pelukis =((jari*jari)+(tinggi*tinggi))
volume   = 1/3*pi*(jari*jari)*tinggi
luas   = pi*jari*(jari+pelukis)

print("\n-----------------Hasilnya-----------------")
print("Volume Kerucut =","{:.2f}".format(volume)) 
print("Luas Permukaan Kerucut =","{:.2f}".format(luas))