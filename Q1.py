# 01) Write a program that counts up the number of vowels [a, e, i, o,u] contained in the string.


string = input("Enter ur word man!!:")

vowels = "aeiouAEIOU"

count = 0

for i in string:
    if i in vowels:
        count +=1

print("number of vowels:",count)