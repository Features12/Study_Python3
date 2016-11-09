#Есть строка, сделать проверку на то, что строка удовлетворяет следующим условиям:
#1. начинается с латинской буквы

#Number_1
a = "Hello World"
a = a.lower()
b = "qwertyuiopasdfghjklzxcvbnm"
for i in b:
    if a[0] in i:
        print("yes")

#Output:
#yes


#Number_2
import re
a = "Hello World"
re.match(r'([A-Za-z])',a)

#Output:
#<_sre.SRE_Match object; span=(0, 1), match='H'>
