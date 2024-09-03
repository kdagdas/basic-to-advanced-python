#listeler köşeli parantezlerle kullanılırken tuple parantezli veya parantezsiz kullanabilir.

list = [1, 2, 3]
tuple = (1, "iki", 3)

#listelerde olduğu gibi istenilen indeksteki eleman yazdırılabilir.
print(tuple[1])

#len komutu da kullanılabilir:
print(len(tuple))

#listelerden farklı olarak tuple'lara tek bir nesne ataması yapamıyoruz:
'''tuple[2] = uc
print(tuple)''' #çalışmaz

#.count, .index gibi metodlar da tuple üzerinde çalışabilir.,

#tuple'lar da toplanabilir:

names = "Sibel", "Esma", "İrem"
print(names + tuple)
