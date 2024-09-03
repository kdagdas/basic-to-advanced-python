# Şimdi kendimiz bir modül oluşturalım.
# Önce modül bileşenlerini hazırlayalım.

'''
Modül Hakkında Bilgilendirme
'''

print('Modül Eklendi')

number = 10

numbers = [1,2,3]

person = {
    'name': 'Ali',
    'age': '25',
    'city': 'istanbul'
}

def func(x):
    '''
    Fonksiyon hakkında bilgilendirme
    '''
    print(f'x: {x}')

class Person:
    def speak(self):
        print('I am speaking')

#Bileşenlerimiz hazır şimdi main.py isimli yeni bir sayfa açalım ve
#'import mod' şeklinde oluşturduğumuz modülü sayfaya yükleyelim.