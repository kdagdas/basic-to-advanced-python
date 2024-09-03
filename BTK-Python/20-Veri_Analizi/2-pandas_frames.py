# DataFrame'ler serilerin birleşimleridir.
# DataFrame'ler üzerinden istenilen serilere ulaşılabilir.
# Farklı uzantılı dosyalardan veriler getirilebilir.

import pandas as pd

df = pd.DataFrame([1,2,3,4])
print(df)

# DataFrame'e data, colon bilgisi ve index(satır) isimlerini atayarak bir tablo
#oluşturmasını sağlayabiliriz. 
# Değişken atamdan yapmak istersek önce Data, sonra index ve daha sonra
#colon bilgileri girilmelidir. 
data = [['Ahmet',50], ['Ali',60], ['Yağmur',70], ['Çınar',80]]
df = pd.DataFrame(data, columns = ['Name', 'Grade'], index = [1,2,3,4])
print(df)

# Dict yapısı ile kolon isimlerini vermek daha da kolaydır:
dict = {'Name': ['Ahmet','Ali','Yağmur','Çınar'], 'Grade':[50,60,70,80]}
df = pd.DataFrame(dict, index = ["1. not", "2. not", "3. not", "4. not"])
print(df)

# Satırın tamamını tek tek dizayn ederek de aynı sonuca ulaşabiliriz.
dict_list = [{"Name": "Ahmet", "Grade": 50},
             {"Name": "Ali", "Grade": 60},
             {"Name": "Yağmur", "Grade": 70},
             {"Name": "Çınar", "Grade": 80}]
df = pd.DataFrame(dict)
print(df)
 
# Pandas serilerini DataFrame hale getirme
s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data  = dict(apples = s1, oranges = s2) # dictionary hale getirdi
print(data)

df = pd.DataFrame(data) # DataFrame haline geldi.
print(df)


