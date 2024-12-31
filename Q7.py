#  7) Write a program that build a Mario pyramid like below:


num = input("Enter ur Number:")



if num.isdigit():

    num = int(num)
    for i in range(1, num +1):

        space = num - i
        print(" "*space + "*"*i)
else:

    print("Put Number broooooo!!")
    