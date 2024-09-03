#CLASS

# class tanımlarken 'class keywordünü kullanırız ve genel kullanımda class'a tanımlanan
# isim büyük harfle başlar.
# class içinde tanımlanan ifadelere attribute denir.
# class tanımladıktan sonra ya bir attribute ya da bir method ekleyerek bir kod yazmamız
#beklenir. Bazen yer tutucu olarak "pass" keywordu kullanılabilir.
'''
class Person:
    pass
'''
#OBJECT / INSTANCE

# Obje tanımlarken değişken tanımlar gibi küçük harfle başlanır ve fonksiyon çağırır gibi
# oluşturulan class bir parantez aç kapa ile çağırılır.
'''
p1 = Person()
p2 = Person()

print(type(p1)) # class Person
print(type(p2)) # class Person
'''

# Class içine attribute tanımlarken iki farklı attribute tipi tanımlayabiliriz.
# 'class attributes' ve 'object attributes'.
# 'object attributes' tanımlarken bir 'constructor' içinde tanımlamamız gerekiyor.
# 'contructor' bir yapıcı metottur ve constructor tanımlamasını fonksiyonlar gibi
#def keywordu ile yaptıktan sonra '__init__()' metodu ile farklı parametreler kullanarak
#objelerle ilgili farklı özellikleri parametrelere aktarabiliyoruz.

# (self) metodu class'tan türetilen herhangi bir objeyi temsil eder. self'ten sonra
# hangi attribute'ları (özellikleri) eklemek istiyorsam self'ten sonra parametre olarak
#eklemem gerekiyor.
'''
class Person:
    # class attributes

    #constructor (yapıcı metod)
    def __init__(self, name, year):
    
        # object attributes
        self.name = name
        self.year = year
        
        # methods
'''

'''
p1 = Person('ali', 1990)
p2 = Person('yağmur', 1995)
'''
# parametreleri gönderirken parametrelerin isimlerini de gönderebiliriz:
'''
p1 = Person(name = 'ali', year = 1990)
p2 = Person(name = 'Yağmur', year = 1995)
'''
#yazdırırken:
'''
print(f"p1 için = name: {p1.name}, year: {p1.year}")
print(f"p2 için = name: {p2.name}, year: {p2.year}")
'''
# Bir de class attribute'ları var:
# bir objeyle alakalı olmayan ve her class'ı çağırdığımızda karşımıza çıksın istediğimiz
#özellikler için class attributeleri tanımlanır.

class Person:
    # class attributes
    address = 'no information'
    #constructor (yapıcı metod)
    def __init__(self, name, year):
    
        # object attributes
        self.name = name
        self.year = year
        
        # methods

p1 = Person(name = 'ali', year = 1990)

# Bazen bilgileri güncellemek isteriz. bu işleme 'update' denir:

p1.name = 'ahmet'
p1.address = 'Denizli / Türkiye'

print(f"p1 için = name: {p1.name}, year: {p1.year}, adres: {p1.address}")