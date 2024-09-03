# Modüller kendi aralarında iletişim halinde olabilirler.
# Hazır modüller veya 3. şahıslar tarafından hazırlanmış modüller olabilir.
# Python için modül havuzuna pypi.org sitesinden ulaşılabilir.

# Şimdi hazır modül kullanımına bakalım.

############## YONTEM 1 ###################

# import + module_name ile modül kullanıma dahil edilir.

# import math
'''
value = dir(math) #math modülü içindeki tüm fonksiyonları görebiliriz.

value = help(math) #math içindeki fonksiyonlar hakkında bilgi sahibi olabiliriz.

value = help(math.factorial) #tek bir fonksiyon hakkında bilgi alabiliriz.
'''
#örnek bir kullanım yapalım:

'''
value = math.sqrt(49) #karekök fonksiyonudur. Çıktı = 7.0
value = math.factorial(5) #faktöriyel fonksiyonudur. Çıktı = 120
value = math.floor(5.9) #aşağı doğru yuvarlama yapar. Çıktı = 5
value = math.ceil(5.9) #yukarı doğru yuvarlama yapar. Çıktı = 6
'''

#kütüphanelere takma ad vererek farklı isimle çağırabiliriz:

'''
import math as islem  #islem ismi math için takma isim oldu.

value = islem.factorial(5)
'''

############## YONTEM 2 ###################

# modülden gerekli kısmı veya hepsini import edebiliriz. 
# hepsini import etmek için "*" kullanılır.
# zaten "math modülünden diye başta beyanda bulunduğumuz için
#direkt fonksiyon ismi kullanılır."

'''
from math import *

value = factorial(5)

'''

# modülden her fonksiyonu çekmek yerine istediğimiz fonksiyonları çekebiliriz:

from math import factorial, sqrt

value = factorial(5)
print(value) # Çıktı = 120
value = sqrt(49)
print(value) # Çıktı = 7
value = ceil(9.8)
print(value) # Çıktı = 'ceil' is not definied

# yüklenmiş modüldeki fonksiyon ismi ile farklı bir modüldeki veya aynı çalışma
#alanındaki modüller aynı isimde olabilir. Bu durumda derleyici aynı isimdeki dosyalardan
#en son tanımlanan fonksiyonu kabul eder.