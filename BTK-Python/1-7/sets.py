#set listeleri indekslenemez liste türleridir.
#yine süslü parantezle kullanılırlar.

fruits = {'orange', 'apple', 'banana'}

#print(fruits[0]) indekslenemez!
#set listelerin elemanlarına ulaşabilmek için döngü kullanabiliriz.

for x in fruits:
    print(x)

#set listeler sıralanamazlar.
    
#listeye yeni eleman eklemek için .add metodu kullanılabilir:
fruits.add("cherry")
print(fruits)

#birden fazla eleman eklemek için .update veya birkaç adet .add metodu kullanılmalıdır.

fruits.update(['mango', 'tomato', 'grape'])
print(fruits)

#set listelerde elemanlar tekrarlanmaz. Eklemeye çalışsak bile eklenmez

#normal listelerden tekrarlayan elemanları çıkarmak için set komutu kullanılabilir:
#set komutu aynı zamanda listeyi küçükten büyüğe sıralar.

myList = [1, 2, 2, 3, 5, 3, 4]
print(myList)
print(set(myList))

#yine bir eleman kaldırmak için .remove .discard kullanılabilir.

fruits.remove('mango')
print(fruits)

#.pop metodu indekse bağlı çalıştığı için
#.pop set listelere uygulandığında içinden rastgele bir eleman silinmiş olur.

#yine .clear ile tüm elemanları silebiliriz.