# Programming Basics (Python Basics)
# Variables
# Data Types
# Type Casting
# Operators
# Input / Output
# Conditional Statements
# Loops
# Functions
# Basic Error Handling

# VARIABLES:

# name = "aman kapil"
# age = 24
# print(name)

# city = "London"
# print(city)
# city = "manchester"
# print(city)

# name = "iphone"
# price = 300
# quantity  = 3
# total = price * quantity
# print(total)

# Math = 23
# science = 54
# english = 45
# total = (Math + science + english)/3
# print ( total)

# DataType:
# 1 STRING:- a string is always in the quests "aman"like this if number is alos in it than it is also a string like "30"
# String concatenation : USING THE SPECIAL CHARECTER.
# first_name = "aman"
# last_name = "kapil"
# final_name = "prince"
# full_name = first_name+" "+last_name+" "+final_name
# print(full_name)

# USING THE .JOIN METHOD:-
# structure = ["Aman","Kapil","future","CM","HIMACHAL","2040"]
# result = " ".join(structure)
# print(result)

# feature = ["car","is","model","2026"]
# result = "  ".join(feature)
# print(result)


# price = ['this','is',"very","expensive"]
# result = " ".join(price)+ " product"
# print(result)

# USING THE "F" STRING METHOD:
# age = 26
# work_place = "Deep Mind"
# year = 2028

# result = (f"the age of the guy is {age} and working in a biggest AI company {work_place} in year {year}")
# print(result)

# STRING REPETATION:- USE FOR REPEAT THE SAME RESULT  as much time we want
# fruit = "apple"
# result = (fruit * 5)
# print ( result)

# String Indexing:- want result only one specific latter.
# word = "elephant"
# print(word[0])
# print(word[1])
# print(word[2])

# NEGATIVE INDEXING:-
# place = " London"
# print(place[-1])

# STRING SLICING : CHOOSE ONLY THE SPECIFIC PORTION OF THE SENTENCE OR THE WORD.[0:3] means count from 3 to 3 only.
# SKIPS CHARACTERS: IT WILL HELP TO SKIP CHARACTER [0:3:2] means count character after 2 steps.
# vehicle = "Rubicon"
# print(vehicle[0:4])
# print (vehicle[0:7:2])

# STRING LENGTH : to know thw length of the character.
# happy = "Mountains"
# print(len(happy))
# for the all latter upper case AND THE LOWER CASE:-
# print(happy.upper())
# print(happy.lower())

# REPLACE TEXT : this will help to replace the previous written text with the new one.
# place = "my favorite place in india is Manali"
# print (place)
# result = place.replace("Manali","Kullu")
# print (result)

# CHECK IF THE WORD EXIST: IT EXPLAIN THE USE OF IT BY ITSELF.
# INDIA = "india is a great country"
# print("great" in INDIA)

# INTEGER integers Are the whole numbers
# age = 20
# print (age)
# print(type(age))

# FLOT are the decimal numbers. flot + integer gives the result float.
# price = 30.9
# another = 20
# result = price + another
# print (result)

# BOOLEAN GIVES THE RESULT IIN TRUE AND FALSE
# price = True
# another = False
# print(price)

# TYPE CASTING: CHANGE ONE DATATYPE TO ANOTHER FORM LIKE CHANGING STRING TO INTEGER AND FLOAT TO INTEGER.
# x = 20
# x = str(x)
# print(x+"5")

# x = 99.5
# print(int(x))

# x = "50"
# x = int(x)
# print(x + 10)

# print(bool(1))

# x = False
# x = int(x)
# print(x + 10)

# x = "100"
# print(x * 2)

# x = "50"
# x = int(x)
# x = x + 25
# x = str(x)
# print(x + "5")

# x = 10
# x = str(x)
# x = x * 2
# x = int(x)
# print(x)

# x = "7"
# x = int(x)
# x = x + int("3")
# x = float(x)
# print(x)

# x = "99"
# x = int(x)
# x = bool(x)
# x = int(x)
# x = str(x)
# print(x + "0")

# x = ""
# x = bool(x)
# x = int(x)
# x = str(x)
# print(x)

# x = "20"
# x = int(x)
# x = str(x)
# x = x + "5"
# x = int(x)
# x = float(x)
# print(x / 5)

# x = "1"
# x = bool(x)
# x = int(x)
# x = str(x)
# x = x + "0"
# print(x)

