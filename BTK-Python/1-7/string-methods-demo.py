website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Regberiniz (40 saat)"

#1- "*Hello World*" karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
H = "*Hello World*"
print(H.strip('*'))

#yalnız soldan silmek istersek .lstrip veya sadece sağdan silmek istersek .rstrip metodları da kullanılabilir

print(H.lstrip('*'))
print(H.rstrip('*'))

#ifadenin başından ve sonundan birden fazla karakteri de silmek istersek silmek istediğimiz ifadeyi parantez içine bir kez yazmak da yeterli olur.
K = "*hello world"
print(K.strip("*hled"))

#ancak bir harfin veya rakamın atlanması durumunda strip ifadesi baştan ve sondan ifadeleri sildiği için çalışmayacaktır. Bunun yerine .replace kullanılabilir:

print(K.replace("*","").replace("o",""))
#2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.

w = website
w = w.split(".")
print(w[1])

#veya

print("www.sadikturan.com".strip("w.com"))

#3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın

print(course.lower())

#4- "course" içinde kaç tane a karakteri vardır? (count('a'))

print(course.count("a"))

#bazen bir kelimeyi bir index aralığında da aratabiliriz:

t = "herkese merhaba arkadaşlar, size merhaba demiş miydim, daha çok merhaba demek istiyorum."
print(t.count("merhaba"))
print(t.count("merhaba",0,25))

#5- "website" www ile başlayıp com ile bitiyor mu?
w = website.startswith("www") 
print(w)

w= website.endswith(".com")
print(w)

#6- "website" içindeki ".com" ifadesi var mı?
K = website.find(".com")
print(K)
print(website[21:26])

#bazen aynı kelimeden birden fazla olabilir. .find komutu bize ilk kelimenin başladığı indexi verir. İstersek .rfind ile sağdan da aratabiliriz.
c = course.rfind("Python")
print(c)

#.find() metoduna benzer olarak .index() metodu da aynı işe yarar. yine sağdan veya soldan aratabiliriz. Eğer aradğımız değer yoksa .find metodunda -1 ifadesi ile
#karşılaşırken .index() metodunda valueerror ile karşılaşırız.

w = website.index("com")
print(w)

#7- "course" içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

c = course
c = c.isalpha()
print(c)

H = "HelloWorld"
print(H.isdigit())
print(H.isalpha())

H = "124".isdigit()
print(H)


#8- "Contents" ifadesini satırda 50 karakter içinde yerleştirip sağ ve soluna * ekleyiniz

C = "Contents"
print(C.center(50,"*"))

#ifadeyi sağa veya sola yaslamak için de .rjust() veya .ljust() kullanılabilir.

print(C.rjust(50,"*"))
print(C.ljust(50,"*"))

#9- "    Course   " karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştiriniz

c = course
print(c.replace(" ","-"))

#eğer yalnızca belli miktarda yer değiştirme yapmak istersek ("*","-","5")

print(c.replace(" ","-",5))

#10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştiriniz

H = "Hello World"
print(H.replace("World", "There"))

#11- "course" karakter dizisini boşluk karakterlerinden ayırın

c = course.split()
print(c)