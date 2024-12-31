# 4) Write a program that remove all vowels from the input word and generate a brief version of it

word = input("Enter ur word :")

vowels = "aeiouAEIOU"

result =""

for i in word:
    if i not in vowels:
        result = result + i

print(result)        

