# ÖZEL METODLAR:
'''
mylist = [1, 2, 3]
myString = 'my String'

print(len(mylist))  # Çıktı: 3
print(len(myString)) # Çıktı : 9
'''
# len veya type gibi metodlar farklı class'lar için (str veya list gibi) farklı şekillerde
# çalışabiliyorlar.

# aslında bu metodlar python kütüphanesinde önceden oluşturulmuş özel metodlar.
# biz bu metodları kullandıkça kütüphane üzerinden önceden yazılmış kodlar çalışarak
# bu metodların sonuç vermesini sağlıyorlar.

# Biz de bunun gibi kendi class'larımız için özel metodlar tanımlayabiliriz.
mylist = [1, 2, 3]

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu')

    def __str__(self): # str metodu çalıştırıldığında ne olacağını tanımlamış oluyorum.
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print('movie was deleted')

m = Movie('film adı', 'filmin yönetmeni', 120)

# Eğer "def __str__" metodunu tanımlamasaydık print(m) komutu için class'ın ram
# üzerindeki konumu bize çıktı olarak dönecekti.

# __str__ metodunu tanımlayarak print(m) ya da print(str(m)) ifadeleri için çıktıların
# tanımlanan sonucu döndürmesi sağlanır (film adı by filmin yönetmeni)
'''
print(len(mylist))
print(len(m))
'''
# del metodu ile objeler sınıflardan silinebilir:

#del m

print(m)