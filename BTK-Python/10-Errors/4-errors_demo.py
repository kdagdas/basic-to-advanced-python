liste = ['1', '2', '5a', '10b', 'abc', '10', '50']

# 1- Liste elemanları içindek sayısal değerleri bulunuz.
'''
for a in liste:
    try:
        result = int(a)
        print(result)
    except ValueError:
        # continue #int olmayan elemanları yazdırmadan döngüye devam et demektir.
        print(f'{a} elemanı int bir eleman değildir.')
'''
# 2- Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz.
# aksi halde hata mesajı yazınız.
'''
while True: #döngüyü (break komutu gelene kadar) sürekli döndür demektir.
    sayi = input('bir sayi giriniz: ')
    if sayi == 'q':
        break
    #gelen sayi int'e çevrilebiliyor mu bakalım:
    try:
        result = float(sayi)
        print("float'a dönüştürülebilir, sıkıntı yok")
    except ValueError:
        print('geçersiz sayı')
        continue
'''
# 3- Girilen parola içindeki Türkçe karakter hatası veriniz.
'''
def checkPassword(parola):
    turkce_karakterler = 'şçğüıİŞÇĞÜ'

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError('Parola Türkçe karakter içeremez.')
        else:
            pass
    print('Geçerli Parola')

parola = input('bir parola giriniz: ')

try:
    checkPassword(parola)
except TypeError as err:
    print(f'bir hata tespit edildi: {err}')
'''
# 4- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları veriniz.

def faktoriyel(x):
    x = int(x)
    if x < 0:
        raise ValueError('Negatif Değer')

    result = 1

    for i in range(1, x+1): #range'te son x parametresi işin içine katılmadığı için x+1
        result *= i
    return result
    
for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(f'{x} değeri yazdırılamaz, hata kodu {err}')
        continue
    print(y)