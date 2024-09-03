# Soru: Girilen bir  sayının asal olup olmadığını bulun.
# **Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara (1 asal değildir!) denir.

sayi = int(input('Bir sayı giriniz: '))

if sayi == 1:
    print('1 sayısı asal sayı olarak kabul edilmez!')
'''
for i in range(2, sayi): #1 zaten her sayıyı bölebildiği için sayıya kadar olan sayılardan sayıyı bölen başka bir sayı var mı diye kontrol etmeliyiz.
    if sayi % i == 0:
        print(f"{sayi} sayısı asal sayı değildir.")
        break
'''
#VEYA:

# Eğer girilen sayıyı, sayıya kadar bir bölen çıkarsa o sayı asal değildir. 
# Dolayısıyla döngünün devam etmesine gerek yoktur. Bu yüzden 'break' ifadesi kullandık.

# Zaten döngü False değeri vermiyorsa sayı asaldır. bunun için yeniden "if" bloğu kullanmama
# gerek yoktur. Bunun için önce sayıyı asal olarak kabul etmem lazım.
# Ve bunun için "asalmi = True" şeklinde bir değişken tanımlayacağım:

asalmi = True

for i in range(2, sayi):
    if sayi % i == 0:
        asalmi = False
        break

if asalmi:
    print(f'{sayi} sayısı asaldır')
else:
    print(f'{sayi} sayısı asal değildir.')

