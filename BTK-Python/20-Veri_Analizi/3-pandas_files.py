# Farklı dosya uzantılardan bilgiler alıp bunları DataFrame haline getirmeyi görelim.

import pandas as pd

# "csv" uzantılı dosyalardan bilgileri alma:
'''
df = pd.read_csv('ford_escort.csv')
print(df)
'''
# ".json" uzantılı dosyalardan bilgileri alma:
'''
df = pd.read_json('example_2.json', encoding='utf-8')
print(df)
'''
# "excel (xlsx)" uzantılı dosyalardan bilgileri alma:
# xlsx dosyaları okuyabilmek için "xlrd" kütüphanesini indirmek gerekiyor.

df = pd.read_excel('example_1.xlsx', header=None)
print(df)