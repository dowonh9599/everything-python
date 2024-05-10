# 4.1 Function Basics
# In Math, function is a device that produces output based on input
# e.g. f(x) = 2x + 1
#   if x = 1, f(1) = 3
#   if x = 2, f(1) = 5
#   if x = 3, f(1) = 7
#   ...

# Similarly, in python, function is device which groups a number of python statements together.
# this group of statements can run by calling the "function prototype" - function name with required arguments


# f(x) = 2x + 1
# To write the same thing in python, we need to understand:
# - f? function name
# - x? function argument (input)
# - f(x)? function prototype (output)
# - 2x + 1? function body
def f(x):
    return 2 * x + 1


# a function called "g" takes the "x" as argument, and returns the squared value of x plus 13.
# In Math: g(x) = x^2 + 13
# In Python:
def g(x):
    return x ** 2 + 13


# real-life python function styles
# Let's try to build a function that does multiple jobs:
# 1. function name: find_average
# 2. function argument: List of numbers
# 3. returns the average value of all elements in the list


def find_average(li):
    # 1. add all numbers in li
    sum = 0
    for i in li:
        sum += i

    # 2. divide by total number of elements in the li
    avg = sum / len(li)

    # 3. return avg
    return avg


print("average of 2, 4, 6, 8, 10, 12, 14:", find_average([2, 4, 6, 8, 10, 12, 14]))