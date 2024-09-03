# FONKİSYON PARAMETRELERİ:

def changeName(n):
    n = 'ada'

name = 'yiğit'

changeName(name)
print(name)

def change(n):
    n[0] = 'istanbul'

sehirler = ['ankara', 'izmir']

change(sehirler)
print(sehirler)

# Ne yapmış olduk? alttaki 'change(sehirler)' komutu ile birlikte yukarıdaki fonksiyonda
# tanımlanmış olan n değişkenine n = sehirler demiş oluruz. sehirlerin birinci indeksi de
# 'istanbul' olduğu için sehirler listesi ['istanbul', 'izmir'] şeklinde değişmiş olur.

# fonksiyon içine aktarım yaptığımızda elemanları kopyalamış olmayız.
# elemanların adreslerini kopyalamış oluruz. Bunun yerine elemanları kopyalamak isteseydik:

n = sehirler[:] #listenin bütün elemanlarını kopyalamak demektir. (slicing yapmak)
print(sehirler) #şeklinde yapmamız gerekir

# aynı şekilde 'change(sehirler(:))' komutu ile de adres kopyalama yerine 
# eleman kopyalama yapılabilir. bu şekilde orijinal liste saklanmış olur.

def add(a, b, c = 0  ):
    return sum((a, b, c)) #sum python kütüphanesiyle gelen toplama fonksiyonudur.

print(add(10, 20))
print(add(10, 20, 30))

#yukarıda olduğu gibi fonksiyonu bazen iki bazen üç parametreli kullanmak istersem
#c = 0 diyerek c'nin belirtilmediği durumlarda c'yi sıfır olarak alabilir.

# parametre sayısı sürekli değişkense ve istediğim kadar parametre girmek istersem
# "*parametreAdi" şeklinde yıldızla bir değişken ismi belirterek fonksiyonu kullanabiliriz:

def add(*params):
    return sum(params)

print(add(20, 300, 45, -10))
print(add(30, 60, 90))
print(add(42, 32, 21))

#veya sum fonksiyonu olmadan:

def add(*params):
    sum = 0
    for n in params:
        sum += n
    return sum

print(add(20, 300, 45, -10))
print(add(30, 60, 90))
print(add(42, 32, 21))

# şimdiye kadar parametreler hep int tipindeydi. Parametreler farklı tipte olsalardı:
# bunun için parametrenin bir liste olması gerekir. Bu tipte verileri genellikle 
# dictionary listeler ile saklıyorduk. İsim ve maaş gibi...

def displayUser(**args): #gönderdiğimiz parametrelerin bir tuple değil de dictionary olduğunu
                         #belli etmek için '**' kullandık. değişken ismi önemli değil.
    for key, value in args.items():
        print(f'{key} is {value}')

displayUser(name = 'Çınar', age = 2, city = 'istanbul')
displayUser(name = 'Ada', age = 12, city = 'kocaeli', phone = '123123')
displayUser(name = 'Yiğit', age = 14, city = 'kocaeli', phone = '123132', mail = 'yigit@gmail.com')

# key ve value parametrelerini tek bir fonksiyona gönderirsek ne olur?

def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10, 20, 30, 40, 50, key1 = 'value1', key2 = 'value 2')
