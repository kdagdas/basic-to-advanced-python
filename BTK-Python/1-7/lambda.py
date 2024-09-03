# gönderilen sayının karesini alan bir fonksiyon yazalım.
'''
def square(num):
    return num **2
'''
# fonksiyon bünyesinde olmasını istediğimiz kodları aynı satıra da yazabiliriz:
'''
def square(num): return num ** 2 #gibi

result = square(2)
print(result)
'''
# elimizde bir liste varsa:
'''
numbers = [1, 3, 5, 9] #bu sayıların karesini almak istersem:
'''
# for döngüsüyle buradaki sayıların her birini çekip square fonksiyonuyla karesini alabiliriz.

# veya "map" metodunu kullanabiliriz.
# map metoduna kullanacağımız fonksiyonun ismini daha sonra liste ismini yazabiliriz.
# yine liste içinde çıkması için liste fonksiyonu içinde yazmamız gerekir.
'''
result = list(map(square, numbers))
print(result)
'''
# veya
'''
for item in map(square, numbers):
    print(item)
'''
# fonksiyona her zaman ihtiyaç duyulmayacak durumlarda ayrı bir yerde tanımlamak yerine
# işlem içinde fonksiyon tanımlanabilir. Buna "lambda expression" denir.
# Tanımladığımız fonksiyon isimsizdir.
# return ifadesi kullanmaya gerek yoktur. 

numbers = [1, 3, 5, 9, 10, 4]

'''result = list(map(lambda num: num ** 2, numbers))'''

#veya bunu fonkisyon dışında yapıp bir değişkene de verebiliriz.
'''
square = lambda num: num ** 2
print(square(3))
'''
# Bazen listedeki her eleman için fonksiyonu çalıştırmak istemeyiz. Bunun için
# filter fonksiyonları kullanırız. Önce normal bir fonksiyon tanımlarız.
# daha sonra filter fonk. ile hangi fonk. çağıracağımızı ve hangi listeye uygulayacağımızı
# belirtiriz.

def check_even(num): return num % 2 == 0

'''result = list(filter(check_even, numbers))''' #map fonksiyonu gibi çalışır.

result = list(filter(lambda num: num % 2 == 0, numbers))

print(result)