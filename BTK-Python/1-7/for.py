# Elimizde bir liste olsun ve bunun elemanlarını tek tek yazdırmak isteyelim
# Bu durumda her bir eleman için liste içinden bir index ile print komutunu
# kullanmamız gerekir (print(my_list[0]) gibi). Eleman sayılarının 50, 100 belki
# daha fazla olduğu durumlarda bu oldukça zor olduğundan "FOR" döngüsünü kullanırız.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers: #kendimize 'num' adında bir değişken ismi seçiyoruz.
    print(num)

# for döngüsü listedeki eleman sayısı kadar dönmeyi sağlar. Bu yüzden yalnızca liste
# elemanlarını yazdırmak için kullanılmaz. Bir şeyi liste eleman sayısı kadar yazdırmak
# için de for döngüsü kullanılabilir:

for num in numbers:
    print('Hello World') #9 kere Hello World çıktısı alırız. 

names = ['çınar' , 'sadık' , 'sena']

for name in names:
    print (f'my name is {name}')

# Peki liste değil de bir str ifade olsa:
    
name = 'sadık turan'

for n in name:
    print(n) #str ifadeler de liste gibi birden çok indekste eleman içerdikleri için
             #name içindeki her bir karakter tek tek yazdırılır.

tuple = ((1, 2) , (3, 4) , (5,6)) #böyle bir tuple listesinde de her bir elemanı yazdırmak
                                  #istersek şu şekilde olur.

for a, b in tuple:
    print(a, b)

d = {'k1' : 1, 'k2' : 2, 'k3' : 3} #böyle bir key value içeren dictionary listesini de yazdırabiliriz.

for item in d:
    print(item) #bize sadece key bilgilerini verir.

#eğer dictionary listelerinde eleman gruplarını yazdırmak istersek:
    
for item in d.items():
    print(item)

#veya tek tek ulaşmak için:
for key, value in d.items():
    print(key, value)