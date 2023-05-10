# if statement
# - conditional statement: boolean expression to determine whether to run the code or not
# - body: a block of code to execute when condition statement returns true

import random

rand_num = random.randint(1,100) # random integer between [1,100] will be generated
print("generated random number is",rand_num)

if rand_num > 50: # if generated random number is larger than 50,
  print(rand_num, "is larger than 50")
if rand_num < 80: # if generated random number is less than 80
  print(rand_num, "is less than 80")

"""if, elif, else"""
## elif
# 1. elif-block MUST HAVE preceding if-block (elif-block must have if-block before used.)
if rand_num < -50: # this will always return false, why?
  print("something impossible happened!") # will never see this
elif rand_num > 10: # this will only execute when above if-condition returned false
  print(rand_num,"is larger than 10")

# 2. conditional statement is ONLY TESTED when preceding if block returned false
if rand_num > 0: # this will always return true
  print("of course, rand_num's range is between 1 to 100")
elif rand_num > 1: # will always be ignored since above if-block can't return false
  print("something impossible happened!")

# 3. you can have as many elif-blocks you want, but it will only run when preceding elif-block returned false
if rand_num > 50:
  print(rand_num,"is larger than 50")
elif rand_num <= 5:
  print(rand_num, "is less than or equal to 5")
elif rand_num <= 10:
  print(rand_num, "is less than or equal to 10")
elif rand_num <= 15:
  print(rand_num, "is less than or equal to 15")
elif rand_num <= 20:
  print(rand_num, "is less than or equal to 20")
elif rand_num <= 25:
  print(rand_num, "is less than or equal to 25")
elif rand_num <= 30:
  print(rand_num, "is less than or equal to 30")
elif rand_num <= 35:
  print(rand_num, "is less than or equal to 35")
elif rand_num <= 40:
  print(rand_num, "is less than or equal to 40")
elif rand_num <= 45:
  print(rand_num, "is less than or equal to 45")
elif rand_num <= 50:
  print(rand_num, "is less than or equal to 50")

# The follow two codes may result in different result
# 1. many questions with yes/no
if rand_num > 50:
  print(rand_num,"is larger than 50")
if rand_num <= 5:
  print(rand_num, "is less than or equal to 5")
if rand_num <= 10:
  print(rand_num, "is less than or equal to 10")
if rand_num <= 15:
  print(rand_num, "is less than or equal to 15")
if rand_num <= 20:
  print(rand_num, "is less than or equal to 20")
if rand_num <= 25:
  print(rand_num, "is less than or equal to 25")
if rand_num <= 30:
  print(rand_num, "is less than or equal to 30")
if rand_num <= 35:
  print(rand_num, "is less than or equal to 35")
if rand_num <= 40:
  print(rand_num, "is less than or equal to 40")
if rand_num <= 45:
  print(rand_num, "is less than or equal to 45")
if rand_num <= 50:
  print(rand_num, "is less than or equal to 50")

# 2. a single multiple-choice question
if rand_num > 50:
  print(rand_num,"is larger than 50")
elif rand_num <= 5:
  print(rand_num, "is less than or equal to 5")
elif rand_num <= 10:
  print(rand_num, "is less than or equal to 10")
elif rand_num <= 15:
  print(rand_num, "is less than or equal to 15")
elif rand_num <= 20:
  print(rand_num, "is less than or equal to 20")
elif rand_num <= 25:
  print(rand_num, "is less than or equal to 25")
elif rand_num <= 30:
  print(rand_num, "is less than or equal to 30")
elif rand_num <= 35:
  print(rand_num, "is less than or equal to 35")
elif rand_num <= 40:
  print(rand_num, "is less than or equal to 40")
elif rand_num <= 45:
  print(rand_num, "is less than or equal to 45")
elif rand_num <= 50:
  print(rand_num, "is less than or equal to 50")

## else
# 1. else block takes place all ALL if-blocks and elif-blocks returned false
# 2. must have preceding if-block or elif-block
# 3. you can decide to have or omit else-block, but you cannot have 2 or more else-blocks
if rand_num > 50:
  print(rand_num,"is larger than 50")
elif rand_num <= 5:
  print(rand_num, "is less than or equal to 5")
elif rand_num <= 10:
  print(rand_num, "is less than or equal to 10")
elif rand_num <= 15:
  print(rand_num, "is less than or equal to 15")
elif rand_num <= 20:
  print(rand_num, "is less than or equal to 20")
else:
  print(rand_num, "is a number between 20 and 50")

# HW (due May 10th, 2023): 
# 1. get user's birthday through keyboard input (1995,9,9)
# 2. tell their age as of now, (use year to find the age)
# - get today's date? google it.
# - reference: https://www.programiz.com/python-programming/datetime/current-datetime#:~:text=Get%20the%20current%20date%20and,class%20of%20the%20datetime%20module.&text=Here%2C%20we%20have%20used%20datetime,and%20time%20in%20another%20format.
# 3. tell their zodiac sign
# - reference: https://www.allure.com/story/zodiac-sign-personality-traits-dates
# - example: Aries (March 21 – April 19)
# - if (month is larger than or equal to 3 and day is larger than or equal to 21)
#       AND
#      (month is less than or equal to 4 and day is less than or equal to 19)
# - repeat for all other signs