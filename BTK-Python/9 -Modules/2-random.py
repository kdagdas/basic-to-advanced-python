import random

# result = dir(random)
# result = help(random)

result = random.random() #varsayılan olarak 0.0 - 1.0 arasında rastgele bir sayı üretir.
result = random.uniform(10, 100) # 10 ile 100 arasında sayılar üretir.
result = int(random.uniform(10, 100)) #ondalık kısımlarını atmak için int metodu kullanaabiliriz.
result = random.randint(10,100) #yukarıdakinin metod karşılığıdır. ondalık kısmını atar.

#random metodu ile bir liste içinden de rastgele eleman seçimi yapılabilir:

names = ['ali', 'yağmur', 'deniz', 'cenk']
result = names[random.randint(0, len(names)-1)]

# Fakat random modülü içine zaten bu iş için bir fonk. eklenmiş:

result = random.choice(names) #verilen liste içinden rastgele bir eleman seçimi yapar.

liste = list(range(10)) #liste isminde 0'dan başlayan 10 elemanlı bir liste oluşturulur.
random.shuffle(liste) #bu listenin karışık olarak listelenmesini sağlar.

result = liste

#shuffle metodu normalde liste elemanlarının yerini değiştirmek için kullanılan bir metoddur.
#ancak random modülü ile birlikte her çağırmada liste elemanları yendien karışır ve
#öyle yazdırılır.

liste = range(100)
result = random.sample(liste, 3) # belirtilen liste içerisinden belirlenen sayı kadar
                                 #eleman seçimi yapar.

print(result)