# FONKSİYONDAN FONKSİYON DÖNDÜRME:

# normalde fonksiyonlardan bir değer döndürüyor ve o değeri kullanıyorduk. Burada göreceğimiz
# çalışma ile fonksiyonlardan fonksiyon döndürmeyi öğreneceğiz.
'''
def us_alma(number):

    def inner(power):
        return number ** power
    
    return inner


two = us_alma(2)
print(two(3)) # Çıktı = 2**3'ten = 8

# us_alma(2) fonksiyonu ile dış fonksiyon ve iç fonksiyonda number olan yerlere 2 yazıldı
# ancak iç fonksiyon bizden bir 'power' değerini de istiyor. Bu fonskiyonların bu haliyle
# kalmış olmaları 'two' değişkenine atanmış. Daha sonra 'two' değişkenine de bir sayı
# verildiği zaman bu 'power' yerine yazılıyor ve sonuç döndürülmüş oluyor.

three = us_alma(3)
print(three(3)) # Çıktı = 3**3'ten = 27
'''
# Şmdi başka bir örnek yapalım:

# Kullanıcı bir sayfaya gitmek istiyor ancak kullanıcının rolüne göre gitmek istediği sayfa
# farklı olacak. (örneğin adminse admin paneline, editörse editör paneline gidecek)
'''
def yetki_sorgula(page):
    def inner(role):
        if role == 'admin':
            return f'({role} rolü {page} sayfasına ulaşabilir)'
        else:
            return f'({role} rolü {page} sayfasına ulaşamaz.)'
    return inner
        
user1 = yetki_sorgula('Product Edit')
print(user1('user'))
'''

# Birden fazla fonksiyon döndürelim:

def islem(islem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim
    
    if islem_adi == 'toplama':
        return toplama
    else:
        return carpma
    
toplama = islem('toplama')
print(toplama(1,3,5,6,7))

carpma = islem('carpma')
print(carpma(1,2,3,6,4))