# 5)Write a program that prints the locations of "i" character in any string you added.


text = input("Enter ur word bro!!:")

location =[]

for index in range(len(text)):
    if text[index] == 'i' or text[index] == 'I':
        location.append(index)


print("Locations of 'i':",location)


