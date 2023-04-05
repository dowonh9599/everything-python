print("Hello World!")

# Creating Variable
first_name = "Ryan" # The value 'Ryan' is stored in a box called 'first_name'
i = 0               # the value 0 is stored in a box called 'i'
num = 32            # the value 32 is stored in a box called 'num'

print("Ryan") # will print "Ryan" at the terminal
print(first_name) # will print the value inside the 'first_name' => "Ryan"

## Data Type
# 1. integer: -4, -5, -1, 0 ,23, 56, ...
val = 5
print(type(val)) # <class 'int'>
# 2. float: 5.67, -7.82, 10.0, 11.5, ...
val = 9.54
print(type(val)) # <class 'float'>
# 3. string: "Ryan", "Dowon", "Conner", "Zoe"
val = "Zoe"
print(type(val)) # <class 'str'>
# 4. boolean: True and False, Yes and No, ...
val = True
print(type(val)) # <class 'bool'>

## Operator
# Basic Arithmetic Operators
num1 = 9
num2 = 5
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print(num1 % num2) # modulus: (num1 / num2)'s remainder
print(num1 ** num2) # num1 to the power of num2, num1^(num2)

# Assignment Operators
num3 = 15
num3 += 3 # equivalent to num3 = num3 + 3 => 15 + 3 = 18
num3 -= 4 # equivalent to num3 = num3 - 4 => 18 - 4 = 14
num3 *= 5 # equivalent to num3 = num3 * 5 => 14 * 5 = 70
num3 /= 6 # equivalent to num3 = num3 / 6 => 70 / 6 = 11.6666666...667

print(num3) # results in 11.666666...667

# Boolean Operator
num4 = 14
num5 = 19
print(num4 < num5) # True
print(num4 <= num5) # True
print(num4 > num5) # False
print(num4 >= num5) # False

print(num4 == num5) # Checking if num4 is "equal to" num5, False
print(num4 != num5) # Checking if num4 is "not equal to" num5, True

# Logical Operator
bool1 = num4 != num5 # True
bool2 = num4 > num5 # False

print(bool1 and bool2) # if there's at least one False -> results False
print(bool1 or bool2) # if there's at least one True -> results True
print(not bool1) # negates (turns into opposite) the boolean -> results False