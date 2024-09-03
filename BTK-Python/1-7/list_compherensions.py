#for ve while döngülerine alternatif yöntemler:
'''
for x in range(10):
    print(x) #0'dan 10'a kadar olan sayılar ekrana yazdırılır.

numbers = [x for x in range(10)]
print(numbers) #0'dan 9'a kadar olan bir dizi tanımlaması yapmış olduk. 
'''
#peki bunun yerine döngüler ile ne yapabiliriz:
'''
numbers = []
for x in range(10):
    numbers.append(x)

print(numbers)
'''
#peki döngü sonrasında elemanlara müdahale ederek çıktı almak istesek:
'''
for x in range(10):
    print(x**2)

#yine aynı şekilde yapabiliriz:

numbers = [a**2 for a in range(5)]
print(numbers)
'''
#göngüler içinde farklı döngü veya bloklar kullanabiliyorduk:
'''
for x in range(10):
    if x % 3 == 0:
        print(x**2)

# bu şekildeki döngüleri de yine liste içinde yazdırabiliriz:
        
numbers = [x**2 for x in range(10) if x % 3 == 0]
print(numbers)
'''
#Aynı şeyleri str ifadeler için de uygulayabiliriz.

myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList)

#bir örnekle doğum tarihleri verilen insanların yaşlarını hesaplatalım.

years = [1999, 2008, 1956, 1986]
ages = [2023 - year for year in years]
print(ages)

#bazen yazdırırken if bloğu kullanabiliriz:

result = [x if x % 2 == 0 else 'tek' for x in range(1,10)]
print(result)

#burada tek olanları yazdırma demedik, eğer x çiftse yazdır, tekse sayı yerine
#'tek' yazdır dedik.

#bir de iç içe döngüleri görelim:

result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

#veya

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)