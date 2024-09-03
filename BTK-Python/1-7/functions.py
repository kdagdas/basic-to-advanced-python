# Fonksiyon tanımlarken anahtar kelimemiz define'ın (tanımlama) kısaltması olan "def'tir" 
# Daha sonra fonksiyonun ismi belirlenir.
# Tıpkı metodlardaki gibi parantez aç kapa yapılır.
# Döngülerde olduğu gibi : eklendikten sonra alt satıra girintili olarak kodlar yazılır.
# Bu, kodların fonksiyon üyesi olduğunun göstergesidir.

def sayHello(): 
    print('Hello')

sayHello()

#fonksiyona dışarıdan parametre de gönderebiliriz:

def sayHello(name):
    print('Hello ' + name)

sayHello('Kadir')
sayHello('Nazire')

#parametre belirtilmediyse yine fonksiyonun çalışması için parametreyi başka bir şeye eşleyebiliriz.

def sayHello(name = 'user'):
    print('Hello ' , name)

sayHello('Kadir Dağdaş')  # Hello Kadir Dağdaş
sayHello()  #Hello user

# return komutu ile yazılan kodların yeniden fonksiyona gönderilmesi sağlanarak fonksiyon
# aslında öyle yazılmış gibi tanımlanabilir:

def sayHello(name = 'user'):
    return 'Hello ' + name #bu şu gibi oldu sayHello(f'Hello {name}')

print(sayHello('Çınar'))

# girilen sayıların toplayan bir fonksiyon hesaplayalım:

def total(num1, num2):
    return num1 + num2

result = total(10, 20)
result = total(20, 30)
print(result)

# bir de yaş hesaplama fonksiyonu yapalım: 

def yasHesapla(dogumYili):
    return 2023 - dogumYili

yas = yasHesapla(1990)
print(f"Yaşınız: {yas}")

yas = yasHesapla(2000)
print(f"Yaşınız: {yas}")

#Emekliliğe ne kadar kaldı:

def EmekliligeKacYilKaldi(dogumYili, isim):
    
    '''
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
    INPUT: Doğum Yılı
    OUTPUT: hesaplanan yıl bilgisi
    '''

    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"emeliliğinize {emeklilik} yıl kaldı")
    else:
        print(f"zaten emekli oldunuz!")

EmekliligeKacYilKaldi(1983, 'Ali')
EmekliligeKacYilKaldi(1950, 'Ahmet')

print(help(EmekliligeKacYilKaldi)) #Yukarıda yorum satırları içinde kalan bilgileri yazdırırır.