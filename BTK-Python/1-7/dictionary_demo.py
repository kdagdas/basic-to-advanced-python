
"""ogrenciler = {
    '120' : {
        'ad' : 'Ali',
        'soyad' : 'Yılmaz',
        'telefon' : '532 000 00 01',
    },
     '125' : {
        'ad' : 'Can',
        'soyad' : 'Korkmaz',
        'telefon' : '532 000 00 02',
    },
     '128' : {
        'ad' : 'Volkan',
        'soyad' : 'Yüksel',
        'telefon' : '532 000 00 03',
    },
    
}"""

#1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içidne saklayınız.

#2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

'''ogrenciler = {
    input("Öğrenci numaranızı giriniz: ") : {
        "ad" : input("isminizi giriniz: "),
        "soyad" : input("soyisminizi giriniz: "),
        "telefon" : input("telefon numaranızı giriniz: ")
    },
    input("Öğrenci numaranızı giriniz: ") : {
        "ad" : input("isminizi giriniz: "),
        "soyad" : input("soyisminizi giriniz: "),
        "telefon" : input("telefon numaranızı giriniz: ")
    },
    input("Öğrenci numaranızı giriniz: ") : {
        "ad" : input("isminizi giriniz: "),
        "soyad" : input("soyisminizi giriniz: "),
        "telefon" : input("telefon numaranızı giriniz: ")
    },
}

print(ogrenciler[input("öğrenci no giriniz: ")])'''

#veya değişken atayarak da yapabiliriz:
ogrenciler = {}

number = input("öğrenci numaranızı giriniz: ")
name = input("adınızı giriniz: ")
surname = input("soyadınızı giriniz: ")
phone = input("telefon numaranızı giriniz: ")

ogrenciler[number] = {
    "ad" : name,
    "soyad" : surname,
    "telefon" : phone,
}

#aynı işlemleri .update metodu üzerinden de yapabiliriz:

'''ogrenciler.update({
    number : {
        "ad" : name
        "soyad" : surname
        "telefon" : phone
    }
})'''

#.update metodunda birden çok veri aynı anda eklenebilir. 

number = input("öğrenci numaranızı giriniz: ")
name = input("adınızı giriniz: ")
surname = input("soyadınızı giriniz: ")
phone = input("telefon numaranızı giriniz: ")

ogrenciler[number] = {
    "ad" : name,
    "soyad" : surname,
    "telefon" : phone,
}

number = input("öğrenci numaranızı giriniz: ")
name = input("adınızı giriniz: ")
surname = input("soyadınızı giriniz: ")
phone = input("telefon numaranızı giriniz: ")

ogrenciler[number] = {
    "ad" : name,
    "soyad" : surname,
    "telefon" : phone
}

ogrNo = input("aramak istediğiniz öğrencinin numarasını yazınız: ")


#Kullanıcılara f string ile daha güzel bir çıktı oluşturalım.

print(f"Aradığınız {ogrNo} numaralı öğrencinin adı {name}, soyadı {surname}, ve telefonu ise {phone}'dir.")


