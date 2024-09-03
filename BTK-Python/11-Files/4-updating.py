# DOSYADA GÜNCELLEME YAPMAK:

# 'r+' modu hem okuma hem de yazma modu anlamına gelir.
# 'r+' modu ile bir yazı yazdırdığınız zaman dosya içindeki bilgilerin tamamı
#silinmeden kürsörün bulunduğu konumdan itibaren yazı karakteri kadar kısmı silinerek
#üzerine yazılır. yani bir nevi güncelleme yapılmış olur.
'''
with open("newfile.txt", "r+", encoding = "utf-8") as file:
    file.seek(20)
    file.write('deneme')

with open("newfile.txt", "r+", encoding = "utf-8") as file:
    print(file.read())
'''

# Sayfanın SONUNDA bir güncelleme işlemi nasıl yapılır?:
'''
with open("newfile.txt", "a", encoding = "utf-8") as file:
    file.write("\nEmel Turhan")

with open("newfile.txt", "r", encoding = "utf-8") as file:
    print(file.read())
'''
# Sayfanın BAŞINDA bir güncelleme işlemi nasıl yapılır?:
'''
with open("newfile.txt", "r+", encoding = "utf-8") as file:
    content = file.read()
    content = "Efe Turhan\n" + content #dosya içerisine yazılmadı, yalnızca buraya ekliyor.
    file.seek(0)
    file.write(content)

with open("newfile.txt", "r", encoding = "utf-8") as file:
    print(file.read())
'''
# Sayfanın ORTASINA güncelleme işlemi nasıl yapılır?:

# readlines fonk. ile liste şeklinde içeriği okutabiliriz ki listelerin istediğimiz
#konumuna eleman ekleyebiliyoruz.

with open("newfile.txt", "r+", encoding = "utf-8") as file:
    list = file.readlines()
    list.insert(1,"Ali Korkmaz\n") #1. indeksten önce belirtilen elemanı ekle demektir.
    # listenin içine Ali Korkmaz'ı ekledik ancak dosyaya eklemedik. Bunun için listenin
    #her bir elemanını for döngüsüyle yeniden dosya içine yazdırabiliriz.
    '''
    file.seek(0)
    for i in list:
        file.write(i)
    print(list)
    '''
    # listeyi for döngüsü yerine file.writelines() fonk. ile de yazdırabiliriz.
    file.seek(0)
    file.writelines(list)


with open("newfile.txt", "r", encoding = "utf-8") as file:
    print(file.read())
