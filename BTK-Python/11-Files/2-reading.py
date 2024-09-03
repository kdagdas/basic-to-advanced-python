# İkinci parametre olarak bir mod bilgisi vermemiş olsak bile varsayılan
#olarak 'r' ataması yaparak dosya okuma moduna geçer.

# read modunda dosyanın illaki belirtilen konumda olması gerekir ki
#aksi halde bir Exception (FileNotFoundError) fırlatır.

#bu hatayı okunabilir kılmak için "try-except" bloğu kullanabiliriz.

'''
try:
    file = open('newfile2.txt')
    print('dosya başarıyla okundu')
except FileNotFoundError:
    print("dosya okuma hatası")
finally:
    print('dosya kapandı')
    file.close()
'''

file = open("newfile.txt", "r", encoding = "utf-8")
#okuma işlemi birkaç yöntemle yapılabilir.

# ************************* for döngüsü ile: *************************
'''
for i in file:
    print(i, end = "")

file.close()

# print fonksiyonu işlemini bitirdikten sonra bir boş satır bıraktığı için okunan değerler
#birer satır arayla görünür, bu yüzden 'end = "" ' komutu ile print ifadesinden sonra boşluk
#bırakma anlamına gelen bir komut verebiliriz.
'''
# ******************** read() fonksiyonu ile: *************************
'''
content1 = file.read()

print('içerik 1')
print(content1)

content2 = file.read()
print('içerik 2')
print(content2)

file.close()
'''
# read komutu ile dosya tamamen okunur ve kürsör sayfanın sonunda yanıp sönmeye başlar.
# İlk okuma yapıldıktan sonra dosya kapatılmadığı için kürsör sayfa başına geçmez ve 
#ikinci okuma yapılmak istendiği zaman okunacak nesne olmadığından dolayı boş bir çıktı verir.

# Bazen belgenin tamamını okutmak istemeyiz:
'''
content = file.read(5)
content = file.read(7)

print(content)
file.close()
'''
# ************************* readline fonksiyonu ile: *************************

# readline fonksiyonu her seferinde bir satır okur. Sonraki her komut için kaldığı satırdan
#okumaya devam eder. Print fonksiyonu okuma yaptıktan sonra bir satır boşluk bıraktığı için
#arada boşluk varmış gibi görünür. Dilenirse yukarıda yaptığımız gibi 'end' fonksiyonu ile
#bu boşluklardan kurtulabilinir.
'''
content = file.readline()
print(content)
print(content)
print(content)
file.close()
'''
# ************************* readlines() fonksiyonu ile: *************************
# Readlines fonksiyonu ile bütün içerik her satır bir eleman olacak şekilde 
#bir dizi olarakgelir.

liste = file.readlines()
print(liste)
print(liste[0])
print(liste[1])
print(liste[2])


file.close()
