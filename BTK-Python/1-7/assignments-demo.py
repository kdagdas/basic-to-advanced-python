x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

#1- Kullanıcıdan aldığınız 2 sayının çarpımmı ile x,y,z toplamının farkı nedir?
kullanici1 = input('bir sayi giriniz: ')
kullanici2 = input('ikinci sayıyı giriniz: ')
carpim = int(kullanici1) * int(kullanici2)
xyzToplam = x + y + z
result = carpim - xyzToplam
print(result)

#2- y'nin x'e kalansız bölümünü hesaplayınız.
a = y
a //= x 
print(a)

#3- (x,y,z) toplamınn mod 3'ü nedir?
xyzToplam %= 3
print(xyzToplam)

#4- y'nin x. kuvvetini hesaplayınız.
b = y
b **= x
print(b)

#5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır?
x, *y, z = numbers
print(z**3)

#6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
c = sum(y)
print(c)