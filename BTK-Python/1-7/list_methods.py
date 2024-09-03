numbers = [1, 10, 5, 16, 4, 9, 52]
letters = ['a','g','s','b','y','s']
mixed = [1, 's', 2, 'c',3, 'a']

val = min(numbers)
print(val)

val = max(numbers)
print(val)

#str içeren listelerde max ve min değerleri alfabetik sıralamaya uygun olarak değer üretir:

val = max(letters)
print(val)

#listenin sonuna bir öğe eklemek istersek .append metodunu kullanabiliriz.
k = numbers.copy()
k.append(49)
print(k)

#istediğimiz konuma bir eleman eklemek için .insert metodunu kullanmalıyız.
#bunun önce hangi indexten önce ekleyeceğimizi yazmalıyız:

l = numbers.copy()
l.insert(3, 78)
print(l)

#.extend metodu liste içine birden fazla öğe veya liste içine liste eklemeyi sağlar:

m = numbers.copy()
m.extend(letters)
print(m)

#.pop ile listenin sonundaki elemanı veya verilen bir index ile o indexteki eleman silinebilir.

n = numbers.copy()
n.pop(2)
print(n)

#.remove metodu ile de hangi elemanı silmek istediğimizi girerek işlem yapabiliriz.
o = mixed.copy()
o.remove("s")
print(o)

#.sort metodu ile birlikte listeyi alfabetik veya küçükten büyüğe doğru sıralamış oluruz:

p = letters.copy()
p.sort()
print(p)

r = numbers.copy()
r.sort()
print(r)

#.reverse listeyi tam tersine çevirir
s = r.reverse()
print(r)

#.count ile istediğimiz elemanı da saydırabiliriz.
t = letters.copy()
print(t.count("s"))

#.clear ile bütün elemanlarını silebiliriz.

