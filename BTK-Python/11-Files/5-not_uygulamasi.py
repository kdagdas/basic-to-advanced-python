# DOSYA YÖNETİMİ:

# Kullanıcıdan ad soyad ve 3 tane not bilgisi istenecek.
# Bu bilgiler de bir dosyaya kaydedilecek.
# Kayıtlı dosyadan istendiği zaman ortalamalar çekilecek.
# Ortalamaya göre harf sistemindeki karşılıklar gösterilecek.
# Bu hesaplanana değerlerin hepsini de başka bir dosyaya kayıt edeceğiz.

# YAPILIŞI:

# Kullanıcıya bilgileri almak için kullanıcı çıkmak isteyene kadar döndürülecek
#(örneğin çıkmak için q'ya basması gerekecek) bir döngü veriyorum.

# Döngüde önce kullanıcıdan hangi işlemi yapmak istediğini görmem için bir seçenek
#sunuyorum.

# Kullanıcının seçeceği seçenek için kullanacağım fonksiyonları döngüden önce tanımlıyorum.

def notlari_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(satir)

def not_hesapla(satir):
    satir = satir[:-1] #sonda alt satıra geçmek için bıraktığımız boşluklardan kurtulmak için
    liste = satir.split(':') #ad soyad ile notları birbirinden ayırmak için
    
    ogrenci_adi = liste[0]
    notlar = liste[1].split(',')
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3
    print(ortalama)
# ortalamanın harf karşılığını verebilmek için de bazı kodlar yazmamız gerekiyor.
    if ortalama >= 90 and ortalama <= 100:
        harf = 'AA'
    elif ortalama >= 80 and ortalama < 90:
        harf = 'BA'
    elif ortalama >= 70 and ortalama < 80:
        harf = 'BB'
    elif ortalama >= 60 and ortalama < 70:
        harf = 'CC'
    else:
        harf = 'FF'

    return ogrenci_adi + ': ' + harf + '\n'


def ortalamalari_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
#ortalama hesaplayabilmek için kaydedilen dosyadaki bilgilerden notların ve isimlerin
#ayrıştırılması ve sonra notların ortalamasının alınması gerekiyor. Bunu da not_hesapla()
#fonksiyonu ile yapacağız.

def not_gir():
    ad = input('öğrenci adı: ')
    soyad = input('öğrenci soyadı: ')
    not1 = input('not 1: ')
    not2 = input('not 2: ')
    not3 = input('not 3: ')

    # girilen bilgileri dosyaya kaydetmek için bir dosya açmamız gerekiyor ancak dosyadaki
    # bilgilere zaman zaman eklemeler yapacağımız için önceki bilgilerin silinmemesi gerekir.
    # Bu yüzden dosya açma modunu 'a' olarak seçiyorum.
    # Yukarıdaki bilgileri dosyaya kaydederken kayıtlı bilgileri nasıl işleyeceğimi de
    #düşünüyorum ki sonra sıkıntı çekmeyeyim. Örneğin daha sonra bu bilgileri
    #',' den sonra veya ':' dan sonra ayırarak işleyebilirim.
    with open("sinav_notlari.txt", "a", encoding='utf-8') as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3 + '\n')
 


def notlari_kaydet():
    with open("sinav_notlari.txt", "r", encoding='utf-8') as file:
        liste = []
    # Bu aşamada dosyaya girdi yapmayacağım için dosyayı açmak için okuma modunu kullanıyorum.
    # Daha sonra bilgileri yeni bir dosyaya kaydedeceğim. Her seferinde değişikliği zaten
    # sinav_notlari.txt dosyasına yaptığım için yeni dosyayı 'w' modunda açabilirim.
        
        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt", "w", encoding='utf-8') as file2: 
            for i in liste:
                file2.write(i)

while True:
    islem = input('1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Ortalamaları Oku\n5- Çıkış\n')

    if islem == '1':
        notlari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kaydet()
    elif islem == '4':
        ortalamalari_oku()
    else: #1, 2, 3, 4 haricinde bir şeye bastığı zaman döngüden çıkılacak.
        break