#DEĞİŞKENLERİN GLOBAL VEYA LOKAL OLARAK TANIMLANMASI:
'''
x = 'global x'

def function():
    x = 'local x'

function()
print(x) # 'x = global x' sonucu çıkar.
'''
# Çünkü fonksiyonlar kendi içinde farklı bir değişken tanımlama alanı kullanırlar.
# Fonksiyonun içinde tanımlanan değişkenler dışarıyı etkileyemezler.
# Ancak fonksiyonun içine print(x) yazsaydık çıktı olarak: 
# 'local x' ve 'global x' çıktısı vereceklerdi.
'''
#global
name = 'Çınar'

def changeName(new_name):
    #local
    name = new_name
    print(name)

changeName('Ada')
print(name)
'''
###################
'''
name = 'global string'

def greeting():
    name = 'Çınar'
    
    def hello():
        name = 'Ada'
        print('hello ' + name)

    #hello()
greeting()
'''
#fonksiyonun içinde tanımlanan fonksiyonlar da global alanda çalışmayacaktır çünkü onlar da
#aslında local alanda kalmışlardır.
#fonksiyonlara dışarıdan gelen değişkenleri sokabiliriz:
#'name = Ada' olmasaydı 'çınar'ı o da olmasaydı 'global string'i yazdıracaktı.

x = 50
def test(x):
    print(f'x : {x}')

    x = 100
    print(f'changed x to {x}')

test(x) # x : 50 ve changed x to 100
print(x) # 50 çıktılarını alırız.

# Dışarıdaki değişkeni fonksiyon içinden değiştirebilmek için 'global' keyword'ünü
# kullanmamız gerekir:

x = 50
def test2():
    global x
    print(f'x : {x}')

    x = 100
    print(f'changed x to {x}')

test2() # x : 50 ve changed x to 100
print(x) # 50 çıktılarını alırız.