# x = 10.9
# x = int(x)
# x = bool(x)
# x = int(x)
# x = str(x)
# print(x * 3)

# x = "5"
# x = int(x)
# x = x*2
# x = str(x)
# x = x + "5"
# x = int(x)
# x = bool(x)
# print(x)

# OPRATERS:-
# ARITHMETIC OPERATORS: ADDITION, SUBTRACTION,MULTIPLICATION,DIVISION,FLOOR DIVISION,MODULUS,POWER

# ADDITION:-
# X = 23
# Y = 67
# print(X + Y)

# Substraction:-
# x = 78
# y = 56
# print(x - y)

# Multiplication:
# x = 67
# y = 89
# print ( x* y)

# Division:
# x = 45
# y = 4
# print (int(x / y))

# Floor division:
# print(34//4)
# print(-34 // 4)

# POWER:-
# print(7**2)

# MODULUS:- after the pair of group what is the remainder.
# print(45 % 6)

# Comparison operator: >,<,>=,<=,==,!=
# print(10==10)
# print (2!=2)

# LOGICAL OPERATORS: AND , OR , NOT.
# AND:- for this both the condition are true.
# temp = 20
# if temp > 12 and temp < 23:
#   print(f"the temprature {temp}is acceptable" )
# else:
#    print ("this is not good")

# username = input ("enter the user name  ")
# password = input ("enter the password;   ")
# if username == "admin" and password == "011234":
#    print(" all details are correct")
# else:
#    print( " something is not right")


# marks = int(input( " enter the marks : "))
# attendance = int(input(" enter the attendance:")
# if marks > 50 and attendance > 70:
#    print(" student is pass")
# else:
#    print("student get low marks")

# age = int(input("enter the age "))
# country = input("enter the country ")
# balance = int(input("enter the ammount "))
# email_varified = True
# if age>18 and balance > 1000 and country == "uk"and email_varified:
#   print("access granted")
# else:
#    print("access denied")

# fill = input("enter the password  ")
# if len(fill)>8 and "@" in  fill:
#    print("this is acceptable")
# else:
#    print(" this is unacceptable")

# num = int(input("enter the number: "))
# if num>10 and num<50:
#    print(" it is correct ")

# user = int(input(" enter the user age : "))
# eats = True
# payment = True
# internet = True
# if user > 18 and seats == True and payment== True and internet == True:
#    print("you have reserved seat ")
# else:
#    print("you have not reserved seat ")

# OR: OUT OF TWO CONDITION ONE MUST BE TRUE
# username = input ("enter the username :")
# email = input("enter the emmail address ")
# phone_number = input ("enter the phone number ")
# if username == "admin" or email == "amankapil@gamil.com" or phone_number == "9805234002":
#    print("you are logged in ")
# else:
#    print(" access not granted ")

# salary = int(input(" enter the salary :"))
# score = int(input("enter the credit score"))
# value = int(input(" enter the property value "))
# guarantor = True
# if salary > 5000 or score > 750 or value > 1000000 or guarantor == True:
#    print (" bank loan is approved")
# else:
#    print(" bank loan is rejected")

# NOT : it will give the opposite result.

# username = input("Enter the user name ")
##suspended = False
# if username == "admin" and not suspended:
#    print ( " login ")
# else:
#    print(" login failed")

# payment = True
# expired = False
# blacklisted = False
# if payment == True and not expired and not blacklisted:
#    print ("flight ticket is confirmed")
# else:
#    print ("flight ticket is not confirmed")

# ASSSINGMENT OPERATORS: SHORTCUT TO ADD subtract and multiply .......
# x = 10 instead  of x = x + 10
# x+=5
# print (x)

# subtract
# y = 8
# y-=4
# print(y)

# MEMBERSHIP OPERATORS : IN , NOT IN
# inventory = ["laptop", "mouse", "keyboard", "monitor"]
# product = input("Enter product name: ")
# if product in inventory:
#    print( "true")

# message = input("Enter message: ")
# forbidden_words = ["hack", "spam", "scam"]
# if message in forbidden_words:
#    print("True")

# word = "python"
# print("t" in word )

# Identity operators : is or is not
# x = 30
# y = x
# print (x is y )
# print ( x is not y)


