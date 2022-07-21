# print("Hello World!");

# if 5 > 2:
#     print("Five is greater than two!")

# name = "Joezer Cardoza"
# age = 23

# print("My name is "+ name + "and my age is " + age)

# firstname = input("Enter your first name: ")
# # lastname = input("enter your last name: ")

# # print("Your Full name is ",firstname, lastname)
# #strings and integers
# print('o----')
# print(' ||||' * 2)

# price = 10 #int
# rating = 4.9 #float
# name = 'Joezer' #string
# is_Publish = False #boolean
# print(price)

# name = 'John Smith'
# age = 20
# new_patient = True
# print("He is a new patient his name is", name, "he is", age , "years old")

# name = input('What is your name? ')
# fav_color = input('what is your favorite color? ')
# print(name + " likes " + fav_color)

# weight = input('your weight(in pounds)? ')
# print(weight ,'lb')
# converstion = float(weight) / 2.205
# print(converstion , 'kgs')

# course = "python's course for beginners"
# print(course)

# name = 'Jennifer'
# print(name[1:-1])

# arr1 = [1,3,5]
# arr2 = [2,4,6]
# median = (arr1, arr2) = 3.5

# x = (2 + 3) * 10 - 3
# print(x)

# import math
# print(math.floor(3.5))

# good_credit = False

# if good_credit:
#     print("You need to put down 10%")
# else:
#     print("You need to put down 20%")
# print("Price of the house is $1M")

# price = 1000000
# good_credit = False

# if good_credit:
#     downpayment = 0.1 * price
# else:
#     downpayment = 0.2 * price
# print(f"Down payment: ${downpayment}")

#Pass the value of a variable to another variable

# x = "a"
# y = "hello"
# x = y
# print(x)
# print(y)

# world = 'Hello World! '
# print(world[6:-1])

# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"you are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

# numbers_arry = {10, 324 , 45, 90}
# print(min(numbers_arry))

# maxi = numbers_arry[0]
# for number in numbers_arry:
#     if number>maxi:
#         maxi = number
# print("maximum value is ", maxi)


# fruits = ["apple" , "banna", "cherry"]
# for x in fruits:
#     if x == "cherry":
#         break
#     print(x)

# numbers=list(map(int,input().split()))
# print(max(numbers))

# list1 = [10,21,4,45,66,93]
# for num in list1:
#     if num % 2 == 0:
#         print(num, end=" ")

# has_high_income = True
# has_good_credit = True

# if has_high_income and has_good_credit:
#     print("eligable to loan")

# temperature = 35

# if temperature != 30:
#     print("It's hot day")
# else:
#     print("It's not a hot day")

# name = "J"

# # print(len(name))
# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good!")

# weight = int(input("Weight: "))
# unit = input('(L)bs or (K)g): ')

# if unit.upper() == "L":
#     converted = weight * 45
#     print(f"You are {converted}kilograms")
# elif unit.upper() == "K":
#     converted = weight / 45
#     print(f"You are {converted}pounds")
# else:
#     print("no input")

# i = 1
# while i <= 5 :
#     print('*' * i)
#     i = i + 1
# print("done")

# sec_code = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == sec_code:
#         print('You won!')
#         break
# else:
#     print('Sorry, you failed!')

# Detail_input = input('> ')
# while Detail_input == "help":
#     print("start - to start the car")
#     print("stop - to stop the car")
#     print("quit - to exit")
#     if Detail_input == "start":
#         print("Car started...Rady to go!")
#     elif Detail_input == "stop":
#         print('Car stopped.')
#     elif Detail_input == "quit":
#         break

# else:
#     print("I don't understand that...")

# print("""
# need help??
# """)
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
# start- to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that")

# prices = [10 , 20 , 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")


# #pass the value of a variable to another variable
# first_variable = "a"
# second_variable = "hello world"

# first_variable = second_variable
# print(first_variable)
# print(second_variable)

# #anything na string manipulation get world! in hello world! string

# word_manipulation = "Hello World! "
# print(word_manipulation[5:-1])

# #Get the highest number in an array
# arr = [1, 324, 45, 90]
# print(min(arr))

# numbers = list(map(int,input().split()))
# print(max(numbers))

# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
# print('done')

# for x in range(4):
#     for y in range(3):
#         print(f'{x},{y}')

# numbers = [1 ,1 ,1 ,1 ,5]
# for x in numbers:
#     print('x' * x)

# numbers = [5,2,5,2,2]
# for x_count in numbers:
#     output=''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

# highest_number = [1,5,6,8,9,20,50,46,77,88,33]
# max = highest_number[0]
# for number in highest_number:
#     if number > max:
#         max = number
# print(max)

##Function

# def my_function():
#     print("Hello from a function")
# my_function()

# def my_function(fname):
#     print(fname + " Refsnes")
# my_function("Joe")
# my_function("Job")
# my_function("Jean")

##Write a program to remove the duplicates in a list.

# numbers = [2,2,4,6,3,4,6,1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# from statistics import median
# arr1 = [201,205,208,2010]
# arr2 = [5,6,7,8]
# arr3 = arr1 + arr2
# arr3.sort()
# print(median(arr3))

# arr1 = [201,205,208,2010]
# arr2 = [5,6,7,8]
# arr3 = (arr1 + arr2)
# arr3.sort()
# length_number = len(arr3)

# if length_number % 2 == 0:
#     median1 = arr3[length_number//2]
#     median2 = arr3[length_number//2 - 1]
#     median = (median1 + median2) / 2
# else:
#     median = arr3[length_number//2]
# print("Median is: "+str(median))
# A naive recursive implementation
# of 0-1 Knapsack Problem

# Returns the maximum value that
# can be put in a knapsack of
# capacity W

#1234 then converts to words

# Phone = input("Phone: ")
# digits_mapping= {
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four"
# }
# output = ""
# for ch in Phone:
#     output += digits_mapping.get(ch)
# print(output)

# from statistics import median


# name = "joe"
# age = 20
# number = 1.2
# email = "Joezer@yaho.com"
# max  = input()
# if max == 0:
#     print("?")
# else:
#     print("nevermind")

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]
# arr3 = arr1+arr2
# arr3.sort()
# print(median(arr3))

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]
# arr3 = arr1+arr2
# arr3.sort()
# length_number = len(arr3)
# if length_number % 2 == 0:
#     median1 = arr3[length_number//2]
#     median2 = arr3[length_number//2 - 1]
#     median = (median1 + median2)/2
# else:
#     median = arr3[length_number//2]
# print(str(median))

# for number in range(3):
#     print("Attempt", number)

# count = 0
# for number in range (1, 10):
#     if number % 2 == 0:
#         count +=  1
#         print(number)
# print(f"count: {count}")

#Function

# def greet_user(first_name , lastname):
#     print(f"Hi {first_name} {lastname}")
# greet_user(lastname="cardoza" ,first_name="Joe")

# def square(number):
#     return number * number
# print(square(3))

# def emojis_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😊",
#         ":(": "😥"
#     }
#     output =""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
# message = input(">")
# print(emojis_converter(message))

#try and except

# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid value')

# def square(number):
#     return number + number
# print(square(5))

#Class

# class point:
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
# point_dec = point()
# point_dec.move()

#Constructors

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi, Im {self.name}")
         
# Joe = Person("Joe zer")
# Joe.talk()