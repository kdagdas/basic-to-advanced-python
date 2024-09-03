# NUMPY İLE MATEMATİKSEL İŞLEMLER ve BELİRLİ KOŞULLARI KONTROL ETME

import numpy as np

numbers1 = np.random.randint(10,100,6) # 10 ile 100 arasında 6 tane sayı
numbers2 = np.random.randint(10,100,6) 

print(numbers1)
print(numbers2)

result = numbers1 + numbers2 # iki dizinin aynı indeksteki elemanlarını toplayıp yeni bir dizi oluşturur.
result = numbers1 + 10 # numbers1 elemanlarının tamamına 10'ar ekleme yapar
result = np.sin(numbers1) # numbers1 elemanlarının tamamının sinüsünü alır.

# MATRISLERLE ÇALIŞMA:
m_numbers1 = numbers1.reshape(2,3)
m_numbers2 = numbers2.reshape(2,3)
'''
print(m_numbers1)
print(m_numbers2)
'''
result = np.vstack((m_numbers1,m_numbers2)) # matrisleri dikey olarak birleştirme yapar.
# tek bir parametre olduğunu belli etmek için de parantez içine alıyoruz.

result = np.hstack((m_numbers1,m_numbers2)) # matrisleri yatay olarak birleştirme yapar.

# BELLİ KOŞULLARI KONTROL ETME:

result = numbers1 >= 50 # numbers1 elemanlarının her birini 50'ten büyük mü diye kontrol eder.
result = numbers1 % 2 == 0 

print(numbers1[result]) # numbers1'de result'dan gelen (true) değerleri yazdır, yani hangi sayılar çift onu görmüş oluyoruz.


print(result)
