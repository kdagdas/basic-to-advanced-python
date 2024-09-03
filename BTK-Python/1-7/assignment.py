#Atama Operatörleri

x = 5
y = 10
z = 20 

#veya
x, y, z = 5, 10, 20

print(x,y,z)

#aradaki bilgileri takas etmek istersek

x, y = y, x

print(x, y)

x = x + 5 #bunun yerine şu kullanılabilir.
x += 5 #yukarıdakiyle aynı anlama gelir.
#yine aynı şekilde (dört işlem, mod, tam bölme veya üs ifadeleri için de 
 #bu şekilde kullanabiliriz.)

#aynı şekilde bir değişkeni bir değişkenle de işleme sokabiliriz:

x /= z
print(x, y, z)

#peki atama operatörleri liste üzerinde nasıl kullanılırlar?

values = 1, 2, 3, 
print(values)
print(type(values))

#values değerlerini x, y, z'ye aktarabiliriz.

x, y, z = values
print(x, y, z)

#values'in içindeki değerlerin x, y, z'ye aktarılabilmesi için aynı sayıda elemana ihtiyaç vardır.
#aksi takdirde hata alırız.

# şayet values elemanları fazla olursa yine hata alırız ancak kalan elemanları dağıtmak
# istediğimiz değişkenin başına yıldız koyarak kalan elemanların bir dizi halinde 
# atama yapılmasını sağlarız:

values2 = 1, 2, 3, 4, 5
a, *b, c = values2
print(a, b, c)

