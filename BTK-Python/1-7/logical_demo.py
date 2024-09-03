#1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

a = input('bir sayı giriniz: ')
result = (int(a) > 0) and (int(a) < 100)
print(result)

#2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

b = input("bir sayı giriniz: ")
result = (int(b) > 0) and (int(b) % 2 == 0)
print(result)

#3- Email ve parola bilgileri ile e mail giriş kontrolü yapınız. 

dogruEmail = "info@kadirdagdas.com"
dogruSifre = "kdag9221"

email = input("e-mail adresinizi giriniz: ")
password = input("şifrenizi belirleyiniz: ")

result = (dogruEmail == email.strip()) and (dogruSifre == password.lower())
print(f'Girdiğiniz e mail {email} ve girmiş olduğunuz şifre {password} olup doğrulama başarı durumu: {result}')

#4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız. 

girSayi1 = input('bir sayı giriniz: ')
girSayi2 = input('ikinci sayıyı giriniz: ')
girSayi3 = input('üçüncü sayıyı giriniz: ')

result1 = girSayi1 > girSayi2
print("birinci sayı ikinci sayıdan büyüktür: ", result1)

result2 = girSayi2 > girSayi3
print("ikinci sayı üçüncü sayıdan büyüktür: ", result2)

result3 = girSayi3 > girSayi1
print("üçüncü sayı birinci sayıdan büyüktür: ", result3)


#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınıız.

vize1 = input('birinci vize notunuz: ')
vize2 = input('ikinci vize notunuz: ')
final = input('final notunuz: ')
ort = float(vize1)*0.3 + float(vize2)*0.3 + float(final)*0.4

#     Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#     a) Ortalama 50 olsa bile fianl notu en az 50 olmalıdır.
#     b) Fianlden 70 alındığında ortalamnın önemi olmasın.

result = ((ort > 50) and (float(final) >= 50)) or (float(final) >= 70)
print(f'Ortalamanız: {ort} ve dersten geçme durumunuz {result}')

#6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#     (Formül: Kilo / Boy uzunluğunun karesi)
#     Aşağıdaki tabloya göre kişi hangi gruba girmelidir? 
#     0 - 18.4    = Zayıf
#     18.5 - 24.9 = Normal
#     25.0 - 29.9 = Fazla Kilolu
#     30.0 - 34.9 = Obez

isim = input('adınız soyadınız: ')
kilo = input('kilonuz: ')
boy = input('boyunuz: ')

indeks = float(kilo) / float(boy)**2

zayıf = 0 < indeks < 18.5
normal = 18.5 < indeks < 24.9
kilolu = 25.0 < indeks < 29.9
obez = 30 < indeks < 34.9

print(f'Sevgili {isim}; verilerinize göre durumunuz: Zayıfsınız: {zayıf}, Normalsiniz: {normal}, Kilolusunuz: {kilolu}, obezsiniz {obez}')