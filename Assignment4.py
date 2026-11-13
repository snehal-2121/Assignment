1. Check whether a number is even or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


2. Find the largest of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


3. Check whether a given number is prime.
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")



4. Print the Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


5. Find the factorial of a number using a loop.
num = int(input("Enter a number: "))

fact = 1

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial:", fact)


2. String Programs
6. Reverse a string without using [::-1].
text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string:", reverse)


7. Check whether a string is a palindrome.
text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


8. Count the number of vowels and consonants in a string.
text = input("Enter a string: ")

vowels = 0
consonants = 0

for char in text.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


3. List Programs
9. Find the sum of all elements in a list.
numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num

print("Sum:", total)


10. Find the largest and smallest element in a list without using max() or min().
numbers = [45, 12, 78, 23, 9, 56]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


11. Remove duplicate elements from a list.
numbers = [10, 20, 30, 10, 40, 20, 50]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List without duplicates:", result)


12. Count how many times each element appears in a list using a dictionary.
numbers = [10, 20, 10, 30, 20, 10, 40]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)



13. Find the second-largest number in a list.
numbers = [10, 20, 40, 30, 50, 50]

largest = None
second = None

for num in numbers:
    if largest is None or num > largest:
        if num != largest:
            second = largest
        largest = num

    elif num != largest and (second is None or num > second):
        second = num

if second is None:
    print("Second largest does not exist")
else:
    print("Second largest:", second)


14. Sort a list without using sort() or sorted().
Using Bubble Sort:
numbers = [50, 20, 40, 10, 30]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)


15. Write a function that accepts a list of numbers and returns only even numbers.
def even_numbers(numbers):

    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result


data = [1, 2, 3, 4, 5, 6, 7, 8]

print("Even numbers:", even_numbers(data))


4. Advanced String & List Programs
16. Find the frequency of each character in a string.
text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequency:", frequency)


17. Check whether two strings are anagrams of each other.
Two strings are anagrams if they contain the same characters with the same frequencies.
str1 = input("Enter first string: ").lower().replace(" ", "")
str2 = input("Enter second string: ").lower().replace(" ", "")

if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not anagrams")


18. Find all duplicate values in a list.
numbers = [10, 20, 30, 10, 40, 20, 50, 30]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate values:", duplicates)


19. Take a sentence and find the longest word.
sentence = input("Enter a sentence: ")

words = sentence.split()

if words:
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest word:", longest)
    print("Length:", len(longest))
else:
    print("No words found")


5. Real-World Python Program
20. Create a student marks program.
Requirements:
1. Accept marks for 5 subjects.
2. Calculate total and percentage.
3. Assign a grade.
4. Display pass or fail.
Assumed grading system:
- 90% and above: A+
- 80%–89%: A
- 70%–79%: B
- 60%–69%: C
- 40%–59%: D
- Below 40%: Fail

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

if any(mark < 0 or mark > 100 for mark in marks):
    print("Invalid marks! Enter marks between 0 and 100.")

else:
    total = sum(marks)
    percentage = total / 5

    if any(mark < 35 for mark in marks):
        grade = "F"
        result = "Fail"

    elif percentage >= 90:
        grade = "A+"
        result = "Pass"

    elif percentage >= 80:
        grade = "A"
        result = "Pass"

    elif percentage >= 70:
        grade = "B"
        result = "Pass"

    elif percentage >= 60:
        grade = "C"
        result = "Pass"

    else:
        grade = "D"
        result = "Pass"

    print("\n----- Student Result -----")
    print("Total Marks:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    print("Result:", result)




































