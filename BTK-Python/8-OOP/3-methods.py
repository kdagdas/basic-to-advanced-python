'''
class Person:
    # class attributes
    address = 'no information'
'''   
    #constructor (yapıcı metod)
'''
    def __init__(self, name, year):
'''    
        # object attributes
'''
        self.name = name
        self.year = year
'''    
    # instance methods
'''
    def intro(self):
        print('Hello There, I am ' + self.name)

    def calculateAge(self):
        return 2019 - self.year
'''
# object (instance)
'''
p1 = Person(name = 'Ali', year = 1990)
p2 = Person(name = 'Yağmur', year = 1995)

p1.intro()
p2.intro()

print(f"Benim adım {p1.name} ve yaşım: {p1.calculateAge()}")
'''
##############

class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yariCap = 1): #yaricap verilmediği durumda 1'e eşit olacak.
        self.yariCap = yariCap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yariCap
    
    def alan_hesapla(self):
        return self.pi * (self.yariCap**2)
    
c1 = Circle()
c2 = Circle(5)

print(f'c1 objesi için = alan: {c1.alan_hesapla()} ve çevre: {c1.cevre_hesapla()}')
print(f'c2 objesi için = alan: {c2.alan_hesapla()} ve çevre: {c2.cevre_hesapla()}')




