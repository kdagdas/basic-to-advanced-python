# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
# durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
# lise ya da üniversite olmalıdır.
'''
name = input('adınız soyadınız: ')
age = int(input('yaşınız: '))
education = input('eğitim durumunuzu giriniz: ')

result = (age >= 18) and ((education == 'lise') or (education == 'üniversite'))
if result:
    print('ehliyet alabilirsiniz.')
else:
    print('ehliyet alamazsınız.')
'''
#daha detaylı:
'''
if age >= 18:
    if education.lower().strip() == 'lise' or education.lower().strip() == 'üniversite':
        print(f'Sevgili {name}, ehliyet almaya uygunsunuz.')
    else:
        print(f'Sevgili {name}, eğitim durumunuz yeterli değil')
else:
    print(f'Sevgili {name}, yaşınız müsait değil.')
'''
# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
# not aralığına karşılık gelen not bilgisini yazdırınız.
# 0 - 24 => 0
# 25 - 44 => 1
# 45 - 54 => 2
# 55 - 69 => 3
# 70 - 84 => 4
# 85 - 100 => 5
'''
vize1 = float(input('birinci yazılı: '))
vize2 = float(input('ikinci yazılı: '))
final = float(input('final: '))

ort = vize1*0.3 + vize2*0.3 + final*0.4

if 0 <= ort <= 24:
    print(f'Ortalamanız {ort} ve notunuz 5 üzerinden 0')
elif  25 <= ort <= 44:
    print(f'Ortalamanız {ort} ve notunuz 5 üzerinden 1')
elif  45 <= ort <= 54:
    print(f'Ortalamanız {ort} ve notunuz 5 üzerinden 2')
elif  55 <= ort <= 69:
    print(f'Ortalamanız {ort} ve notunuz 5 üzerinden 3')
elif  70 <= ort <= 84:
    print(f'Ortalamanız {ort} ve notunuz 5 üzerinden 4')
else: 
    print(f'Ortalamanız {ort} ve Tebrikler, notunuz 5 üzerinden 5')
'''
# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanınını aşağıdaki bilgilere
# göre hesaplayınız.

#     **Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#     ***datetime modülünü kullanmanız gerekiyor.

#     1. Bakım => 1. yıl
#     2. Bakım => 2. yıl
#     3. Bakım => 3. yıl

yıl = int(input('aracı satın aldığınız yıl: '))
ay = int(input('aracı satın aldığınız ay: '))
gün = int(input('aracı satın aldığınız gün: '))

import datetime
simdi = datetime.datetime.now() #şimdiki zamanı çeviren datetime modülü
arac = datetime.datetime(yıl, ay, gün)

fark = simdi - arac
gun = fark.days

if int(gun) < 365:
    print(f"aracın alımından itibaren geçen süre; {gun} gündür ve araç 1. bakım yılındadır.")
elif 365 <= gun < 365*2:
    print(f"aracın alımından itibaren geçen süre; {gun} gündür ve araç 2. bakım yılındadır.")
elif 365*2 <= gun < 365*3:
    print(f"aracın alımından itibaren geçen süre; {gun} gündür ve araç 3. bakım yılındadır.")
else:
    print(f"aracın alımından itibaren geçen süre; {gun} gündür ve aracın bakım yılı 3 seneyi aşmıştır.")
 

