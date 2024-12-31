# 6) Write a program that generate a multiplication table from 1 to the number passed.

num = input("Enter ur number:")

list = []

if num.isdigit():
    num=int(num)
    for i in range(1, num +1):
        row=[]
        for j in range(1 , i +1):
            row.append(j*i)
        list.append(row)

print(list)
    
