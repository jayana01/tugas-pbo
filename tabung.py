print ("Program Menghitung Volume dan Luas silinder atau tabung")
"""
Programmer : Jayana
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""
pi    = 22/7
jari   = float(input("Masukan Jari-jarinya: "))
tinggi = float(input("Masukan Tinggginya: "))
volume = pi*jari*jari*tinggi
luas   = 2*pi*jari*(jari+tinggi)

print("-----------------Hasilnya-----------------")
print("Volume Tabung         =","{:.2f}".format(volume))
print("Luas Permukaan Tabung =","{:.2f}".format(luas)) 