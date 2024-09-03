#range() metodu:

#bir listedeki elemanları yazdırmak for döngüsü ile kolaydır.
#Elimizde liste yoksa range() metodu ile bir liste oluşturulabilir.

for item in range(10): #0 başlayarak  10'a kadar bir liste oluşturur.
    print(item)

#istersek başlangıç noktası da verebiliriz:

for item in range(2,10):
    print(item)

#range() metodunu döngü dışında list() fonksiyonu ile kullandığımızda bir dizi sonucu alırız.
#istersek sayıların kaçarlı artmasını da isteyebiliriz. (start, stop, step):

dizi = list(range(10,100,10)) #10'dan başla 10'ar git ve 100 dahil olmasın demektir.
print(dizi)


#enumerate metodu:

greeting = 'Hello'

for letter in greeting:
    print(letter)  #Her karakteri ayrı ayrı yazdıracaktır.

# Bu karakterlerin indeksine ulaşmak istersem 'enumerate' metedunu kullanabilirim.
# enumarete kullanmadan bu işlemi nasıl yaparım:
    
index = 0

for letter in greeting:
    print(f"index: {index}, eleman: {letter}")
    index += 1

#ben yine index değişkeni tanımlamadan enumerate metodu ile bunu yapabilirim:

for letter in enumerate(greeting):
    print(letter) #önce index sonra eleman şeklinde (0, 'H') şeklinde bir çıktı alırız.

#eğer indeks ve eleman değerlerini ayrı ayrı yazdırmak istersem for döngüsüne
#bir değişken daha atamam gerekir:
    
for indeks, letter in enumerate(greeting):
    print(f'indeks: {indeks}, eleman: {letter}')


#zip() metodu:
    
list1 = [1, 2, 3, 4, 5]

list2 = ['a', 'b', 'c', 'd', 'e']

#elimizde dictionary listesi bulunmadığını ve bu şekilde iki listenin birbirine karşılık
#gelmesi gereken durumlarda [örneğin bir isim listesi ve telefon numaraları gibi]
#birleştirmemiz gerekirse zip() metodunu kullanabiliriz. 

print(list(zip(list1, list2)))

#daha fazla listede bir araya getirilebilir ancak yeni oluşacak liste en az elemanlı
#listedeki kadar elemana sahip olur, diğerleri yazdırılmaz:
list3 = ['bir' , 'çocuk' , 'var']

print(list(zip(list1, list2, list3)))

#for döngüsü içinde de zip metodu kullanılabilir.

for item in zip(list1, list2):
    print(item)
    
#sadece birinci listenin elemanlarını almak istersem birden fazla değişken tanımlayabilirim:

for a, b, c in zip(list1, list2, list3):
    print(a)

#veya liste içinden çıkartıp hepsini ayrı ayrı da yazdırabilirim: 

for a, b, c in zip(list1, list2, list3):
    print(a, b, c)
