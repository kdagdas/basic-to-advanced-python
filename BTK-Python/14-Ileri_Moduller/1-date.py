# import datetime => datetime içindeki bütün class'lar yüklenmiş olur.
# Bunun yerine "from datetime import date / time / datetime" şeklinde de yüklemeler yapabiliriz.

# Bütün classları yüklemek veya sadece date ve time modüllerinin biriyle sınırlı 
#kalmamak için her ikisini de kapsayan datetime içinden datetime modülünü yüklüyorum.
from datetime import datetime

simdi = datetime.now() # şu andaki tarih ve saati verir.
simdi = datetime.today() # şu andaki tarih ve saati verir. Her ikisinin işlevi de aynıdır.
print(simdi) # Çıktı = 2024-01-22 08:00:34.989626

# Bu bilgiler içinden de istediğim kısımları alabilirim:
result = simdi.now().year
print(result)

# Daha açıklayıcı ve str ifadelerle tarih öğrenmek için ctime() metodunu kullanabiliriz
# ctime() metodu benden bir yukarıda oluşturduğumuz 'simdi' gibi bir datetime objesi istiyor.
result = datetime.ctime(simdi)
print(result)

# ctime() metodundan çıkan sonucu özelleştirmek için strftime() modülü kullanabiliriz.
# strftime modülü ikinci parametre olarak format değişkeni ister:

result = datetime.strftime(simdi, '%Y') # tırnaklar içine "year'ın y'sini" yazdık.
print(result) #sadece yıl kısmını yazdırmış olduk

# % ifadelerini artırarak daha fazla bilgi alınabilir.
result = datetime.strftime(simdi, '%Y %X %d') #hangi harfler ne işe yarar araştır!
print(result) #yıl saat ve gün bilgisini almış olduk.

# Elimizde var str şeklindeki ifadeden uygulama gün ay yıl şeklinde bir çıkarım yapamaz.
t = '22 Ocak 2024'
gun, ay, yil = t.split()
print(gun) #22
print(ay) #ocak
print(yil) #2024

# Bundan daha kolayı ise strptime() metodu ile str ifadeden programın hangi ifadelerin
#neye karşılık geldiğini anlatarak programın ifadeyi anlamasını sağlayabiliriz:
# Metodun görmesini istemediğimiz kısımları aynen yazıyoruz.
t = '04 December 2000 hour 05:12:20'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
print(result) #2000-12-04 05:12:20
# Daha sonra aynı tanımladığımız ifade içinden yine istediğimiz kısmı alabiliriz:
result = result.year
print(result) #2000

# Bir değişkene tarih bilgisi tanımlayabilmek için de datetime modülü gereklidir:
birthday = datetime(2000, 12, 4, 5, 12, 20)
print(birthday)

# Bilgisayarlar için milat 01.01.1970 03:00:00'dır. Bu yüzden hesaplamaları ona göre yapar.
dt = datetime.fromtimestamp(0)
print(dt) # 1970-01-01 03:00:00
# datetime'ı farklı biçimlere de dönüştürmek mümkündür:
saniye = datetime.timestamp(birthday) # 1970'ten itibaren geçen saniye cinsine çevirme yapar
print(saniye) # 975895940.0
dt = datetime.fromtimestamp(saniye) # saniyeden yeniden datetime'a çevirir
print(dt)

# İki tarih arasındaki tarih farkını bulmak:
result = simdi - birthday # Buradan gelen obje 'timedelta' objesidir. Farklı bir class'tandır.
print(result)

# Artık timedelta objesi üzerinden istediğim kısımları almam gerekir:
result = result.days
print(result)

# İleri veya geri bir tarihi bulmak istiyorsak "TIMEDELTA'yı" da import etmek gerekir.
from datetime import timedelta
result = simdi + timedelta(days=10)
print(result) # 2024-02-01 09:04:35.092350
result = simdi - timedelta(days = 730)
print(result) # 2022-01-22 09:04:35.092350