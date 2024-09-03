website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

#1. Soru: "course" karakter dizisinde kaç karakter bulunmaktadır?
print("1. Soru: " + str(len(course)))

#2. Soru: "website" içinden "www" karakterlerini alın
print("2. Soru: " + str(website[7:10]))

#3. Soru: "website" içinden "com" karakterlerini alın
print("3. Soru: " + str(website[len(website)-3:]))

#4. Soru: "course" içinden ilk 15 ve son 15 karakterlerini alın
print("4. Soru: " + str(course[:14]))
print(str(course[14:]))

#str eğer print içerisine str ifade yazmazsam nasıl yazabilirim?

print(len(course))
print(website[7:10])
print(website[len(website)-3:])
print(course[:14])
print(course[14:])

#5. Soru: "course ifadesindeki karakterleri tersten yazdırın"
print(course[::-1])
#sondaki basamak harflerin hangi aralıklarla yazılması gerektiğini bildirir
#eğer negatif ifade yazarsak terse doğru yazdırır.

name, surname, age, job = "Bora", "Yılmaz", 32, "Mühendis"

#6. Soru: Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")
#veya
print("Benim adım {} {}, yaşım {} ve mesleğim {}" .format(name, surname, age, job))

#7. Soru: "Hello world" ifadesindeki "w" harfini "W" ile değiştirin.
h = "Hello world"
h = h[:6] + "W" + h[7:]
print(h)

#daha sonra göreceğimiz .replace metodu da vardır: şunun yerine şunu koy anlamına gelir:
h.replace("w","W")
print(h)

#8. Soru: "abc" ifadesini yan yana üç defa yazdırın.
a = "abc"
print(a, a, a) #veya
b = "abc " * 3
print(b)