1 check if the no is positive,negative or zero
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")



#2 check the no is even or odd 
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")



#3 check greatest of two no
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("The greatest number is:", a)
elif b > a:
    print("The greatest number is:", b)
else:
    print("Both numbers are equal")



#4 Find greatest of three no's
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("The greatest number is:", a)
elif b >= a and b >= c:
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)



#5 check if the person is eligible for vote
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")



#6 check if a year is leap year
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("It is a Leap Year")
elif year % 100 == 0:
    print("It is not a Leap Year")
elif year % 4 == 0:
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")



#7 check if the character is vowel or constant
ch = input("Enter a character: ").lower()

if ch in "aeiou" and len(ch) == 1:
    print("It is a Vowel")
elif ch.isalpha() and len(ch) == 1:
    print("It is a Consonant")
else:
  


#8 check if the no is divisible by 5 and 11
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by 5 and 11")
else:
    print("The number is not divisible by 5 and 11")



#9 check if the no is multiple of both 3 and 7
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("The number is a multiple of both 3 and 7")
else:
    print("The number is not a multiple of both 3 and 7")



#10 Assign grades based on marks
marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 35:
    print("Grade E")
else:
    print("Fail")



 #11 Check if the character is uppercase or lowercase
ch = input("Enter a character:")
if ch >= 'A' and ch <= 'Z':
    print("Uppercase")
elif ch >= 'a' and ch <= 'z':
    print("lowercase")
else:
    print("Not an alphabet")



#12 Find whether alphabet is vowel using if-elif
ch = input ("Enter an alphabet:")
if ch == "a":
    print("Vowel")
elif ch == "e":
    print("Vowel")
elif ch == "i":
    print("Vowel")
elif ch == "0":
    print("Vowel")
elif ch == "u":
    print("Vowel")
else:
    print("Consonant")



#13 Check if three sides can form a traingle
a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side:"))

if a+b>c and a+c>b and b+c>a :
    print(" Triangle can be formed")
else:
    print("Triangle cannot be formed")



  #14 Determine types of triangle (Equilateral, Isosceles and Scalene)
a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c = int(input("Enter third side:"))

if a == b and b == c:
    print("Equilateral traingle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")



#15 Find the largest among four numbers
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter fourth number:"))

if a > b and a > c and a > d:
    print(" Largest number is:", a)
elif b > a and b > c and b > d:
    print("Largest number is:", b)
elif c > a and c > b and c > d:
    print(" Largest number is:",c)
else:
    print("Largest number is:", d)



  #16 Check if the number is three digit number
num = int(input("Enter a number:"))

if num >= 100 and num <= 999 or num >= -999 and num <= -100:
    print("Three digit number")
else:
    print("Not a three digit number")



#17 Calculate electricity bill using slab rates
units = int(input("Enter electricity units:"))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3
else:
    bill = 100 * 2 + 100 * 3 + (units - 200)* 5
print("Electricity bill is Rs.", bill)



#18 Calculate income tax based on income slabs
# income upto 2,50,000 - no tax
# 2,50,000 - 5,00,000 - 5%
# 5,00,001 - 10,00,000 - 20%
# above 10,00,000 - 30%
income = float(input("Enter your annual income:"))

if income <= 2500000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("income tax is Rs.", tax)



#19 Check if a student passes (min 35 marks in each subject)
sub1 = int(input("Enter marks in subject 1:"))
sub2 = int(input("Enter marks in subject 2:"))
sub3 = int(input("Enter marks in subject 3:"))

if sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
    print("Student passed")
else:
    print("Student failed")



#20 Find whether a number is within a given range
num = int(input("Enter a number:"))
start = int(input("Enter the starting range:"))
end = int(input(" Enter the ending range:"))

if num >= start and num <= end:
    print("Number is within the range")
else:
    print("Number is outside the range")



#21 Build simple calculator using if-elif-else
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
op = input("Enter operator (+,-,*,/):")

if op == "+":
    print("Result:", a+b)
elif op == "-":
    print("Result:", a-b)
elif op == "*":
    print("Result:", a*b)
elif op == "/":
    if b != 0:
        print("Result:", a/b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")



#22 Check if a year is century leap year
year = int(input("Enter a year:"))

if year % 100 == 0 and year % 400 == 0:
    print("century leap year")
elif year % 100 == 0:
    print("century year but not a leap year")
else:
    print("Not a century year")



 #23 Determine season based on month number
 month = int(input("Enter month number (1-12):"))
 
if month == 12 or month == 1 or month == 2:
     print("Winter")
... elif month >= 3 and month <= 5:
...     print("Summer")
... elif month >= 6 and month <= 9:
...     print("Rainy Season")
... elif month >= 10 and month <= 11:
...     print("Autumn")
... else:
...     print("Invalid month number")
... 
... 
... 
... #24 Find the number of days in a month
... month = int(input("Enter month number (1-12):"))
... 
... if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
...     print("31 days")
... elif month == 4 or month == 6 or month == 9 or month == 11:
...     print("30 days")
... elif month == 2:
...     print("28 or 29 days")
... else:
...     print("Invalid month number")
... 
... 
... 
... #25 Check whether password meets minimum conditions (length, digits etc)
... password = input("Enter password:")
... 
... if len(password) >= 8:
...     print("Valid password")
... else:
...     print("invalid password")
... 
... 
... 
... #26 Determine ticket price based on age category
... age = int(input("enter your age:"))
... 
... if age < 5:
...     print("Ticket price: Free")
... elif age <=17:
...     print("Ticket price: Rs. 100")
... elif age <= 59:
    print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 150")
  


#27 Calculate discount based on purchase amount
amount = float(input("Enter purchase amount:"))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

print("Discount:", discount)
print("Final amount:", amount - discount)



#28 Check if a person is eligible for a driving license (age and eyesight)
age = int(input("Enter your age:"))
eyesight = input("Is eyesight normal? (yes/no):")

if age >= 18 and eyesight == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")



#29 Create login system with username and password validation
username = input("Enter username:")
password = input("Enter password:")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid username or password")



#30Create menu-driven program using if-elif-else with addition,subtraction,multiplication,division and exit
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice:"))

if choice == 1:
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    print("Result:", a+b)

elif choice == 2:
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    print("Result:", a-b)

elif choice == 3:
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    print("Result:", a*b)

elif choice == 4:
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    print("Result:", a/b)

elif choice == 5:
    print("Exit")
else: