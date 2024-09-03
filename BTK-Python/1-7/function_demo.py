# 1- Göderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
'''
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir('Kadir Dağdaş\n', 3) #'\n' ifadesi yeni satıra geç anlamına gelir.
'''
# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listye çeviren fonksiyon yazınız.

def listeyeCevir(*params):
    liste = []

    for param in params:
        liste.append(param)

        print(liste)
    # return liste
        
listeyeCevir(10, 20, 30, 'Merhaba')
# result = listeyeCevir(10, 20, 30, 'Merhaba')
# print(result)

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulunuz.
'''
def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1): #sayi2'yi de işin içine katmak için +1 ifadesi kullandık.
        if sayi > 1:
            for i in range(2, sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)

sayi1 = int(input('bir sayı giriniz: '))
sayi2 = int(input('ikinci sayıyı giriniz: '))

asalSayilariBul(sayi1, sayi2)

# 4- KEndisinie gönderile bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

def tamBolenleriBul(sayi):
    tamBolenler = []
    
    for i in range(2, sayi):
        if sayi % i == 0:
            tamBolenler.append(i)

    return tamBolenler

result = tamBolenleriBul(20)
print(result)
'''