# Pandas veriler ile çalışmamımızı sağlar
# Veriler üzerinde kolayca değişikliklikler yapabiliriz.
# Numpy'a alternatif değildir, her ikisi de alanında yardımcı kütüphanelerdir.
# Numpy daha çok matematiksel işlemlerde kullanılır.
# Pandas daha çok veriler üzerindeki çalışmalarda tercih edilir.

# Pandas serileri, verilen farklı türde verilere göre farklı datatype alırlar.
import pandas as pd
import numpy as np
'''
# data
numbers = [20,30,40,50] 
letters = ['a', 'b', 'c', 'd']
scalar = 5
dict  = {'a':10, 'b':20, 'c':30, 'd':40}
random_numbers = np.random.randint(10,100,6)

# numpy dizilerinde elemanların homojen olması gerekiyordu ancak pandas'da böyle değil
karisik = ['K',4,'D',1,'R']


pandas_series = pd.Series(numbers) # dtype: int64
print(pandas_series)

pandas_series = pd.Series(letters) # dtype: object
print(pandas_series)

pandas_series = pd.Series(karisik) # dtype: object
print(pandas_series)

# hangi indekslere verileri koyacağımızı da ayarlayabiliriz.
# verdiğimiz indeks kadar verinin artması için scalar veri türünde olması gerekmekte.
pandas_series = pd.Series(scalar, [0,1,2,3,4]) # dtype: int64
print(pandas_series) # bütün indekslere 5 koyar

# indeksler yerine key bilgileri ile de eşleştirme yapabilirim.
pandas_series = pd.Series(numbers, ['a','b','C','d']) # dtype: int64
print(pandas_series)

# dict veriler zaten kolayca key value şeklinde eşleşir.
pandas_series = pd.Series(dict) # dtype: int64
print(pandas_series)

# numpy ile oluşturduğumuz bir listeyi de verebiliriz.
pandas_series = pd.Series(random_numbers) # dtype: int64
print(pandas_series)



pandas_series = pd.Series([20,30,40,51], ['a','b','C','d'])
print(pandas_series)


#indeks numaralarını değiştirmiş olsak da standart indeks no ile elemanlara erişebiliriz.
result = pandas_series[0]
print(result) # 20

result = pandas_series[:2] # ilk iki eleman
print(result)

# tanımladığımız indeksler ile de veriye ulaşabiliriz.
result = pandas_series['d']
print(result) # 51

# birden fazla key bilgisine sahip elemanlar da alabiliriz.
result = pandas_series[['a','d']]
print(result) #a 20 b 51

# numpy'daki metodları da kullanabiliriz:
result = pandas_series.ndim  # 1 = 1 boyutlu bir liste
result = pandas_series.dtype # int64
result = pandas_series.shape # (4,) = 4'e 1'lik bir liste
result = pandas_series.sum() # toplamı = 140
result = pandas_series.max() # en büyük eleman = 51

# matematiksel işlemler de yapılabilir:
result = pandas_series + pandas_series # liste elemanları iki katına çıkar

# numpy üzerinden de bazı işlemler yapılabilir:
result = np.sqrt(pandas_series) # elemanların karekökünü alır.
result = pandas_series % 2 == 0
print(result)
print(pandas_series[pandas_series % 2 == 0])
'''

opel2018 = pd.Series([20,30,40,10],['astra', 'corsa', 'mokka', 'insignia'])
opel2019 = pd.Series([40,30,20,10],['astra', 'corsa', 'grandland', 'insignia'])

# çıktıda mokka ve grandland için karşı listelerde veri olmadığı için Not a Number anlamına
#gelen NaN çıktısı gelir.

total = opel2018 + opel2019
print(total)
print(total['astra']) # 60




