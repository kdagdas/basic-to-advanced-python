names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1997]

#1- "Cenk" ismini listenin sonuna ekleyiniz.
a = names.copy()
a.append("Cenk")
print(a)

#2- "Sena" değerini listenin başına ekleyiniz.
b = names.copy()
b.insert(0,"Sena"),
print(b)

#insert metodu ile en sona eleman ekleme de yapabiliriz:
m = names.copy()
m.insert(len(names), "Dilara")
print(m)

#3- "Deniz" ismini listeden siliniz.
c = names.copy()
c.pop(3)
print(c)

#.remove ile de silinebilir.
n = names.copy()
n.remove("Deniz")
print(n)

# 3- "Deniz" isminin indeksi nedir?
print(names.index("Deniz"))

# 4- "Ali" listenin bir elemanı mıdır?
d = "Ali" in names
print(d)

# 5- Liste elemanlarını ters çevirin.
e = names.copy()
e.reverse()
print(e)

# 6- Liste elemanlarını alfabetik olarak sıralayınız.
f = names.copy()
f.sort()
print(f)

# 7- years lsitesini rakamsal büyüklüğe göre sıralayınız.
g = years.copy()
g.sort()
print(g)

# 8- str = "Chevrolet, Dacia" karakter dizisini listeye çevviriniz.
str =  "Chevrolet , Dacia"
h = str.split(",")
print(h)

# 10- years dizisinin en büyük ve en küçük elemanı nedir?
print("dizinin en büyük elemanı:", max(years))
print("dizinin en küçük elemanı:", min(years))

# 11- years dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))

# 12- years dizisinin tüm elemanlarını siliniz.
k = years.copy()
k.clear()
print(k)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
k = [input("Bize 3 tane otomobil markası söyler misiniz?")]
print(k)

#veya .append metodu ile de yapabiliriz:
markalar = []
marka = input("3 adet otobil markası giriniz: ")
markalar.append(marka)
print(markalar)

#bu liste bir elemanlı oldu. Eğer 3 elemanlı bir liste oluşturmak istersek şimdi
#döngüleri öğrenmediğimiz için bu işlemi 3 kere tekrar etmemiz gerekir:

ucmarka = []
marka1 = input("1. markayı giriniz: ")
ucmarka.append(marka1)
marka2 = input("2. markayı giriniz: ")
ucmarka.append(marka2)
marka3 = input("3. markayı giriniz: ")
ucmarka.append(marka3)

print(ucmarka)

