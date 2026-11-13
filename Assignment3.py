1. Find the data type of every value in a mixed list.

data = [10, "Hello", 25.5, True, 100]

for item in data:
    print(item, ":", type(item))


2. Convert a nested list into a tuple of tuples.
data = [[1, 2], [3, 4], [5, 6]]

result = tuple(tuple(item) for item in data)

print(result)


3. Remove all duplicate values from a mixed list while preserving the original order.
data = [10, "Hello", 20, 10, "Python", "Hello", 30]

result = []

for item in data:
    if item not in result:
        result.append(item)

print(result)


2. Operators
4. Check whether a number is a power of 2 using operators.
num = int(input("Enter a number: "))

if num > 0 and (num & (num - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")


 5. Swap two numbers using bitwise XOR.
a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)


6. Find whether a number is divisible by both 4 and 6 using logical operators.
num = int(input("Enter a number: "))

if num % 4 == 0 and num % 6 == 0:
    print("Divisible by both 4 and 6")
else:
    print("Not divisible by both")


7. Calculate the total electricity bill using different unit rates.
Assumed rates:
- First 100 units: ₹2 per unit
- Next 100 units: ₹3 per unit
- Above 200 units: ₹5 per unit

units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")

elif units <= 100:
    bill = units * 2

elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3

else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

if units >= 0:
    print("Total electricity bill: Rs.", bill)


3. Conditional Statements
8. Check whether three sides can form a triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")


9. Determine the type of triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0 or a+b <= c or a+c <= b or b+c <= a:
    print("Invalid triangle")

elif a == b == c:
    print("Equilateral triangle")

elif a == b or b == c or a == c:
    print("Isosceles triangle")

else:
    print("Scalene triangle")


10. Create a simple ATM menu.
balance = 5000

while True:
    print("\n1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter withdrawal amount: "))

        if 0 < amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Invalid amount or insufficient balance")

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    elif choice == 3:
        print("Current balance:", balance)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")


11. Calculate income tax based on different tax slabs.
For this example, use illustrative tax slabs (not official current tax rates):
- Up to ₹3,00,000: No tax
- ₹3,00,001–₹6,00,000: 5%
- ₹6,00,001–₹9,00,000: 10%
- Above ₹9,00,000: 15%

income = float(input("Enter annual income: "))

if income < 0:
    print("Invalid income")

elif income <= 300000:
    tax = 0

elif income <= 600000:
    tax = (income - 300000) * 0.05

elif income <= 900000:
    tax = 15000 + (income - 600000) * 0.10

else:
    tax = 45000 + (income - 900000) * 0.15

if income >= 0:
    print("Income tax:", tax)


12. Create a menu-driven calculator using if-elif.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Result:", a + b)

elif choice == 2:
    print("Result:", a - b)

elif choice == 3:
    print("Result:", a * b)

elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")


4. Loops
13. Print all prime numbers between 1 and n.
n = int(input("Enter limit: "))

for num in range(2, n + 1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")


14. Find the factorial of a number using a loop.
num = int(input("Enter a number: "))

fact = 1

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial:", fact)


15. Print the Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    a, b = b, a + b


16. Check whether a number is an Armstrong number.
num = int(input("Enter a number: "))

temp = num
power = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if num >= 0 and total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


17. Reverse a number and check if it is a palindrome.
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reverse:", reverse)

if original >= 0 and original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")


18. Find the Greatest Common Divisor (GCD) of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = abs(a)
b = abs(b)

while b != 0:
    a, b = b, a % b

print("GCD:", a)


5. Functions
19. Write a function to check if a string is a palindrome.
def palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

word = input("Enter a string: ")

palindrome(word)


20. Write a function to count vowels and consonants in a string.
def count_letters(text):
    vowels = 0
    consonants = 0

    for ch in text.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

text = input("Enter a string: ")

count_letters(text)


21. Create a function to calculate simple and compound interest.
def interest(p, r, t):
    si = (p * r * t) / 100
    ci = p * (1 + r / 100) ** t - p

    print("Simple Interest:", si)
    print("Compound Interest:", ci)

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time in years: "))

interest(p, r, t)


22. Write a function to return all factors of a number.
def factors(num):
    result = []

    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)

    return result

