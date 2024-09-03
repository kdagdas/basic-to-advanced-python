name = "Sadık"
surname = "Turan"
age = 36

#eğer ifadeleri tek satıra yazdırmak yerine alt satıra yazdırmak istersek
#\n ifadesinden sonraki kısım alt satıra yazılacak şekilde düzenlenir:
#print("My name is " + name + " " + surname + " and \nI am " + str(age) + " years old.")


greeting = "My name is " + name + " " + surname + " and \nI am " + str(age) + " years old."

'''print(greeting)'''

#strings değerler için her karaktere bir index numarası atanır ve bu index numaraları
#sıfırdan başlar. yalnızca o indexi yazdırmak için köşeli parantez kullanılır:
#boşluk karakterleri de indexlenir!

"""print(greeting[0])"""

#greeting ifadesinin kaç karakterli olduğunu bulmak için "len" komutu kullanılır:

'''print(len(greeting))'''

'''length = len(greeting)'''
'''print(greeting[length-2])'''  #son karakteri yazdırmak istersek bir değişken ile
#yukarıdaki gibi -1 yazarak son karakter yazdırılmış olur. 

#bu kadar işlem yerine greeting[-1] ifadesi de son karakteri vermiş olur.
'''print(greeting[-2])'''

#indexi bir yerden başla ve bir yere kadar git demek için [2:5] şeklinde ifade kullanılabilir.
'''print(greeting[2:5])'''

#başlangıç ve bitişi yazmak zorunda değilim yazmadığım taraf sonsuza gider:
'''print(greeting[3:])'''

#her karakter yerine 2 karakterde bir yazdır demek istersem: [2:5:2]
'''print(greeting[2:40:2])'''

