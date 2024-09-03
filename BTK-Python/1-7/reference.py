#value types => string, number, bool, float

x = 5
y = 25

x = y
y = 10
print(x, y)

#görüldüğü üzere y'de "sonradan" yapılan değişiklik x'i etkilemedi.

#reference types => list, claas
a = ['apple', 'banana']
b = ['apple', 'banana']

a = b

b[0] = 'grape'
print(a,b)

#burada da görüldüğü üzere b üzerinde sonradan değişiklik yapılmış olmasına rağmen
#a listesine de bu aksetti ve bize aynı sonuçları verdiler. 
#Çünkü bu listeler reference type'tır.


#value type'larda bellekte o bilgi tutulurken reference type'larda o bilginin
#adresleri tutulur. Bu sayede reference type'lar gibi büyük dosya boyutuna
#sahip olma potansiyeli olan bilgiler toplandığı zaman yeniden alan işgal etmezler.
#aslında o bilgilerin adresleri kopyalanmış olur ve çağırmada ilk bilgiye gidilir.
