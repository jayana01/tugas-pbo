print("Program Python Hitung Volume dan Luas Permukaan Bola")
"""
Programmer : Jayana
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""

pi    = 22/7
jari   = float(input("Masukan Jari-jarinya : "))
volume   = 4/3*pi*(jari*jari*jari)
luas   = 4*pi*(jari*jari)

print("\n-----------------Hasilnya-----------------")
print("Volume Bola =","{:.3f}".format(volume)) 
print("Luas Permukaan Bola =","{:.3f}".format(luas))