# age = int(input(" enter teh age: "))
# Movie_type= input(" enter the movie type here ")
##if age >= 18 and Movie_type == "adult":
#   print("your ticket is booked")
# elif Movie_type == "normal":
#    print(" ticket is booked")
# else:
#    print(" Booking denied ")

# name = " aman "
# age = 24
# country = " india"
# salary = 2600000
# print(f" teh name of the person is {name} and the age is {24} belongs to the country {country}.he earns monthly {salary}")

# COMPARISON OPERATORS : IF ELIF AND ELSE.
# marks = int(input("Enter the marks "))
# entrance_score = int(input(" Enter the score here "))
# sports_quota = True
# interview = "passed"
# if marks >75 and entrance_score > 80 and sports_quota == True and interview == "passed":
#    print (" you got your offer latter")

# age = int(input(" ENter the valid age "))
# salary = int ( input (" enter the valid salary details :"))
# credit_score = int ( input ( " credit score :"))
# existing_loans = int(input (" how many loans are pending "))
# nationality = "Indian"

# if age > 21 and salary > 50000 and credit_score >750 and existing_loans <2 and nationality =="Indian":
#    print (" your loan is approved ")
# else:
#    print (" your loan is rejected")

# amount = 3000
# gst = 18
# tip = 100
# members = True
# total = amount + (amount * gst / 100) + tip
# if members:
#    total = total - 300
#    print(" here is your final bill:", total)


#  FOR LOOPS  used WHEN WE KNOW HOW MANY TIMES WE REPEAT : WHILE LOOPS : WHEN THE CONDITION IS TRUE
# FOR LOOPS:
# num = 5
# for i in range(1,10):
#    print(num * i)

# even = 0
# odd = 0
# for i in range(10):
#    if i % 2 == 0:
#        even +=1
#    else:
#        odd +=1
# print(" even: ", even)
# print(" odd: ", odd)

# for i in range(3):
#    password = input("Enter your password: ")
#    if password == "python123":
#        print("access is granted")
#        break
#    else:
#        print("wrong password")
# else:
#    print("Account blocked")

# name = "python"
# reverse = ""
# for i in name:
#    reverse = i + reverse
# print(reverse)

# string = "appleissweet"
# count = 0
# for i in  string:
#    if i in "aeiou":
#        count+=1
# print("vowels are",count)

# num = str(9805234002)
# reverse = ""
# for i in num:
#    reverse = i + reverse
# print(reverse)

# list = [12,45,7,89,23]
# largest = list[0]
# for i in  list:
#    if i > largest:
#        largest = i
# print(largest)

# password = input( "Enter the password:")
# has_digit = False
# contain = False
# for i in password:
#    if i.isdigit():
#        has_digit = True
#    if i == "@":
#        contain = True
# if len(password) >=8 and has_digit and contain:
#     print("access granted")
# else:
#    print (" access denied")

# num = "1234"
# repeat = ""
# for i in num:
#    repeat = repeat + i
#    print(repeat)

# word = "PyThon"
# upper_count = 0
# lower_count = 0
# for i in word:
#    if i.isupper():
#        upper_count +=1
#    elif i.islower():
#        lower_count +=1
# print(f"the lower words are {lower_count}")
# print(f" the upper words are {upper_count}")

# word = "Python is powerful"
# result = " "
# for i in word:
#    if i != " ":
#        result +=i
# print(result)

# num = 7
# for i in range(1,11):
#    result = num * i
#    print (f"{num} * {i} = {result}" )

# word = "python123"
# result = ""
# for letter in word:
#    if not letter.isdigit():
#        result +=letter
# print(result)

# password = input("enter your password here :")
# has_special = False
# has_digit = False
# has_lower = False
# has_upper = False
# for p in password:
#    if p.isdigit():
#        has_digit = True
#    elif p.isupper():
#        has_upper = True
#    elif p.islower():
#        has_lower = True
#    elif p == "@":
#        has_special = True
# if len(password)>8 and has_digit and has_lower and has_upper and has_special:
#    print("strong password")
# else:
#    print("weak password")

#WHILE LOOP:---- while loop start working while the loop is true.
# i = 1
# while i <= 50:
#    if i % 2 == 0:
#        print(i)
#    i += 1

# i = 1
# while i <= 10:
#  print(i)
#  i = i + 1

# i = 1
# total = 0
# while i <=100:
#    total = total + i
#    i = i + 1
# print(total)

