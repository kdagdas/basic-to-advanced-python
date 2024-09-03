#1- "Bmww, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

my_list = ["Bmw", "Mercedes", "Opel", "Mazda"]
# print(my_list)

# #2- Liste Kaç elemanlıdır?

# print(len(my_list))

# #3- Listenin ilk ve son elemanı nedir?

# print(my_list[0], my_list[-1])

# #4- Mazda değerini Toyota ile değiştirin.

# my_list[-1] = "Toyota"
# print(my_list)

# #5- Mercedes listenin bir elemanı mıdır?

# if "Mercedes" in my_list:
#     print("Evet, Mercedes listenin bir elemanıdır")
# else:
#     print("Hayır, Mercedes listenin bir elemanı değildir")

# #veya "in" operatörü ile birlikte True ya da False değeri alınabilir:
    
# result = "Mercedes" in my_list
# print(result)

# #6- Listenin -2 indeksindeki değer nedir?
    
# print(my_list[-2])

# #7- Listenin ilk üç elemanını alın.

# print(my_list[0:3])

# #8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.

# my_list[-2:] = ["Toyota" , "Renault"]
# print(my_list)

# #9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

# # k = my_list.extend(["Audi" , "Nissan"])
# # print(k)

# #veya liste üzerine manuel eklemeler de yapılabilir:

# result = my_list + ["Audi","Nissan"]
# print(result)

# #10- Listenin son elemanını silin.

# my = my_list[:2]
# print(my)

# #veya "del" komutu ile liste içindeki indexe sahip elemanı silebiliriz.

# del my_list[-1]
# print(my_list)

# #11- Liste leemanlarını tersten yazdırınız.

# araba = my_list.reverse()
# print(araba)

#veya string ifadelerde olduğu gibi

result = my_list[::-1]
print(result)

#12- Aşağıdaki verileri bir liste içinde saklayınız.
    
    #studentA: Yiğit Bilgi 2010, (70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    #studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["Yiğit Bilgi" , 2010 , [70,60,70]]
studentB = ["Sena Turan", 1999, [80,80,70]]
studentC = ["Ahmet Turan" , 1998 , [80,70,90]]

#13- Liste elemanlarını ekrana yazdırınız.

result = studentA + studentB + studentC
print(result)

not_ortalama1 = sum(studentA[2])/len(studentA[2])
not_ortalama2 = sum(studentB[2])/len(studentB[2])
not_ortalama3 = sum(studentC[2])/len(studentC[2])

result1 = f"{studentA[0]}'nın yaşı {2023 - studentA[1]} ve not ortalaması {not_ortalama1:.2f}'dır."
print(result1)
result2 = f"{studentB[0]}'nın yaşı {2023 - studentB[1]} ve not ortalaması {not_ortalama2:.2f}'dır."
print(result2)
result3 = f"{studentC[0]}'nın yaşı {2023 - studentC[1]} ve not ortalaması {not_ortalama3:.2f}'dır."
print(result3)