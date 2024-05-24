# Question 1: Greeting Function
# Write a function named greet that takes a name as an argument and prints a greeting message to the console.
# For example, greet("Alice") should print "Hello, Alice!"
def greet(name):
  print("Hello,", name, "!")

# Question 2: Absolute Value
# Create a function named my_abs that takes a number and returns its absolute value without using the abs() built-in function.
# For instance, my_abs(-5) should return 5, and my_abs(3) should return 3.
def my_abs(num):
    if num < 0:
        print(-num)
    else:
      print(num)
    pass

# Question 3: Area of a Circle
# Define a function named circle_area that computes the area of a circle. The function should take the radius of the circle as an argument and return the area.
# Use the formula: area = pi * r^2 (you can use 3.14159 as an approximation for pi).
def circle_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    print(area)
# Question 4: Maximum of Two Numbers
# Write a function named max_of_two that takes two numbers as arguments and returns the larger of the two. For example, max_of_two(4, 7) should return 7.
def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
# Question 5: Sum of a List
# Create a function called sum_list that takes a list of numbers as an argument and returns the sum of all elements in the list.
# For instance, sum_list([1, 2, 3, 4]) should return 10.
def sum_list(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
# Question 6: Count Vowels
# Define a function named count_vowels that takes a string and returns the number of vowels in that string.
# Consider 'a', 'e', 'i', 'o', and 'u' as vowels for this exercise.
def count_vowels(word):
    counts = 0
    for i in word:
        if i == 'a':
            counts += 1
        if i == 'e':
            counts += 1
        if i == 'i':
            counts += 1
        if i == 'o':
            counts += 1
        if i == 'u':
            counts += 1
    return counts

def count_vowels_2(word):
    VOWELS=list("aeiou")
    counts = sum(v in VOWELS for v in word) # summing boolean list => True = 1, False = 0
    return counts


print(count_vowels_2("apple"))

# Question 7: Factorial
# Write a function named factorial that computes the factorial of a given number.
# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. For example, factorial(5) should return 120.

def factorial(number):
    if number == 0:
        return 1
    else:
        first = 1
        for j in range(1, number+1):
            first * j
        return first
# Question 8: Fibonacci Sequence
# Create a function named fibonacci that takes a number n and returns the nth number in the Fibonacci sequence.
# Recall that the sequence starts with 0, 1, and each subsequent number is the sum of the previous two.
def fibonacci(n):
    num1 = 0
    num2 = 1
    seq = []
    for i in range(n):
        # find entry for fibonacci seq by summing numbers of the previous two
        num3 = num1 + num2
        seq.append(num3) # append entry to the list seq
        num1 = num2 # override num1 with num2
        num2 = num3 # override num2 with num3
    return seq
print(fibonacci(5))

# Question 9: Palindrome Checker
# Define a function named is_palindrome that checks whether a given string is a palindrome
# (reads the same forward and backward). For example, is_palindrome("radar") should return True, while is_palindrome("python") should return False.
def is_palindrome(pal):
    reversed_pal = pal[::-1]
    if reversed_pal == pal:
        print("True")
    else:
        print("False")

# Question 10: Temperature Converter
# Write a function named convert_to_celsius that converts a temperature from Fahrenheit to Celsius.
# The formula to convert Fahrenheit to Celsius is (F - 32) * 5/9. For example, convert_to_celsius(95) should return 35.
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius