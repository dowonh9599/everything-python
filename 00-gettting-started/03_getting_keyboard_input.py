# use input function to get keyboard input

age = input("enter your age:") # the console will stop here until you enter something
print("your age is", age)

# IMPORTANT!
# the value passed through input function ALWAYS returns string type!
num1 = input("enter your first number:")
num2 = input("enter your second number:")
print(num1,"+",num2,"is",num1+num2)

# to avoid this
## 1. permanently change the type of value in num1, num2
num1 = input("enter your first number:")
num2 = input("enter your second number:")
num1 = int(num1)
num2 = int(num2)
### or ###
num1 = int(input("enter your first number:"))
num2 = int(input("enter your second number:"))

## 2. temporarily change the type to integer when math is being done
num1 = input("enter your first number:")
num2 = input("enter your second number:")
print(num1,"+",num2,"is",int(num1)+int(num2)) # type conversion happens, but not saved in `num1` and `num2`