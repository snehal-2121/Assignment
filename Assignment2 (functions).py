
# 1Even or Odd Function
def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(is_even(num))


# 2Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(20, 15))


# 3Print Numbers (1 to N)
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

num = int(input("Enter a number: "))
print_numbers(num)


# 4Sum of Numbers
def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

num = int(input("Enter a number: "))
print("Sum:", sum_n(num))


# 5Multiplication Table
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

num = int(input("Enter a number: "))
table(num)


# 6Count Even Numbers
def count_even(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1

    return count

print(count_even([1, 2, 3, 4, 6]))


# 7Find Maximum Without Using max()
def find_max(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

print(find_max([10, 25, 5, 40, 15]))


# 11FizzBuzz
def fizzbuzz():
    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)

fizzbuzz()


# 12Palindrome Checker
def palindrome(s):
    s = s.lower()

    if s == s[::-1]:
        return True
    else:
        return False

word = input("Enter a word: ")

print(palindrome(word))


# 13Count Vowels
def count_vowels(s):
    count = 0

    for ch in s.lower():
        if ch in "aeiou":
            count += 1

    return count

word = input("Enter a string: ")

print("Vowels:", count_vowels(word))


# 14Second Largest Number Without Using sort()
def second_largest(numbers):

    largest = float('-inf')
    second = float('-inf')

    for num in numbers:

        if num > largest:
            second = largest
            largest = num

        elif largest > num > second:
            second = num

    if second == float('-inf'):
        return "Second largest number does not exist"

    return second

print(second_largest([10, 20, 40, 30, 50]))


# 15Guessing Game
import random

def guessing_game():

    secret = random.randint(1, 10)

    print("Guess a number between 1 and 10")

    while True:

        guess = int(input("Enter your guess: "))

        if guess == secret:
            print("Congratulations! Correct Guess!")
            break

        elif guess < secret:
            print("Too Low! Try Again")

        else:
            print("Too High! Try Again")

guessing_game()


# 16Grade Function
def grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "F"

marks = int(input("Enter your marks: "))

print("Your Grade:", grade(marks))
