###################### error handling => hata yönetimi ############################

# hata gelebilecek kod blokları 'try' içine alınır.
# except komutları ile alınan hatalar için önlem veya uyarı hazırlanır.
'''
try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except ZeroDivisionError:
    print('y için 0 girilemez')
except ValueError:
    print('yalnızca sayısal ifadeler kullanınız.')
'''
# gelebilecek hatalara karşı her bir hata için except komutu yazmak yerine bir except
#komutu içinde tuple listesi ile hatalar listelenebilir.

# except komutu içine as komutu eklenerek gelebilecek hatalara bir değişken atanır ve
#except bloğu içinde istenirse oluşan hata yazdırılabilir. Bu sayade hatanın hangi sebeple
#ortaya çıktığı öğrenilmiş olur.
'''  
try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except (ZeroDivisionError, ValueError) as hata:
    print('yanlış bilgi girdiniz.')
    print(hata)
'''
# Ortaya çıkacak hataları tek tek belirtmek yerine yalnızca except komutu kullanılarak
# bütün hatalar için tek bir mesaj verilebilir ancak hatanın sebebi anlaşılamamış olur.

# hatalar için mesaj verilebildiği gibi hata olmadığında da else bloğu ile mesaj verilebilir.

'''
try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except:
    print('yanlış bilgi girdiniz.')
else:
    print("her şey yolunda")
'''

# while döngüsü ile kullanıcıdan sürekli olarak sayı isteyip işlemi gerçekleştirebiliriz,
#ta ki else'den gelecek olan (hatasız yapılan işlemden) break komutuna kadar:

# except bloğu için ValueError ve ZeroDivisionError gibi hataların ana Class'ı olan
#exception'ı da yazabiliriz. Bu sayede en azından hatanın hangi kategoriden kaynaklandığı
#hakkında fikir sahibi olabiliriz.

# Şayet yine 'as' komutu ile bir takma ad verirsek çıktı da Exception içindeki hatalardan
#hangisinin ortaya çıktığını da anlayabiliriz. 

# finally bloğu ile de bir döngü bittiğinde ortaya çıkacak bir mesaj da verilebilir.

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('yanlış bilgi girdiniz.', ex)
    else:
        print("her şey yolunda")
        break
    finally:
        print('try except sonlandı.')