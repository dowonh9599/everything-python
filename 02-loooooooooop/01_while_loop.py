# # While Loop
# age = 1
# # if age < 18:
# # 	print("You Cannot Drink Alcohol at age:", age)
# # 	age += 1
# # else:
# # 	print("You reached age",age,",Let's get your first Soju!")

# # if age < 18:
# # 	print("You Cannot Drink Alcohol at age:", age)
# # 	age += 1
# # else:
# # 	print("You reached age",age,",Let's get your first Soju!")

# # if age < 18:
# # 	print("You Cannot Drink Alcohol at age:", age)
# # 	age += 1
# # else:
# # 	print("You reached age",age,",Let's get your first Soju!")

# # if age < 18:
# # 	print("You Cannot Drink Alcohol at age:", age)
# # 	age += 1
# # else:
# # 	print("You reached age",age,",Let's get your first Soju!")

# # if age < 18:
# # 	print("You Cannot Drink Alcohol at age:", age)
# # 	age += 1
# # else:
# # 	print("You reached age",age,",Let's get your first Soju!")

# # if age < 18:
# # 	print("You Cannot Drink Alcohol at age:", age)
# # 	age += 1
# # else:
# # 	print("You reached age",age,",Let's get your first Soju!")

# # if age < 18:
# # 	print("You Cannot Drink Alcohol at age:", age)
# # 	age += 1
# # else:
# # 	print("You reached age",age,",Let's get your first Soju!")

# # # .... Until When?
# # print ("Blah Blah Blah...")

# # age  = 17
# # if age < 18: # age = 17
# # 	print("You Cannot Drink Alcohol at age:", age)
# # 	age += 1
# # else:
# # 	print("You reached age",age,",Let's get your first Soju!")

# # if age < 18: # age = 18
# # 	print("You Cannot Drink Alcohol at age:", age)
# # 	age += 1
# # else:
# # 	print("You reached age",age,",Let's get your first Soju!")

# # Problem is that it is very tedious job to copy the same if statement 10 times. We must wrap redundant codes into loops.

# ## while loop executes the body until the associated boolean statement returns True

# while (age < 18): # while age is less than 18,
# 	print("You Cannot Drink Alcohol at age:", age)
# 	age += 1

# # ...computer exits the while loop when age is NOT less than 18, starts reading here
# print("You reached age",age,",Let's get your first Soju!")

# # another example of while loop
# num = 0.0
# while num < 10.0: # This while runs while num < 10
# 	num = num + 0.1 # This line is executed 10.0/0.1 = 100 times.

# print("num is",int(num)) # num is 10

# # Practicing while loop

# # Q1
# # print the following.
# # *
# # **
# # ***
# # ****

# print("instead of this...")
# print("*")
# print("**")
# print("***")
# print("****")

# print("do this!")
# numStar = 1 # first row has 1 star
# while numStar <= 4:
# 	print("*"*numStar)
# 	numStar += 1 # for every print of stars, add 1, since for every row, the number of star increases by 1

# HW: print those shapes below:
# Q2
#   *
#  ***
# *****
#  ***
#   *

# num_space = 2
# num_star = 1
# count = 1


# while count <= 5:
#     print(*num_space+'*'*num_star)
#     if count <= 2:
#         num_space -= 1
#         num_star += 2
#     else:
#         num_space += 1
#         num_star -= 2
#     count += 1

# # Q3
# *******
#  *****
#   ***
# #    *

# num_space = 0
# num_star = 7
# count = 1

# while count <= 4:
#     print(*num_space+'*'*num_star)
#     if count <= 4:

#         num_space += 1
#         num_star -= 2
#     else:
#         num_star += 1

#     count += 1

# Q4
# 1234567
#  12345
#   123
#    1


print("Q4")
layers = 4
n = 7
spaces = 0
while layers > 0:
    digit = 1
    print((" " * (spaces // 2)), end="")
    while digit <= n:
        print(digit, end="")
        digit += 1
    print((" " * (spaces // 2)), end="")  # finished drawing one layer, what's next?
    # 1. skip a line, reduce n by 2, increase space by 2, reduce layer by 1
    print()
    n -= 2
    spaces += 2
    layers -= 1


# Q5
# *@*@*@*   - 7 symbols, odd = *, even = @
#  *@*@*    - 5 symbols, same pattern
#   *@*     - 3 symbols, same pattern
#    *      - 1 symbol, same pattern

layer = 4
num_symbols = 7
i = 1
while layer > 0:
    while i <= num_symbols:  # 1 ~ ? (7,5,3,1)
        if i % 2 == 0:  # if i is even:
            print("@", end="")
        else:
            print("*", end="")
        i += 1  # increment the i
    num_symbols -= 2  # so that in the next layer, num_symbol is 2 less
    layer -= 1  # add one to layer
    i = 1  # initialize the i, so that in the next layer, i start from 1 again.
    print()  # skip a line
