sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ile ekrana yazdırın.
'''
x = 0
while x < len(sayilar):
    print(sayilar[x])
    x += 1
'''
# 2- Başlangıç ve bitiş değerlerini kullancıdan alıp aradaki
# tüm tek sayıları ekrana yazdırın.
'''    
a = int(input('başlangıç sayısı giriniz: '))
b = int(input('bitiş sayısı giriniz: '))

x = a

while a <= x <= b:
    if x % 2 == 1:
        print(x)
    x += 1
'''
# 3- 1-100 arasındaki sayıları azlan şekilde yazdırın.
'''
x = 100

while 1 <= x <= 100:
    print(x)
    x -=1
'''
# 4- Kullanıcıdan aldığınız 5 sayıyı ekranda sıral bir şekilde yazdırın:
'''
numbers = []

x = 0

while x < 5:
    sayi = int(input('bir sayı giriniz: '))
    numbers.append(sayi)
    x += 1

numbers.sort()

print(numbers)

'''
# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız
#     *ürün sayısını kullanıcıya sorun.
#     ** dictionary listesi yapısı (name, price) şeklinde olsun. 
#     *** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin. 

urunSayisi = int(input('ürün sayısını giriniz: '))
urunler = []
x = 0

while x < urunSayisi:
    name = input('ürünün adını giriniz: ')
    price = float(input('ürünün fiyatını giriniz: '))
    urun = {'isim' : name, 'fiyat': price}
    urunler.append(urun)
    x += 1

for a in urunler:
    print(f"ürün adı: {a['isim']}, ürünün fiyatı {a['fiyat']}")
    