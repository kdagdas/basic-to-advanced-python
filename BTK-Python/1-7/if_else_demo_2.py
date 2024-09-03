#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
'''
girSayi = int(input('bir sayı giriniz: '))
if 0 < girSayi < 100:
    print('Sayı 0 ile 100 arasında bir sayıdır')
elif girSayi < 0:
    print('Girdiğiniz sayı negatif bir sayıdır.')
elif girSayi == 0:
    print("Girdiğiniz sayı 0'a eşittir.")
elif girSayi == 100:
    print("Girdiğiniz sayı 100'dür")
elif girSayi > 100:
    print("Girdiğiniz sayı 100'den büyüktür.")
'''
#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
'''
girSayi = int(input('bir sayı giriniz: '))
if girSayi > 0:
    if girSayi % 2 == 0:
        print('Sayı pozitif çift sayıdır.')
    else:
        print('Sayı pozitiftir ancak çift sayı değildir.')
elif girSayi == 0:
    print ('sayı 0 olduğu için nötrdür.')
else:
    print('sayı negatif bir sayıdır.')
'''
#3- Email ve parola bilgileri ile e mail giriş kontrolü yapınız. 
'''   
dogruMail = 'info@kdagdas.com'
dogruPassword = 'kadirdagdas'

girMail = input('email adresinizi giriniz: ')
girPassword = input('şifrenizi giriniz: ')

if girMail.strip().lower() == dogruMail:
    if girPassword.strip() == dogruPassword:
        print('başarıyla giriş yapıldı')
    else:
        print('parolanız yanlış')
else:
    print('girdiğiniz email kayıtlı değil')
'''
#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız. 
'''
a = int(input('birinci sayıyı giriniz: '))
b = int(input('ikinci sayıyı giriniz: '))
c = int(input('üçüncü sayıyı giriniz: '))

if a > b > c:
    print(f"en büyük sayı {a} ve en küçük sayı {c}")
elif b > a > c:
    print(f"en büyük sayı {b} ve en küçük sayı {c}")
elif b > c > a:
    print(f"en büyük sayı {b} ve en küçük sayı {a}")
elif a > c > b:
    print(f"en büyük sayı {a} ve en küçük sayı {b}")
elif c > a > b:
    print(f"en büyük sayı {c} ve en küçük sayı {b}")
elif c > b > a:
    print(f"en büyük sayı {c} ve en küçük sayı {a}")
'''

#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınıız.
'''
vize1 = float(input('birinci vize notunuz: '))
vize2 = float(input('ikinci vize notunuz: '))
final = float(input('final notunuz: '))

ort = vize1*0.3 + vize2*0.3 + final*0.4
'''
#     Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#     a) Ortalama 50 olsa bile fianl notu en az 50 olmalıdır.
#     b) Fianlden 70 alındığında ortalamnın önemi olmasın.
'''
if ort >= 50 or final >= 70:
    if final >= 50:
        print(f'Ortalamanız {ort}, Tebrikler dersten geçtiniz!')
    else:
        print(f'Ortalamanız {ort}, finalden 50 ve üstü alamadığınız için dersten geçemediniz.')
else:
    print(f'Ortalamanız {ort}, ortalamanız 50 ve üstü olmadığı, finalden de 70 ve üstü almadığınız için dersten kaldınız.')
'''
#6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#     (Formül: Kilo / Boy uzunluğunun karesi)
#     Aşağıdaki tabloya göre kişi hangi gruba girmelidir? 
#     0 - 18.4    = Zayıf
#     18.5 - 24.9 = Normal
#     25.0 - 29.9 = Fazla Kilolu
#     30.0 - 34.9 = Obez

name = input('adınız soyadınız: ')
wg = float(input('kilonuzu giriniz: '))
hg = float(input('boyunuzu giriniz (m): '))

indeks = wg / hg**2

if 0 < indeks <= 18.4:
    print(f'boy-kilo indeksiniz {indeks} ve durumunuz "ZAYIF"')
elif 18.5 <= indeks <= 24.9:
    print(f'boy-kilo indeksiniz {indeks} ve durumunuz "NORMAL"')
elif 25.0 <= indeks <= 29.9:
    print(f'boy-kilo indeksiniz {indeks} ve durumunuz "KİLOLU"')
elif 30.0 < indeks <= 34.9:
    print(f'boy-kilo indeksiniz {indeks} ve durumunuz "OBEZ"')
else:
    print('hatalı değerler girmiş olabilirsiniz, lütfen kontrol edin.')

    