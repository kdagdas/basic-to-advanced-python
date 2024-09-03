################### Raising an Exception => Exception Fırlatma ##############

# Kendi oluşturduğumuz fonksiyonlarda girilen veriler ile ilgili bazı hata mesajları
#vermek isteyebiliriz. Örneğin belli bir doğum yılının altında veri kabul etmeyebiliriz.
#Bu gibi durumlarda kendi Exceptionlarımızı fırlatabilmemiz gerekir.
'''
x = 10

if x > 5:
    raise Exception("x 5'ten büyük olamaz.")
'''
#daha gerçekci bir örnek:
'''
def check_password(psw):
    import re #(regular exppression ismindeki bu modül girilen değerlerin
              # üzerinde kontrol sağlar. Örn: küçük-büyük harf, rakam vb.)
    if len(psw) < 7:
        raise Exception('Parola en az 7 karakter olmalıdır.')
    elif not re.search("[a-z]", psw): #eğer parolada küçük harf bulunuyorsa
                                      #False değer gönderir (not ifadesi bulunduğu için)
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam içermelidir.")
    elif not re.search("[_@$]", psw):
        raise Exception("Parola sembol içermelidir.")
    elif re.search(" ", psw): #boşluk karakteri var mı diye kontrol eder.
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print('Geçerli parola')

password = 'Aa_1234567'

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print(f'geçerli parola: {password}')
finally:
    print('validation tamamlandı.')
'''

class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception('name alanı fazla karakter içeriyor.')
        else:
            self.name = name

p = Person('Kadir', 2000)