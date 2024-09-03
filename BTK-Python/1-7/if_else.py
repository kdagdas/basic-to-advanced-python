# if bloklarında bir True veya False sonucu çıkmalı ki blok çalışsın 
# aynı zamanda if bloğu kapsamındaki kod satırları da bir içe girintili yazılır.

if 3 > 2:
    print('Hoş Geldiniz') #bu 3, 2'den büyükse 'Hoş Geldiniz' yazdır demektir.

isLoggedin = True #Kullanıcı doğru giriş yaptı mı demektir.
if isLoggedin:
    print('Doğru şekilde giriş yaptınız.')

#Bazen durum False çıkarsa da kullanıcıya bir sonuç göstermek isteriz
#Bunun için de 'else' operatörünü kullanırız.

username = 'kdagdas'
password = 'abc1234'

girUsername = input('kullanıcı adınızı giriniz: ')
girPassword = input('şifrenizi giriniz: ')

isLoggedin = (username == girUsername.lower().strip()) and (password == girPassword.lower())
print(isLoggedin)
if isLoggedin:
    print('kullanıcı adı ve parolanız doğru, giriş yapıldı')
else:
    print('kullanıcı adı veya paralonazın hatalı, lütfen yeniden deneyin.')

#Kullanıcılar 'kullanıcı adı mı parola mı yanlış bilmek isterler.
#Bu gibi durumlarda iç içe if blokları çalıştırabiliriz:

if girUsername == 'kdagdas':
    if girPassword == 'abc1234':
        print('Hoş Geldiniz')
    else:
        print('parola hatalı')
else:
    print('kullanıcı adı hatalı')

