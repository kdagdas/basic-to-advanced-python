# Generators, bellekte yer işgal etmeyen bir Iterator üretir.
# Eğer bir elemana yalnızca o anda ulaşmak istiyorsak ve daha sonra onunla işimiz yoksa
#generator objeleri kullanmalıyız.

'''
def cube():
    result = []

    for i in range(5):
        result.append(i**3)
    return result

print(cube()) # Oluşan liste şu anda bellekte bir yer tutuyor.
'''
# Amacım sadece oluşan listeyi ekrana yazdırmaktı. Sadece ekrana yazdıracağım liste için
#listenin ramde yer tutarak kaynaklarımı tüketmesine gerek yok. Listelerin her zaman 5
#sayıdan ibaret olmadığını ve zaman zaman içinde bir sürü bilgi olan devasa listeler
#ile çalışacağımzı unutmamalıyız.

def cube():
    for i in range(5):
        yield i ** 3

#print(cube())

# yield keywordü ile bir değer üretiyorum ve onun küpünü alıyorum ancak bu değerler
#bir yerde saklanmıyor. Dolayısıyla yeniden ulaşmak istediğim zaman ulaşamıyorum. 

# Generator objelerin asıl amacı zaten iteratorler oluşturarak bizim bunlar arasında
#gezebilmemizi sağlamak. Peki bunlar arasında nasıl geziyoruz?

generator = cube()

'iterator = iter(generator)'
# Aslında generator obje kendi kendini iterable hale getiriyor o yüzden yeniden iter()
#fonksiyonuna ihtiyacımız yok.

for i in cube():
    print(i)

# Generator objeleri yalnızca 'yield' keywordü ile kullanmak zorunda değiliz.
    
liste = [(i**3) for i in range(5)] #for döngüsü ile liste yazmanın başka bir yoluydu
print(liste) # Çıktı = 0,1,8,27,64

# Eğer listenin köşeli parantezleri yerine normal parantezler kullanırsak bu generator
#obje haline gelir.

liste = ((i**3) for i in range(5))
print(liste) # <Çıktı = generator object>
