# DOSYA OKURKEN KULLANILAN FONKSİYONLAR:
'''
file = open("newfile2.txt", "r", encoding="utf-8")

content = file.read()
print(content)

file.close()
'''
# Yukarıda yaptığımız işlem bizim klasik uyguladığımız işlem.
# Bunun yerine with bloğu kullanarak da dosya açabilir ve kapatabiliriz.
# Böylece file.close()'a ihtiyacımız kalmaz çünkü blok tamamlanmış olur.
# with bloğunda file nesnesini as komutu ile tanımlamamız gerekir:

with open("newfile2.txt", "r", encoding="utf-8") as file:
    content = file.read(10)  #10 bayt oku demektir.
    print(content)
    #yapılan okumadan sonra kürsörü istediğimiz yere göndermek için seek fonk. kullanırız.
    #seek fonksiyonuna kürsörü kaçıncı bayt'a göndermek istediğimizi veririz
    file.seek(5)
    print(file.tell()) #tell fonksiyonu o anda kürsörün konumunu verir. Çıktı = 30

    content2 = file.read()
    print(content2) #bir çıktı gelmez çünkü kürsör en sonda