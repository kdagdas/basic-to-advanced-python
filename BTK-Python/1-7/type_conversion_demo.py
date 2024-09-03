# Daire Alanı : πr²
# Daire Çevresi : 2πr

# Yarı çapı verilen bir dairenin alanını bulunuz. (π=3.14)

yariCap = float(input("yarı çap giriniz: "))
pi = 3.14

alan = pi * (yariCap ** 2)
cevre = 2 * pi * yariCap

print("alan: ", alan)
print("cevre: ", cevre)

print("alan: "+ str(alan) + " cevre: "+ str(cevre))
