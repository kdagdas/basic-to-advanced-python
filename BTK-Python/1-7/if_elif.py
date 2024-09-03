#Bazen sadece 2 sonuçlu durumlar ortaya çıkmaz
#Daha fazla olasılıklı durumlar için 'elif' operatörü kullanılır.

x = float(input('bir sayı giriniz: '))
y = float(input('ikinci sayıyı giriniz: '))

# "x" y'den büyük olabilir, küçük olabilir ama eşit de olabilir:
#aynı zamanda x çift de olabilir tek de...

if x > y:
    print("x y'den büyüktür")
elif x == y:
    print("x y'ye eşittir")
else:
    print("y x'ten büyüktür")


num = int(input('sayı: '))
if num > 0:
    print('sayı pozitif')
elif num < 0:
    print('sayı negatif')
else:
    print('sayı sıfır')