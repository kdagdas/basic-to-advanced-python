# DECORATOR FONKSİYONLAR:

# Bir fonksiyona bir özellik eklemek istediğimiz zaman kullanılan fonksiyonlardır.

# Bir özelliği birçok farklı yerde kullanmak istiyorsak özelliği bir fonksiyona atayıp
#birden çok yerde kullanabiliriz.
'''
def my_decorator(func):
    def wrapper():
        print("fonksiyondan önce işlemler")
        func()
        print('fonksiyondan sonraki işlemler')

    return wrapper

#özellik eklemek istediğim fonksiyonları tanımlıyorum.

@my_decorator # bu şekilde yazım ile aşağıda yaptığımız atamaları yapmış oluyoruz.
              #ve sayHello() fonksiyonunu my_decorator() içine yazmış oluyoruz.
def sayHello():
    print('hello')

sayHello()
'''
'''
def sayGreeting():
    print("greeting")
'''
# Tanımladığım fonksiyonlar ile özellikleri bağdaştırmam gerekiyor. Yani sayHello() fonksiyonunu
# çağırdığım zaman otomatik olarak wrapper() fonksiyonunda işlem yapması gerekiyor.

# sayHello = my_decorator(sayHello)
# sayHello()
# sayGreeting = my_decorator(sayGreeting)
# sayGreeting()

#DAHA GERÇEKCİ BİR ÖRNEK YAPALIM:

'''
import math
import time #fonksiyonların ne kadar sürede hesaplandığını görmek için time modülü ekliyorum.


def us_alma(a,b):
    
    start = time.time() #başlama zamanı bize gelecek
    time.sleep(1) #fonksiyonun süresini hesaplama açısından 1 saniyeliğine fonksiyonu durdurur
    
    print(math.pow(a,b))
    
    finish = time.time() #bitiş zamanı bize gelecek
    print('fonksiyon ' + str(finish - start) + ' saniye sürdü.')

def faktoriyel(num):
    
    start = time.time()
    time.sleep(1)
    
    print(math.factorial(num))
    
    finish = time.time()
    print('fonksiyon ' + str(finish - start) + ' saniye sürdü.')

us_alma(2,3)
faktoriyel(4)

# Yukarıdaki iki fonksiyon da kendi işlerininin yanında ortak noktaları olarak
# zaman hesaplama yapıyorlar. Bu işlemi daha fazla fonksiyonda kullanmak da isteyebilirim.
# Hesaplama fonksiyonlarını tek tek eklemek yerine sadece fonksiyonlara temel işlemlerini
# yaptırıp zaman hesaplama işlemini başka bir fonksiyona yaptırabiliriz. Bunun için
# tanımladığım fonksiyonların üzerine 'calculate_time()' isminde bir fonksiyon tanımlıyorum.
'''
import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)

        func(*args, **kwargs)

        finish = time.time()
        print('fonksiyon ' + func.__name__ +' '+ str(finish - start) + ' saniye sürdü.')
    
    return inner

@calculate_time
def us_alma(a,b):    
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(*args):
    toplam = 0
    for i in args:
        toplam += i
    print(toplam)


us_alma(2,3)
faktoriyel(4)
toplama(10, 20, 30, -40, 50, 50)