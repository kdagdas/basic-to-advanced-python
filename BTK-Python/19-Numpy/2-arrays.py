import numpy as np

result = np.array([1,3,5,7,9])

# Elemanları kendimiz belirtmek istemediğimiz zaman:
result = np.arange(1,10) # 1'den 10'a kadar bir eleman oluştur (1 dahil, 10 dahil değil)
# print(result) # [1 2 3 4 5 6 7 8 9]
result = np.arange(10,100,10) # artış miktarı 3'er olacak şekilde 10'dan 100'e eleman oluştur.
# print(result) # [10 20 30 40 50 60 70 80 90]
result = np.zeros(10) #10 tane float 0'lardan oluşan bir eleman listesi
# print(result) # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
result = np.ones(10) # 10 tane float 1'lerden oluşan bir eleman listesi
# print(result) # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
result = np.linspace(10, 100, 5) # başlangıç ve bitiş arasındaki sayıları 5 parçaya böler
# print(result) # [ 10.   32.5  55.   77.5 100. ]
result = np.linspace(0, 5, 5)
# print(result) # [0.   1.25 2.5  3.75 5.  ]


# NP kütüphanesi içinde de random dosyası bulunmaktadır.
result = np.random.randint(0,10) # 0 ile 10 (dahil değil) arasında rastgele bir tam sayı üretir

result = np.random.randint(20) # başlangıcı 0 kabul ederek üst değeri 20 alır.

result = np.random.randint(1,10,3) # 1 ile 10 arasında rastgele 3 sayı

result = np.random.rand(5) # 0 ile 1 arasında 5 tane sayı üretir.
result = np.random.randn(5) # -1 ile 1 arasında 5 tane sayı üretir.


# array ve matrislerle çalışma
np_array = np.arange(50)
np_multi = np_array.reshape(5,10) # 5 satır ve 10 sütunluk bir matris
'''
print(np_multi.sum(axis=1)) # matrisin satırlarn toplamını verir: [ 45 145 245 345 445]
print(np_multi.sum(axis=0)) # matrisin sütunların toplamını verir: [100 105 110 115 120 125 130 135 140 145]
'''

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max() # üretilen sayılar içindeki en büyük sayı
result = rnd_numbers.min() # üretilen sayılar içindeki en küçük sayı
result = rnd_numbers.mean() # üretilen sayıların ortalaması
result = rnd_numbers.argmax() # üretilen en büyük sayının indexi


print(result)






