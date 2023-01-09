# take value of length and breadth of a rectangle from the user and check if it is square or not


# length = int(input("enter the length: "))
# breadth = int(input("enter the breadth: "))

# if length == breadth:
#     print("It is square ")
# else:
#     print("It is not square ")



# A. School has following rules for grading system:
# a Below 25 F
# b. 25 to 45 E
# c. 45 to 50 D
# d.50 to 60 C
# e. 60 to 80 B
# f. Above 80 A
# ask user to enter marks and print  the corresponding grade.


# def grading_system():
#     std_grade = int(input("enter your marks: "))
#     return std_grade

# def corresponding_grade(mark,score):
#     School_grade = int(f"your marks {mark}, your scores {score}")
#     if mark >= 25:
#         return " F "
#     elif 
    


# results = grading_system()
# print(results)

# score = input("enter the mark")

# if score == 80:
#     print("A")
# elif score <= 60:
#     print("B")
# elif score <= 50:
# #     print("C")
# # elif score <= 45:
# #     print("D")
# # else:
# #     print("E")

# # write a program to priint sum averagge of all numbers, smallest and the largest element of a list.

# l1 = [12,5,8,2,3,7,4,18,0]
# def sum_list(list):
#     sum = 0
#     for i in list:
#         sum = sum + i
#     print(sum)


# sum_list(l1)
# # sum_list([1,2,3,4,5,6,7,8,9,0])



# max = l1[0]
# for i in l1:
#     if i > max:
#          max = i
# print(max)

# min = l1[0]
# for i in l1:
#     if i < min:
#         min = i
# print(min)


# write a program to calculate the electricity bill ( accept bumber of unit from user according to the following criteria:)

#    Unit                                                     Price
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)


# bill = int(input("enter the units: "))
# if bill <= 100:
#     bill = 0
# elif bill <= 200:


# units = int(input("Enter the number of units: "))
# if units <= 100:
#   bill = 0
# elif units <= 200:
#   bill = (units - 100) * 5
# else:
#   bill = (100 * 5) + (100 * 10) + ((units - 200) * 15)

# print("Total bill: Rs", bill)


# write a program to check whether the given number is even or not

# number = int(input("enter the number: "))
# x = int(number) % 2
# if x == 0:
#   print('The number is Even.')
# else:
#   print('The number is Odd.')



# Write a Python function called find_longest_word()
# that takes in a list of words and returns the longest word in the list.

# ['cat', 'window', 'defenestrate', 'feline', 'furnace']



# def find_longest_word(words):
#    longest_word = ''
#    for word in words:
#     if len(word) > len(longest_word):
#       longest_word = word
#    return longest_word
# words = ["cat", "window", "defenestrate", "feline", "furnace"]
# word1 = find_longest_word(words) 
# print(word1)
# # output defenestrate
# # input = [1,2,3]
# def sum_elements(numbers):
#    # if input == 6:
#       return sum(numbers)
# print(sum_elements([1,2,3]))


# PYthon program to swap elements

# def swapPositions(list, pos1, pos2):
#    list[pos1], list[pos2] = list[pos2], list[pos1]
#    return list
# list = [ 23, 65, 19, 90]
# pos1, pos2 = 1, 3
# print(swapPositions(list,pos1-1, pos2-1))


#output [19, 65, 23, 90]
# sum = 0
# for i in range(1,101):
#    sum = sum + 1
# print(sum)

# 
      # output1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz
# 31
# 32
# Fizz
# 34
# Buzz
# Fizz
# 37
# 38
# Fizz
# Buzz
# 41
# Fizz
# 43
# 44
# FizzBuzz
# 46
# 47
# Fizz
# 49
# Buzz
# Fizz
# 52
# 53
# Fizz
# Buzz
# 56
# Fizz
# 58
# 59
# FizzBuzz
# 61
# 62
# Fizz
# 64
# Buzz
# Fizz
# 67
# 68
# Fizz
# Buzz
# 71
# Fizz
# 73
# 74
# FizzBuzz
# 76
# 77
# Fizz
# 79
# Buzz
# Fizz
# 82
# 83
# Fizz
# Buzz
# 86
# Fizz
# 88
# 89
# FizzBuzz
# 91
# 92
# Fizz
# 94
# Buzz
# Fizz
# 97
# 98
# Fizz


# Buzz


# def add(x, y):
#   return x + y

# def subtract(x, y):
#   return x - y

# def multiply(x, y):
#   return x * y

# def divide(x, y):
#   return x / y

# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# choice = input("Enter choice(1/2/3/4): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == '1':
#   print(num1,"+",num2,"=", add(num1,num2))

# elif choice == '2':
#   print(num1,"-",num2,"=", subtract(num1,num2))

# elif choice == '3':
#   print(num1,"*",num2,"=", multiply(num1,num2))

# elif choice == '4':
#   print(num1,"/",num2,"=", divide(num1,num2))
# else:
#   print("Invalid input")



# def add(x,y):
#    return x + y
# def subtract(x,y):
#    return x - y
# def multiply(x,y):
#    return x * y
# def divide(x,y):
#    return x / y

# print("select Operation:")
# print("1.Addition:")
# print("2.Subtraction:")
# print("3.Multiplication:")
# print("4.Division:")
# user = input("enter your choice:1/2/3/4:")

# num1 = float(input("enter the First number:"))
# num2 = float(input("enter the Second number:"))

# if user == '1':
#    print(num1,'+',num2,'=',add(num1,num2))
   
# elif user == '2':
#    print(num1,'-',num2,'=',subtract(num1,num2))

# elif user == '3':
#    print(num1,'*',num2,'=',multiply(num1,num2))
# elif user == '4':
#    print(num1,'/',num2,'=',divide(num1,num2))
# else:
#    print("invalid option!!")



class circle:
   def __init__(self, radius):
      self.radius = radius

   def calculate_area(self):
      print(f"The area is {2*3.14*self.radius**2}")
   def calculate_circumference(self):
      print(f"The circumference is {2*3.14*self.radius}")


circle1=circle(7)
circle2=circle(14)
circle1.calculate_area()
circle2.calculate_circumference()
