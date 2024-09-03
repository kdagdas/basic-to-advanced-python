message = "Hello There. My name is Kadir Dağdaş"
#tüm metodlarda içine bir şey yazılmayacak olsa bile parantez açılır ve kapatılır.

#.upper() metodu ile değişken içindeki tüm karakterler büyük yazılır:
"message = message.upper()"
"print(message)"

#.lower() tüm karakterleri küçük yapar:

"message = message.lower()"
"print(message)"

#.titel() her kelimenin baş harfini büyük harfe çevirir
#.capitalize() verilen ifadenin yalnızca ilk harfini büyük yazmış olur. 
#.strip() baştan ve sondan varsa bir boşluk karakteri silinmesini sağlar. Bazen şifre işlemleri için gerekebilir.
#.split() ile her boşluk karakterinden sonraki ifadenin ayrı olarak verilmesini sağlar

"message = message.split()"
"print(message)"

#split() ile aslında her ifadeye bir index atanmış olur. Eğer cümle içinden bir ifade
#çağrılmak istenirse index no istenebilir:

"print(message[2])"

#split ifadeye neyden ayırması gerektiğini parantez içine yazarak anlatabiliriz:

'''message = message.split(".")
"print(message)"
"print(message[0])'''

#split ile ayırdığımız kelimeleri yeniden birleştirebilir ve her araya gelecek elemanı da seçebiliriz.

'''message = message.split()
message = " (ara) ".join(message)
print(message)'''

#.find() ifadenin içinde bir kelimenin var mı yok mu olduğunu bakmak içindir
#kelime hangi index numarasından itibaren başlıyor, onu anlatır.
#eğer -1 değeri geliyorsa o kelime cümle içerisinde yok demektir.

'''index = message.find("Kadir")
print(index)

print(message[24:30])'''

#.startwith() ile mi başlıyor demektir. bool ifadeler için kullanılabilir.

'''"isFound = message.startswith('H')"
message = message.split()
print(message)
isFound = message[1].endswith('.')
print(message[1])
print(isFound)'''

'''message = message.replace('Kadir','Çınar')
message = message.replace(' ','*').replace('ı','i').replace('ğ','g')
print(message)'''

#.center() metodu içindeki sayı kadar karakterli bir alan açar ve mevcut yazıyı
# ortalayarak oraya aktarır:

'''print(message.center(200))'''

#kalan boşlukları da istediğimiz ifade ile doldurmak için:

"""print(message.center(50,'*'))"""

#bunu bir div içinde 