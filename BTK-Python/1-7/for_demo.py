sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır?

for a in sayilar:
    if a % 3 == 0:
        print(a)

# 2- Sayilar listesindeki sayıların toplamı kaçtır?

print(sum(sayilar))

#for döngüsüyle

toplam = 0
for sayi in sayilar:
    toplam += sayi #bu "toplam = toplam + sayi" demektir.
print(toplam)

# 3- Sayilar listesindeki tek sayıların karesini alınız.

for tek in sayilar:
    if not tek % 2 == 0:
        print(tek**2)


sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?

for a in sehirler:
    if len(a) <= 5:
        print(a)


urunler = [
    {'name' : 'samsung s6', 'price': 3000},
    {'name' : 'samsung s7', 'price': 4000},
    {'name' : 'samsung s8', 'price': 5000},
    {'name' : 'samsung s9', 'price': 6000},
    {'name' : 'samsung s10', 'price': 7000}
]

# 5 - Ürünlerin fiyatları toplamı nedir?

toplam = 0
for urun in urunler:
    toplam += urun['price']
print(toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz?

for urun in urunler:
    if urun['price'] <= 5000:
        print(urun['name'])