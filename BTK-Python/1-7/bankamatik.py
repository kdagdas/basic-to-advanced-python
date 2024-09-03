# BANKAMATİK UYGULMASI:

sadik_hesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '123456',
    'bakiye': 3000,
    'ekHesapLimit': 2000,
    'ekHesap': 2000
}

ali_hesap = {
    'ad': 'Ali Turan',
    'hesapNo': '123789',
    'bakiye': 2000,
    'ekHesapLimit': 1000,
    'ekHesap': 1000
}

# Oluşturulan hesaplardan kullanıcılar para çekmek istediğinde önce bakiyeden sonra 
# ek hesaptan olacak şekilde istenilen paraya göre para çekebilmeleri isteniyor.

# Eğer girilen tutar bakiye ve ek hesaptan büyük ise 'bakiye yetersiz' uyarısı, eğer miktar
# bakiyeden büyük ama ek hesaptan da çekilmesi gerekiyorsa, 'ek hesaptan para çekilecek,
# onaylıyor musunuz?' şeklinde uyarı çıkması gerekiyor. 

def paraCek(hesap, miktar):
    print(f'Merhaba {hesap['ad']}')

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)

    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı? (e/h)')

            if ekHesapKullanimi == 'e':
                miktar -= hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= miktar
                bakiyeSorgula(hesap)
    
            else:
                print('Ek hesap kullanma talebini reddettiniz!')
                bakiyeSorgula(hesap)
    
        else:
            print('üzgünüz, bakiyeniz yetersiz olduğundan işleminiz gerçekleştirilemiyor')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} no'lu {hesap['ad']}'a ait hesabın\ngüncel bakiyesi: {hesap['bakiye']} ve ek hesap bakiyesi: {hesap['ekHesap']}")

def paraYatir(hesap, miktar):
    fark = hesap['ekHesapLimit'] - hesap['ekHesap']
    if fark < hesap['ekHesapLimit']:
        miktar -= fark
        hesap['ekHesap'] += fark
        hesap['bakiye'] += miktar - fark
        print('Ek Hesap borcunuz ödendi ve kalan tutar hesabınıza yüklendi')
        bakiyeSorgula(hesap)
    else:
        hesap['bakiye'] += miktar
        print('Tutar hesabınıza başarıyla gönderildi')
        bakiyeSorgula(hesap)
         
#bakiye sorgulama fonksiyonunu alttaki gibi her para çekme işleminde çağırmak yerine
#fonksiyon içine koyarak otomatik gelmesini sağlayabiliriz.       
            
paraCek(sadik_hesap, 1000)
#bakiyeSorgula(sadik_hesap)

paraCek(sadik_hesap, 3000)
#bakiyeSorgula(sadik_hesap)

paraYatir(sadik_hesap, 4000)

paraCek(sadik_hesap, 3000)
#bakiyeSorgula(sadik_hesap)

# global ve local olarak değişkenlerin tanımlanmasını görmüştük.
# Buna göre fonksiyon içindeki değişiklikler dışarıdaki verileri etkilemezdi.
# Peki neden fonksiyonda bulunan veriler dışarıya da değişerek çıktılar?
# Çünkü verileri dict. liste şeklinde vererek bir adres kopyalaması yapmış olduk.
# Bunun yerine verileri doğrudan değişkenlere atasaydık 
# orijinal verilerde değişiklik yapılmazdı