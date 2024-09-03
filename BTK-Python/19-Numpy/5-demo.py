import numpy as np

# 1- (10,15,30,45,60) değerlerin sahip numpy dizisi oluşturunuz.

np_array = np.array([10,15,30,45,60])
print(np_array)


# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz. 

arr = np.arange(5,15)
print(arr)

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.

arr2 = np.arange(50,100,5)
print(arr2)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.

zeros = np.zeros(10)
print(zeros)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz

ones = np.ones(10)
print(ones)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin

arr3 = np.linspace(0,100,5)
print(arr3)

# 7- (10-30) arasında rastgele 5 tane tamsayı üretin

result = np.random.randint(10,30,5)
print(result)

# 8-  -1 ile 1 arasında 10 adet sayı üretin

result = np.random.randn(10)
print(result)


# 9- 3x5 boyutlarında 10-50 arasında rastgele bir matris oluşturunuz

array = np.random.randint(10,50,15)
matris = array.reshape(3,5)
print(matris)

# 10- Üretilen matrisin satır ve sütun sayılar toplamlarını hesaplayınız

matris_top_satir = matris.sum(axis=1)
matris_top_sutun = matris.sum(axis=0)
print(matris_top_satir)
print(matris_top_sutun)


# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir?

matris_max = matris.max()
print(matris_max)

# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır?

print(matris_max.argmax())

# 13- 10-20 arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz

np_array2 = np.arange(10,20)
print(np_array2[:3])

# 14- Üretilen dizinin elemanlarını tersten yazdırınız

print(np_array2[::-1])

# 15- Üretilen matrisin ilk satırını seçiniz

print(matris[0])

# 16- Üretilen matrisin 2. satır 3. sütundaki elemanını seçiniz

print(matris[1,2])


# 17- Üretilen matrisin tüm satırlarındaki ilk elemanı seçiniz

print(matris[:,0])

# 18- Üretilen matrisin her bir elemanının karesini alınız

matris_kare = matris ** 2
print(matris_kare)

# 19- -50 ile 50 arasında bir matris elemanlarının hangileri pozitif çift sayıdır?


array = np.random.randint(-50,50,15)
matris = array.reshape(3,5)
print(matris)

ciftler = matris[matris % 2 == 0]
print(ciftler)

pozitif_ciftler  = ciftler[ciftler>0]
print(pozitif_ciftler)


