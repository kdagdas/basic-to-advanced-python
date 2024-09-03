#Karşılaştırma Operatörleri

#Karşılaştırma operatörleri işlemler sırasında yönelendirme yapmak için kullanılır

#örneğin kullanıcıdan aldığımız username, password => database'e gider
#'sadikturan' ve '123456' bilgileri alınmış olsun.

a, b, c, d = 5, 5, 10, 4

# '==' ifadesi 'eşit mi?' sorusuna karşılık gelir. Cevap bool tipindedir. 

result = (a == b) #True
result = (a == c) #False

username = 'kdagdas'
password = '1234'
result = ('kdagdas' == username) 

print(result)

# '!=' ifadesi 'eşit değildir mi' gibi bir anlama gelir. İfadeler birbirne eşit
# olduğunda 'False' sonucunu verir.

result = (a != b)
print(result) #False (çünkü eşit)

result = (a != c)
print(result) #True (çünkü eşit değil)

# '>' ifadesi "..'den büyük mü?", '<' ifadesi "..'den küçük mü?" 
#sorusuna karşılık gelir.
result = (a > c)
print(result) #False (çünkü büyük değil)

# ">=" ifadesi de "büyük eşit mi?" anlamına gelir.

# bool ifade olan "True" numerik olarak "1'e", "False" ise "0'a karşılık" gelir.
result = (True == 1)
print(result) #True

result = True + False + 40
a = result == 41
print(a)