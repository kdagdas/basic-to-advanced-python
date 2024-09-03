#IDENTITY OPERATOR: is

x = y = [1, 2, 3] # x ve y dizilerinin adresleri aynı
z = [1, 2, 3]     # z dizisinin x ve y dizileriyle elemanları aynı, adresleri farklıdır. 

print(x==y) #True değeri gelir çünkü adresler aynı
print(x==z) #True değeri gelir çünkü elemanlar aynı

#yani '==' (eşit mi?) ifadesi ile elemanların aynı olup olmadığı sorgulanır.
#verilen ifadelerin adreslerini sorgulamak için "is" operatörü kullanılır.

print(x is y) #True değeri gelir çünkü adresler aynı
print(x is z) #False değeri gelir çünkü adresler farklı
print(x is not z) #zaten is de False çıkan is not'da True çıkar.

#MEMBERSHIP OPERATOR: in

#var mı yok mu anlamına gelir.
x = ['apple' , 'banana']
print('banana' in x)

#yine str ifadeler için de kullanılabilir:
name = 'Kadir'
print("Kadir'in için a harfi var mı?:", 'a' in name)