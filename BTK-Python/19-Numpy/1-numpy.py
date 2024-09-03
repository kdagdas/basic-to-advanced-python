# Numpy veri analizinde kullanılan oldukça popüler bir kütüphanedir.

# PYTHON LIST:
py_list = [1,2,3,4,5,6,7,8,9]

# Numpy ile klasik python listelerinde yapamadığımız bir çok şeyi yapabiliriz.
# Klasik listelerde bulunmayan birçok metod da Numpy'da bulunur.
# Büyük verilerle çalışırken Numpy kullanmak daha kullanışlıdır.
# Numpy ile çalışmak daha az yer kaplar ve daha performanslıdır.

# Python listelerinin Numpy'daki karşılığı "array'dir"

# Bir listeyi array haline getirmek için np.array() metoduna liste elemanlarını parametre
#olarak algılamaması için yine köşeli parantezler içinde yazmak gereklidir. 

import numpy as np

np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list)) # Çıktı = <class 'list'>
print(type(np_array)) # Çıktı = <class 'numpy.ndarray'>

# "np_array" dizisi "py_list" dizisi gibi tek boyutlu bir dizidir.
# Çok boyutlu dizilerde liste içinde listeler bulunur. Bunlar da farklı grupların
#verilerini temsil edebilirler (Örn: farklı bölgelere ait hava durumu verileri)
# Tek boyutlu bir array'i çok boyutlu bir array haline .reshape() metodu ile getirebiliriz.
# 'array'in' çok boyutlu haline 'matris' denir.

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3) #np_array'i 3'e 3'lük gruplar haline getirir. 3 satır ve 3 kolondan oluşur.
print(np_multi)
print(py_multi)

# boyutlarını karşılaştıralım:
print(np_array.ndim) # 1 Boyutlu
print(np_multi.ndim) # 2 Boyutlu

# shape'lerini karşılaştıralım:
print(np_array.shape) # (9,)
print(np_multi.shape) # (3,3)
