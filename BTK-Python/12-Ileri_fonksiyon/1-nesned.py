# İÇ İÇE FONKSİYONLAR:

# Fonksiyonlar da objedir.

def greeting(name):
    print('hello', name)
'''
print(greeting('ali')) # Çıktı = hello ali
print(greeting)        # Çıktı = None ve bellek üzerinde bir adresi var, demek ki objedir.
'''

sayHello = greeting
'''
print(sayHello) #bellek üzerindeki adres ikisinin de aynı
print(greeting)
'''
del sayHello #sayHello'yu silmiş olmak adresi silmiş olmak demek değil
print(greeting) #bellek üzerindeki adres gösterilmeye devam eder.
'''
def outer(num1):
    print('outer çalışıyor.')
    def inner_increment(num1):
        print('inner çalışıyor')
        return num1 + 1
    
outer(10) #sadece outer fonk. çağırır. içteki fonksiyonu çağırmaz.
'''
# inner fonksiyonun da çalışması için inner fonksiyonunu outer içinde çağırmak gerekli:
# burada yapılan işleme 'encapsulation' adı verilir.
'''
def outer(num1):
    print('outer çalışıyor.')
    def inner_increment(num1):
        print('inner çalışıyor')
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)
    
outer(10)
#peki dışarıdan inner_increment() fonksiyonunu çağırabilir miyiz?
inner_increment(10) #tanımlanamaz çünkü fonk. içinde olan fonk. içinde kalır.
'''
# Bir örnek daha yapalım:

def factorial(number):
    if not isinstance(number, int): #isinstance komutu verilen bilginin ilgili class'a ait olup olmadığını bildiren bir komuttur.
        raise TypeError('number must be an integer!')
    
    if not number >= 0:
        raise ValueError("number must be zero or positive")
    
    def inner_factorial(number):
        if number <= 1:
            return 1
        
        return number * inner_factorial(number-1)
    
    return inner_factorial(number)
try:
    print(factorial('5'))
except Exception as ex:
    print(ex)

