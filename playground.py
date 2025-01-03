# # Write a function that accepts two arguments (length, start) to generate an array of a specific length filled with integer numbers increased by one from start

# def generateArray(length, start):
#     result = []
    
#     for i in range(length):        
#         result.append( start + i)

#     return result


# print(generateArray(5,10))




# def generate_Array(len , start):
#     result = []
#     k =0 

#     for i in range(len):
#         result.append(start + k)
#         k += 1

#     return result    

# print(generate_Array(5,10))




# 02) write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is divisible by both return "FizzBuzz"

# def FizzBuzz(num):
   
#    if num % 3 == 0 and num % 5 == 0:
#       return "FizzBuzz"
   
#    elif num % 3 == 0:
#       return "Fizz"
   
#    elif num % 5 == 0:
#       return "Buzz"
   
#    else:
#       return num


# number = int(input("Enter Your Number:"))
# print(FizzBuzz(number))






# 03) Write a function which has an input of a string from user then it will return the same string reversed.

# def reverse_string(input_string):

#     return input_string[::-1]


# string_input = input("Enter your string pls:")
# print(reverse_string(string_input))



# 04) Ask the user for his name then confirm that he has entered his name(not an empty string/integers). then proceed to ask him for his email and print all this data (Bonus) check if it is a valid email or not

# import re


# def checkEmail(email):
#     if re.match(r"[^@]+@[^@]+\.[^@]+", email):
#         return True

# def userData():

#     name = input("Enter your Name:").strip()

#     if not name or name.isdigit():
#         print("pls enter vaild name")
#         return
    

#     email = input("Enter your email:").strip()

#     if not checkEmail(email):
#         print("pls enter valid email")
#         return
#     print(f"Name: {name} \n Email:{email}")


# userData()







# Write a function that takes a string and prints the longest alphabetical ordered substring occurred For example, if the string is 'abdulrahman' then the output is: Longest substring in alphabetical order is: abdu


# def longest_substring(string):
#     current = string[0]
#     longest = string[0]

#     for i in range(1, len(string)):
#         if string[i] >= current[-1]:
#             current += string[i]
#             if len(current) > len(longest):
#                 longest = current
#         else:
#             current = string[i]

#     return longest


# input_string = input("Enter your string pls:")

# print(longest_substring(input_string))


# 06) Write a program which repeatedly reads numbers until the user enters “done”.
#  - Once “done” is entered, print out the total, count, and average of the numbers.
#  - If the user enters anything other than a number, detect their mistake, print an error message and skip to the next number.


def calculate():
    total = 0
    count = 0

    while True:
        try:
            user_input = input("Enter a number:")
            if user_input == "done":
                break
            else:
                total += int(user_input)
                count += 1
        except:
            print("Invalid input")
            continue


    print(f"Total: {total} \n Count: {count} \n Average: {total/count}")

calculate()
