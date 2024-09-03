#string ifadelerin içindeki her bir karakter aslında bir liste'nin elemanını temsil ediyor.

message= "Hello There. My name is Kadir Dağdaş"

my_list = [1,2,3]
print(my_list)

my_list = ["bir", 2 , True, 5.6]
print(my_list)

#str ifadelerde olduğu gibi list ifadeler de toplanabilir:

# list1 = ["one", "two", "three"]
# list2 = ["four", "five", "six"]
# numbers = list1 + list2
# print(numbers)
# print(len(numbers))
# print(message[0])

userA = ["Kadir", 23]
userB = ["Sadık", 36]
userC = ["Çınar", 40]

users = userA + userB + userC
print(users)

#string ifadelerde olduğu gibi listeleri toplamak yerine listeler ile yeni bir liste yapılabilir:

users = [userA, userB, userC]
print(users)

#listenin listesi içindeki bir elemanın da içinden bir elemanı çağırabiliriz:

a = users[1]
print(a[0])

#veya

print(users[1][0])