# num = 7
# i = 1
# while i <= 10:
#    print(f"{num} * {i} = {num * i} ")
#    i = i + 1

# attempt = 1
# correct_password = "python123"
# while attempt <= 3:
#    password = input("enter the password here : ")
#    attempt +=1
#    if password ==correct_password:
#        print("Access Granted")
#    else:
#        print("Access denied")
# print()

# num = 1
# count = 0
# while num<=5:
#    count += num
#    num = num + 1
# print(count)

# secret_number = 7
# while True:
#    number = int(input("enter the number here"))
#    if number == secret_number:
#        print(" you got it ")
#        break
#    else:
#        print(" enter again ")

# num = 1234
# reverse = 0

# while num > 0:

#    digit = num % 10
#    reverse = reverse * 10 + digit
#    num = num // 10

# print(reverse)

# num = 1
# count = 0
# while num <= 5:
#    num = num + 1
#    count = count + 1
# print(count)

# total = 0
# while True:
#    number = int(input("enter the number: "))
#    if number == 0:
#        break
#    total = total + number
# print(total)

# num = int(input("enter the number "))
# total = 0
# while num > 0:
#    digit = num % 10
#    total += digit
#    num //= 10
# print(total)


# number = int(input("enter the number here : "))
# is_prime = True
# divisor = 2
# while number > divisor:
#    if number % divisor == 0 :
#        is_prime = False
#        break
#    divisor += 1
# if is_prime and number > 1:
#     print(" it is prime number" )
# else:
#     print ("it is not prime number")

# n = 6
# first = 0
# second = 1
# count = 0
# total = 0
# while count < n:
#    print(first)
#    next = first +second
#    first = second
#    second = next
#    count += 1
#    total = total + next
# print(total)

# FUNCTIONS :--> functions are reused  the codes.

# def check_password(password):
#    uppercase = False
#    lowercase = False
#    digit = False
#    special = False
#    length = False

#    for p in password:
#       if p.isdigit():
#         digit = True
#       if p.isupper():
#         uppercase =  True
#       if p.islower():
#         lowercase = True
#       if p == "@":
#         special = True
#       if len(password) >= 8:
#         length = True
#    if uppercase and lowercase and digit and special and length:
#         return "strong password"
#    else:
#         return "weak password"
# password = "Aman09kapil@"
# result =check_password(password)
# print(result)


# def is_prime(num):
#   if num <= 1:
#       return False
#   for i in range(2,num):
#       if num % i == 0:
#           return False
#       else:
#           return True
# result = is_prime(7)
# print(result)


# def withdraw(balance,amount):
#    amount = int(amount)
#    balance = int(balance)
#    if balance < amount:
#        return "insufficient funds"
#    else:
#        balance -= amount
#        return f" withdrawal successful and the remaing balnce is {balance} "
# result = withdraw(5000,2000)
# print(result)

# def student_grades(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     else:
#         return "Fail"
# result = student_grades(45)
# print(result)

# marks = [78, 95, 64, 88, 92, 55]
# def marks_obtained(data):
#    total = 0
#    highest = data[0]
#    lowest = data[0]
#    passed = 0
#    failed = 0
#    for i in data:
#        total += i

#        if i > highest:
#            highest = i

#        if i < lowest:
#            lowest = i

#        if i >= 40:
#            passed += 1
#        else:
#            failed += 1

#   average = total / len(data)
#    print("average marks :",average)
#    print("passed student",passed)
#    print("Failed student",failed)
#    print("highest marks",highest)
#    print("lowest marks",lowest)
# marks_obtained(marks)

# data = ["Python", "", "Data", " ", "Science", None]
# def cleaning(words):
#    clean_data = []
#    for w in words:
#        if w != "" and w != " " and w is not None:
#            clean_data.append(w)
#    return clean_data
# result = cleaning(data)
# print(result)

# number = [10,20,30,40]
# def normalised(data):
#   norm = []
#   minimum = min(data)
#   maximum = max(data)
#   for i in data:
#       value = (i-minimum) / (maximum - minimum)
#       norm.append(value)
#   return norm
# result = normalised(number)
# print(result)

# messages = ["win money now", "hello friend", "free offer"]
# def spam_count(data):
#    count = 0
#    for i in data:
#        if "win" in i or "free" in i or "offer" in i:
#            count += 1
#    return count
# result = spam_count(messages)
# print(result)