num = int(input("Enter a number: "))

if num > 0:
    print("Factors:", factors(num))
else:
    print("Enter a positive number")



23. Write a function to find the second-largest number in a list.
def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()

    if len(unique) < 2:
        return "Second largest does not exist"

    return unique[-2]

data = [10, 20, 40, 30, 40, 50]

print("Second largest:", second_largest(data))


6. Lists
24. Merge two lists without duplicates.
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

result = []

for item in list1 + list2:
    if item not in result:
        result.append(item)

print("Merged list:", result)


25. Find the second-largest and second-smallest elements.
numbers = [10, 20, 30, 40, 50, 10]

unique = sorted(set(numbers))

if len(unique) >= 2:
    print("Second smallest:", unique[1])
    print("Second largest:", unique[-2])
else:
    print("Not enough unique elements")


26. Rotate a list to the left by k positions.
numbers = [1, 2, 3, 4, 5]

k = int(input("Enter rotation value: "))

if numbers:
    k = k % len(numbers)

    result = numbers[k:] + numbers[:k]

    print("Rotated list:", result)
else:
    print("List is empty")


27. Separate even and odd numbers into two lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)


28. Find the common elements between two lists.
list1 = [10, 20, 30, 40]
list2 = [20, 40, 50, 60]

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)



7. Tuples & Sets
29. Count the frequency of each element in a tuple.
data = (10, 20, 10, 30, 20, 10, 40)

frequency = {}

for item in data:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequency:", frequency)


30. Find the union, intersection, and difference of two sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Union:", set1 | set2)

print("Intersection:", set1 & set2)

print("Difference:", set1 - set2)


31. Check whether one set is a subset of another.
set1 = {10, 20}
set2 = {10, 20, 30, 40}

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")


8. Dictionaries
32. Count the frequency of words in a sentence.
sentence = input("Enter a sentence: ")

words = sentence.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)


33. Create a dictionary from two lists (keys and values).
keys = ["Name", "Age", "City"]

values = ["Snehal", 21, "Solapur"]

result = dict(zip(keys, values))

print(result)


34. Sort a dictionary by its values.
data = {
    "Apple": 50,
    "Banana": 20,
    "Orange": 40,
    "Mango": 60
}

result = dict(sorted(data.items(), key=lambda x: x[1]))

print("Sorted dictionary:", result)


9. File Handling
35. Read a text file and count the number of lines, words, and characters.
First create a file named sample.txt and add some text.
with open("sample.txt", "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)


36. Copy only the even-numbered lines from one file to another.
Create a file named input.txt.
with open("input.txt", "r") as source:
    lines = source.readlines()

with open("output.txt", "w") as destination:
    for i, line in enumerate(lines, start=1):
        if i % 2 == 0:
            destination.write(line)

print("Even-numbered lines copied successfully")


10. Exception Handling
37. Handle invalid integer input using try-except.
try:
    num = int(input("Enter an integer: "))

    print("You entered:", num)

except ValueError:
    print("Invalid input! Please enter an integer.")


38. Handle file-not-found errors while reading a file.
try:
    with open("sample.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: Permission denied!")


11. Modules
39. Create a random password generator using random and string modules.
import random
import string

length = int(input("Enter password length: "))

if length <= 0:
    print("Enter a positive length")

else:
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated password:", password)


40. Use the datetime module to calculate the number of days between two dates.
from datetime import datetime

date1 = input("Enter first date (DD-MM-YYYY): ")
date2 = input("Enter second date (DD-MM-YYYY): ")

d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")

difference = abs((d2 - d1).days)

print("Difference in days:", difference)








