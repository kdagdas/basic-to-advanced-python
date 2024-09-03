# Numpy dizilerindeki belli elemanlara ulaşma, bölme ve parçalama

import numpy as np

# Tek boyutlu array'de elemanlara ulaşma:
numbers = np.arange(0,80,5)

result = numbers[5] # 5. indeksteki eleman
result = numbers[-1] # sonuncu indeksteki eleman
result = numbers[0:3] # 0. indeksten 3. indekse (dahil değil) elemanlar
result = numbers[:3] # 0. indeksten 3. indekse (dahil değil) elemanlar
result = numbers[3:] # 3. indekten itibaren tüm elemanlar
result = numbers[::] # tüm elemanlar
result = numbers[::-1] # elemanları tersten yazdırma
result = numbers[3:10-1] # 3. indekten 10. indekse kadar ters yönde

# Çok boyutlu array'de (matris) elemanlara ulaşma:

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
print(numbers2)

result = numbers2[2] # 2. indekste bulunan (aslında satır) [50,75,85] eleman dizisi
result = numbers2[0,2] # 0. indekste bulunan (ilk satır) 2. indeksindeki (3. kolon) eleman
result = numbers2[:,2] # tüm satırlardan 3. sütunlardaki elemanlar
result = numbers2[:,0:2] # tüm satırlardan 1. ve 2. sütunlardaki elemanlar
result = numbers2[-1,:] # son satırdaki tüm sütunlar

# print(result)

arr1 = np.arange(0,10)
arr2 = arr1 # referans kopyalama yani aynı adreslere sahip
print(arr1) # [0 1 2 3 4 5 6 7 8 9]
print(arr2) # [0 1 2 3 4 5 6 7 8 9]

arr2[0] = 20 # 0. indeksteki elemanı 20 ile değiştirdik.

print(arr1) # [20 1 2 3 4 5 6 7 8 9]
print(arr2) # [20 1 2 3 4 5 6 7 8 9]
#değişikliği sadece arr2 için yapmış olmammıza rağmen her iki dizi de değişti

# referans kopyalamak istemiyorsak:
arr2 = arr1.copy() # arr1 ve arr2 farklı adreslere sahip olmuş oldu
arr2[0] = 30

print(arr1) # [20 1 2 3 4 5 6 7 8 9]
print(arr2) # [30 1 2 3 4 5 6 7 8 9]





