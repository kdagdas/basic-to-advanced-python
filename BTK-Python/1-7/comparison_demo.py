# 1- Girilen 2 sayıdan hanigsi büyüktür?
'''
birinciSayi = int(input('bir sayı giriniz: '))
ikinciSayi = int(input('ikinci sayıyı giriniz: '))
result1 = (birinciSayi > ikinciSayi)
print(f'İlk sayı {birinciSayi} ikinci sayıdan {ikinciSayi} büyük müdür?: {result1}')
'''
# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

'''vize1 = float(input("birinci vize sonucu: "))
vize2 = float(input("ikinci vize sonucu: "))
final = float(input("final sonucu: "))

ortalama = (vize1*0.3) + (vize2*0.3) + (final*0.4)

print(f'Not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama >= 50}')
'''
# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

'''girSayi = int(input("Bir sayı giriniz: "))
a = girSayi % 2
b = a < 1
print(f'Girdiğiniz sayı: {girSayi} ve bu sayı çifttir: {b}')'''

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın
'''
girSayi2 = int(input("Bir sayı giriniz: "))
c = girSayi2 < 0
print(f'Girmiş olduğunuz sayı {girSayi2} ve bu sayının negatiflik durumu {c}')
'''
# 5- Parola ve email bilgisini isteyip doğruluğu kontrol ediniz.
#    (email: email@sadikturan.com parola:abc123)

email = input("email'inizi giriniz: ")
password = input("bir şifre oluşturunuz: ")

d = email.strip() == ('email@sadikturan.com')
e = password.lower() == ('abc123')

print(f'girmiş olduğunuz mail: {email}, ve şifreniz {password}, ve mailinizin uyumu {d}, ve şifreniz uyumu {e}')

# şifrelerde büyük küçük harfe dikkat edilmesin istiyorsak password kısmı için .lower() metodu kullanılmalıdır.
# maillerde de sonunda bırakılan boşluklara dikkat edilmesin istiyorsak .strip() metodu kullanılır.