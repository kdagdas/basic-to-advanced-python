#Mantıksal Operatörler
x = 5
result = 4 < x < 10 # "x beş ile 10 arasında mı?" demektir
print(result) #True değeri gelir.

#bu soruyu her zaman bu şekilde sormak zorunda veya matematiksel ifadeler
#kullanmak zorunda değiliz. 

#bunun yerine "and" , "or" ve "not" operatörlerimiz var

result = x > 5 and x < 10
print(result) #False, True değerleri geldiği için sonuç 'False'

#and operatörü her iki taraf da "True" olduğunda "True" sonuç çıkarır.

#örneğin bir oyun olsun
hak = 3
devam = 'e'
result = hak > 0 and devam == 'e'
print(result) 

#or operatörü için tek tarafın #True olması yeterlidir.
result = (x > 4) or (x % 2 == 0) #True , False değerleri geldiği için sonuç #True
print(result)

#not operatörü sonucun tersini alır:

result = not (x > 4)
print(result)

#Birden fazla koşul da tek seferde sorgulanabilir:
result = ((x > 4) and (x < 10)) or x % 2 == 0
print(result)

