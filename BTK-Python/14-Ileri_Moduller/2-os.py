# OS Modülü ile işletim sistemi, klasörler veya dosyalarla alakalı işlemler yapılır.
import os
'''
# işletim sistemi öğrenme:
result = os.name # Çıtkı = nt (windows)

# mevcut dosya (2-os.py) hangi klasörde:
result = os.getcwd() # C:\Users\Kadir Dağdaş\Desktop\python_temelleri\14-Ileri_Moduller

# mevcut klasörün yerini öğrendikten sonra o konuma yeni klasör oluşturabilirim.
#os.mkdir('new_directory') # aynı dizine new_directory isminde bir klasör oluşturuldu.

#Başka bir konuma geçmek / dizin değiştirmek için:
os.chdir('C:\\') # C diskindeyiz.
result = os.getcwd()
# os.mkdir('new_directory') # C diskine 'new_directory isminde bir dosya oluşturdu.

# os.chdir(..) => bir üst dizine geçer
# os.chdir(../..) => iki üst klasöre geçmiş olur.
# os.chdir(..) => bir üst dizine geçer

# İç içe klasör oluşturma:
# os.makedirs('new_directory/yeniklasör') # mevcut dizine new_directory altında yeniklasör isminde bir klasör oluşturdu.

# veya direkt istediğiniz konumu girerek de oluşturabilirsiniz:
# os.makedirs('C:\\newdirectory/yeniklasör') # C diskinde newdirectory içine yeniklasör isminde
'''
# LİSTELEME İŞLEMLERİ:
'''
result = os.listdir() #dizindeki dosyanın listelemesini yapar
result = os.listdir('C:\\') #istenen dosyanın (C diski) listelemeesini yapar
'''
# listelenecek dosyalarda filtreleme işlemi: