name = "Kadir"
surname = "Dağdaş"
# '''
# strings ifadeleri "+" kullanarak strings birleştirme yapmak yerine stings formatlama kullanılabilir.

# strings formatlama için süslü parantez yerine gelecek olan ifade ".format" ile belirlenir.
# "." ifadesinden sonra stings ile kullanılabilen diğer metodlar yazılabilir. Şimdilik .format metodunu kullancağız.
# '''

print("My name is {} {}" .format(name, surname))

# """süslü parantezler de birer indexi ifade eder. İlk süslü parantez sıfırıncı, ikinci süslü parantez birinci indextir. 
# eğer süslü parantezlerden biri yerinde diğerini yazmak istersek süslü parantezler içindeki index numaralarını değiştirmemiz yeterli olur."""

print("My name is {1} {0}" .format(name, surname))

# """aynı şeyi değişkenlere yeni bir değişken atayarak da yapabiliriz:"""

print("My name is {s} {n}" .format(n=name, s=surname))

# """süslü parantezler ille de değişkenlerle doldurulmak zorunda değildir."""

print("My name is {} {} and I'm {} years old." .format(name, surname, "36"))

#float bir bilgiyi str olarak yazdırabiliriz.

result = 200 / 700

print("The result is {}" .format(result))

#float bilginin yalnızca belli sayıda basamaklarını görüntülemek için kullanacağımız metod şu şekildedir:

print("The result is {r:1.3}" .format(r=result))

#format bilgisini print komutu içerisinde f komutu ile de yazdırabiliriz:
print(f"My name is {name} {surname} and I'm 23 years old")
