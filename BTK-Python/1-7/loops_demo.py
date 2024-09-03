# DÖNGÜLER DEMO:

# 1-100 arasında rastgele üretilecek bir sayıyı bulma oyunu yapacağız.
# önce "random modülü" ile bilgisayardan random bir sayı oluşturmasını,
# sonra bu sayıyı kullanıcıdan tahmin etmesini isteyeceğiz.
# ** "random modülü" için bir araştırma yapın:
# *** Kullanıcının tahmin hakkını varsayılan olarak 5 yapın ancak kullanıcıdan 
#     hak adedini kendinin belirlemesini isteyin.
# *** Hak adedine göre 100 üzerinden bir puanlama yapın. Örneğin 5 can sayısı için
#     her soruda 20 puan eksilsin ve 3 can sonrasında skor 40 olsun.


import random

rastgele_tamsayi = random.randint(1,10)

hak = int(input('Kaç hak kullanmak istersiniz: '))
can = hak 


sayac = 0 #puanlama için gerekli

while can > 0:
    tahmin = int(input('Tahmininiz nedir?: '))
    can -= 1
    sayac += 1
    if tahmin == rastgele_tamsayi:
        print(f'Tebrikler! {tahmin} doğru tahmindi :)')
        print(f"{sayac} seferde bildiniz. Puanınız:", 100 - (sayac - 1) * (100/hak)) #bu turda bildiği için sayacın bu tur için işlemesine gerekt yoktur. bulduğum tur için puan düşmeme gerek yok
        break
    elif tahmin < rastgele_tamsayi:
        print('yukarı')
    else:
        print('aşağı')
    
    if can == 0:
        print(f'hakkınız bitti! Doğru cevap: {rastgele_tamsayi}')