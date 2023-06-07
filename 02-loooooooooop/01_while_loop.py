# While Loop
age = 1
# if age < 18:
# 	print("You Cannot Drink Alcohol at age:", age)
# 	age += 1
# else:
# 	print("You reached age",age,",Let's get your first Soju!")

# if age < 18:
# 	print("You Cannot Drink Alcohol at age:", age)
# 	age += 1
# else:
# 	print("You reached age",age,",Let's get your first Soju!")

# if age < 18:
# 	print("You Cannot Drink Alcohol at age:", age)
# 	age += 1
# else:
# 	print("You reached age",age,",Let's get your first Soju!")

# if age < 18:
# 	print("You Cannot Drink Alcohol at age:", age)
# 	age += 1
# else:
# 	print("You reached age",age,",Let's get your first Soju!")

# if age < 18:
# 	print("You Cannot Drink Alcohol at age:", age)
# 	age += 1
# else:
# 	print("You reached age",age,",Let's get your first Soju!")

# if age < 18:
# 	print("You Cannot Drink Alcohol at age:", age)
# 	age += 1
# else:
# 	print("You reached age",age,",Let's get your first Soju!")

# if age < 18:
# 	print("You Cannot Drink Alcohol at age:", age)
# 	age += 1
# else:
# 	print("You reached age",age,",Let's get your first Soju!")
	
# # .... Until When?
# print ("Blah Blah Blah...")

# age  = 17
# if age < 18: # age = 17
# 	print("You Cannot Drink Alcohol at age:", age)
# 	age += 1
# else:
# 	print("You reached age",age,",Let's get your first Soju!")
	
# if age < 18: # age = 18
# 	print("You Cannot Drink Alcohol at age:", age)
# 	age += 1
# else:
# 	print("You reached age",age,",Let's get your first Soju!")
	
# Problem is that it is very tedious job to copy the same if statement 10 times. We must wrap redundant codes into loops.

## while loop executes the body until the associated boolean statement returns True

while (age < 18): # while age is less than 18,
	print("You Cannot Drink Alcohol at age:", age)
	age += 1
	
# ...computer exits the while loop when age is NOT less than 18, starts reading here
print("You reached age",age,",Let's get your first Soju!")

# another example of while loop
num = 0.0
while num < 10.0: # This while runs while num < 10
	num = num + 0.1 # This line is executed 10.0/0.1 = 100 times.

print("num is",int(num)) # num is 10

# Practicing while loop

# Q1
# print the following.
# *
# **
# ***
# ****

print("instead of this...")
print("*")
print("**")
print("***")
print("****")

print("do this!")
numStar = 1 # first row has 1 star
while numStar <= 4:
	print("*"*numStar)
	numStar += 1 # for every print of stars, add 1, since for every row, the number of star increases by 1
	
# HW: print those shapes below:
# Q2
#   *
#  ***
# *****
#  ***
#   *

# Q3
#   *
#  ***
# *****
#  ***
#   *

# Q4
# 1234567
#  12345
#   123
#    1

# Q5
# *@*@*@*
#  *@*@*
#   *@*
#    *