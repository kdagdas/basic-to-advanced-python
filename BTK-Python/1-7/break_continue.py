#while ve for döngüleriyle kullanılabilen komutlardır.

name = 'Sadık Turan'

for letter in name:
    print(letter) #bütün karakterler sırayla ekrana yazdırılır.

#fakat ben her karakteri ekrana yazdırmak istemiyor olabilirim.
for letter in name:
    if letter == 'ı':
        break
    print(letter) #eğer karakter ı ise döngüyü durdur demiş oluyorum.

#eğer 'break' yerine 'continue' komutu girseydik 'ı' harfi geldiğinde o seferki
#döngü atlanırdı. Çıktı olarak "Sadk Turan" alınır.  

#yani 'break' döngüden tamamen çıkış yapar
#'continue' ise o sefere mahsus atlar.

x = 0

while x < 5:
    if x == 2:
        continue
    print(x) #hatalı çıktı alır çünkü
    x +=1

#x 2'de takılı kalır ve 1 artmadan continue komutundan dolayı geri döner.
#yapmamız gereken:
    
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)


x = 0
result = 0

while x <= 100:
    x += 1
    if x % 2 == 1:
        continue
    result += x #sadece çift sayıları toplama demektir.
    

print(f"toplam: {result}")