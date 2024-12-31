# 2) Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.


value = []
i = 0

while i<5:
    num=input("Enter ur number:")
    if num.isdigit():
        num=int(num)
        value.append(num)
        i += 1
    else:
        print("Put number bro!!!")
    

value.sort()
print(value)
value.sort(reverse=True)
print(value);

