# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erisme_modu)
# dosya_erisme_modu => dosyayı hangi maaçla açtığımızı belirtir.

# 'w' => (Write) yazma modu. Dosyayı konumda oluşturur. Bu mod ile açılan dosyaların
# üzerine yazılmış olur ve önceki bilgiler silinir.
'''
file = open('newfile.txt', 'w') 
# mevcut dosyamızın bulunduğu dizine yani şu anda files klasörünün içine 'newfile.txt'
#isminde bir dosya oluşturdu.

# Oluşturulan dosyanın işimiz bittikten sonra halen daha kaynakları tüketmesini istemeyiz.
#bu yüzden dosyayı kapatmamız gerekir.
file.close()
'''

#Başka bir konumda dosya nasıl yazılır ona bakalım:
'''
file = open("C:/users/Kadir Dağdaş/desktop/newfile.txt","w")
print(file)
'''

# Dosya içine bilgi nasıl yazılır?:
'''
file = open('newfile.txt', 'w', encoding='utf-8') #Türkçe karakterleri tanıması için doysa kodunu değiştirdik. 
file.write("Kadir Dağdaş Medya Sanayi Ticaret Anonim Şirketi")
file.close()
'''
# 'a' => (Append) ekleme. Dosya konumda yoksa oluşturur. Önceki bilgiler silinmez, 
# sadece ekleme yapılmış olur.
'''
file = open('newfile.txt', 'a', encoding='utf-8')
file.write('Kadir Dağdaş Medya Sanayi ve Ticaret Limited Şirketi\n')
file.close()
print(file)
'''
# 'x' => (Create) oluşturma. Dosya zaten varsa hata verir.

file = open('newfile2.txt', 'x', encoding='utf-8')


# 'r' => (Read) okuma. varsayılan. dosya konumda yoksa hata verir.