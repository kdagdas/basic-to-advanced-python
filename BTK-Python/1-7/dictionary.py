#key - value sistemiyle çalışır.
#yani bir bilgiye ulaşmak için önce key bilgisi gerekiyor.

#dictionary bilgisini kullanmadan aynı işlemleri yapmak:

sehirler = ["kocaeli","istanbul"]
plakalar = [41,34]

print(plakalar[sehirler.index("kocaeli")])

#burada her iki listenin de sıralarının uyması gerekiyor ki doğru sonuca ulaşalım.

#dictionary listeler süslü parantezler ile kullanılır.

plakalar = {"kocaeli" : 41, "istanbul" : 34}
print(plakalar["kocaeli"])
print(plakalar["istanbul"])

#eğer dic. listede olmayan bir elemana bilgi girersek o elemanı listeye ekler:

plakalar["ankara"] = 6
print(plakalar)

#eğer var olan elemanı tanımlarsak onun value'sini değiştirmiş oluruz.

plakalar["istanbul"] = "otuzdört"
print(plakalar)

#dic listeler bir key ile birden fazla value vererek bir eleman için birden fazla
#bilgiyi aynı anda alabilmemize olanak tanırlar.
users = {
    "sadikturan" : {
        "age" : 36,
        "mail" : "sadik@gmail.com",
        "adress" : "kocaeli",
        "phone" : "5396943344"
        },
    "cinarturan" : {
        "age" : 20,
        "mail" : "cinar@gmail.com",
        "adress" : "istanbul",
        "phone" : "5396343344"
        }
}


#bunun altındaki bilgilere de ulaşabilirim:
'''
print(users["sadikturan"]["age"])
print(users["sadikturan"]["mail"])
print(users["sadikturan"]["adress"])
print(users["sadikturan"]["phone"])
'''

#dic. listeler içinde diziler de yazılabilir:
users = {
    "sadikturan" : {
        "roles" : ["admin" , "users"],
        "age" : 36,
        "mail" : "sadik@gmail.com",
        "adress" : "kocaeli",
        "phone" : "5396943344"
        },
    "cinarturan" : {
        "roles" : ["users"],
        "age" : 20,
        "mail" : "cinar@gmail.com",
        "adress" : "istanbul",
        "phone" : "5396343344"
        }
}
print(users)

print(users["sadikturan"]["roles"])