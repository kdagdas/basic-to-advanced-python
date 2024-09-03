'''
liste = [1,2,3,4,5]

for i in liste:
    print(i)

# döngüler içinde kullandığımız 'liste' konumundaki araçlara iterable objects yani
#'yinelenebilir nesneler' denir.
    
# for döngüsü iterable obje olan "liste'yi" iterator oluşturuyor. Peki biz iterable
#objeleri nasıl iterator hale getireceğiz?
    
iterator = iter(liste) #iter fonksiyonu aracılığıyla bir iterable objeden iterator oluşturuluyor.

print(iterator) # Çıktı = list_iterator object at ....

# Bir iterator üzerinden next() metodu ile dolaşırsak liste içindeki elemanlar 'tek tek'
#karşımıza gelir.

print(next(iterator)) # Çıktı = 1
print(next(iterator)) # Çıktı = 2
print(next(iterator)) # Çıktı = 3
print(next(iterator)) # Çıktı = 4
print(next(iterator)) # Çıktı = 5
print(next(iterator)) # Çıktı = StopIteration

# aslında for döngüsünün arka planı yukarıdaki veya aşağıdaki gibi işliyor:
while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration: #bu hatayı aldığında döngüden çık demek
        break
'''
# Peki Iterator oluşturmak bizim nerede işimize yarayacak?
# Bizde liste gibi class'lar oluşturabiliriz. Burada Iteratorler işimize yarayacak:
    
class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
list = MyNumbers(10,20)
for x in list:
    print(x)

my_iter = iter(list)
print(my_iter)
print(next(my_iter))
print(next(my_iter)) 
print(next(my_iter))
print(next(my_iter))

