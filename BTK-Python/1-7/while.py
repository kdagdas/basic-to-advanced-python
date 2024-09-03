# Elimizde liste varken for döngüsü ile bu listenin elemanlarına ulaşmak kolaydı.
# Ancak ben 0'dan 100'e kadar olan sayıları bir liste içine almak istediğim zaman 
# "WHILE" döngüsüne başvurabilirim.

x = 0 #bir değişken tamamlamış olduk.

#while döngüsü için bir koşul bulmamız gerekiyor.
#Koşul tamamlanıncaya kadar "True" olan koşul, tamamlandıktan sonra "False" olur.

while x < 100:
    print(x)
    x += 1  #(x = x + 1 demektir) 
            #(x sürekli birer artmalı ki sonsuz bir döngü ortaya çıkmasın.)
print('ve bitti...')

#Gelen bütün ifadeleri de yazmayabiliriz. Bunun için bir koşul daha atamalıyız.

while x <= 100:
    if x % 2 == 1:
        print(f'sayı tek: {x}')
    else:
        print(f'sayı çift: {x}') #if çalıştığı zaman çalışır.
    x += 1                       #if çalışsın ya da çalışmasın x'in 100'e yaklaşmasını isteriz.


#örnek olarak bir kişiden istenilen bilgiyi almak istiyoruz.
#her yanlış girdiğinde yeniden sormak istiyoruz.
    
name = '' #False
while not name: #while yanındaki ifade 'True' değeri verdikçe çalışır.
    name = input('isminizi giriniz: ') #name yanlış olduğunda not name ifadesi 'True' değeri vermiş olur.

print(f'Merhaba {name} Bey, hoşgeldiniz.')