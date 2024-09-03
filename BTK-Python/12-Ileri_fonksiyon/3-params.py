# FONKSİYONLARA PARAMETRE OLARAK FONKSİYON GÖNDERMEK:

def toplama(a, b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    return a/b

def islem(f1, f2, f3, f4, islem_adi): #f1, f2, f3 ve f4 gönderdiğimiz fonksiyonların referanslarını alacak parametre isimleridir.
    if islem_adi == "toplama":
        print(f1(2,3)) #yani f1 yerine aslında toplama(2,3) şeklinde fonk. çağırması yapmış oluyoruz.
    elif islem_adi == "çıkarma":
        print(f2(5,3))
    elif islem_adi == "çarpma":
        print(f3(3,4))
    elif islem_adi == "bölme":
        print(f4(10,2))
    else:
        print('geçersiz işlem!')

islem(toplama, cikarma, carpma, bolme, "toplama") # Çıktı = 5
islem(toplama, cikarma, carpma, bolme, "çıkarma") # Çıktı = 2
islem(toplama, cikarma, carpma, bolme, "çarpma") # Çıktı = 12
islem(toplama, cikarma, carpma, bolme, "bölme") # Çıktı = 5
islem(toplama, cikarma, carpma, bolme, "toplaamma") # Çıktı = geçersiz işlem!