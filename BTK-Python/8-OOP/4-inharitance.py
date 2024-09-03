#INHERITANCE (KALITIM): Class'ların birbirinden miras almasıyla ortaya çıkan bir durumdur:

# Person => name, lastname , age ,eat(), run(), drink()
# Student(Person), Teacher(Person)

# Yukarıdaki örnekteki gibi Person class'ına ait objeler ve metodlar tanımlamış olabiliriz.
# Yine bunun gibi alttaki Student ve Teacher class'larında da aynı şekilde objeler ve
#metodlar tanımlamak için yeniden tanım yapmak yerine Person class'ından miras alırız.
# Daha sonra Student ve Teacher için kendine ait attribute'lar da eklenebilir.

# Animal => Dog(Animal), Cat(Animal) 
'''
class Person:
    def __init__(self):
        print('Person Created')

class Student(Person):
    def __init__(self):
        Person.__init__(self)  # Hem student hem de person class'larını init komutu çalışsın istersem
        print('Student Created') # Student'in init'i önceliklidir.

p1 = Person()
s1 = Student()
'''
# Bunu bir örnekle gösterelim:

class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

class Student(Person):
    def __init__(self, fname, lname, cnummer):
        Person.__init__(self, fname, lname)
        self.classNummer = cnummer
        print('Student Created')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname) 
        #Person.__init() yerine kullanılır, yeniden self yazmaya gerek yoktur.
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher.')

p1 = Person('Ali' , 'Yılmaz')
s1 = Student('Çınar' , 'Turan', 210503067)
t1 = Teacher('Ayla', 'Yılmaz', 'English')

t1.who_am_i()

print(f"Velinin adı {p1.firstName} {p1.lastName}")
print(f"Öğrencinin adı {s1.firstName} {s1.lastName} ve numarası: {s1.classNummer}")
