# # if statement
# # - conditional statement: boolean expression to determine whether to run the code or not
# # - body: a block of code to execute when condition statement returns true

# import random

# rand_num = random.randint(1,100) # random integer between [1,100] will be generated
# print("generated random number is",rand_num)

# if rand_num > 50: # if generated random number is larger than 50,
#   print(rand_num, "is larger than 50")
# if rand_num < 80: # if generated random number is less than 80
#   print(rand_num, "is less than 80")

# """if, elif, else"""
# ## elif
# # 1. elif-block MUST HAVE preceding if-block (elif-block must have if-block before used.)
# if rand_num < -50: # this will always return false, why?
#   print("something impossible happened!") # will never see this
# elif rand_num > 10: # this will only execute when above if-condition returned false
#   print(rand_num,"is larger than 10")

# # 2. conditional statement is ONLY TESTED when preceding if block returned false
# if rand_num > 0: # this will always return true
#   print("of course, rand_num's range is between 1 to 100")
# elif rand_num > 1: # will always be ignored since above if-block can't return false
#   print("something impossible happened!")

# # 3. you can have as many elif-blocks you want, but it will only run when preceding elif-block returned false
# if rand_num > 50:
#   print(rand_num,"is larger than 50")
# elif rand_num <= 5:
#   print(rand_num, "is less than or equal to 5")
# elif rand_num <= 10:
#   print(rand_num, "is less than or equal to 10")
# elif rand_num <= 15:
#   print(rand_num, "is less than or equal to 15")
# elif rand_num <= 20:
#   print(rand_num, "is less than or equal to 20")
# elif rand_num <= 25:
#   print(rand_num, "is less than or equal to 25")
# elif rand_num <= 30:
#   print(rand_num, "is less than or equal to 30")
# elif rand_num <= 35:
#   print(rand_num, "is less than or equal to 35")
# elif rand_num <= 40:
#   print(rand_num, "is less than or equal to 40")
# elif rand_num <= 45:
#   print(rand_num, "is less than or equal to 45")
# elif rand_num <= 50:
#   print(rand_num, "is less than or equal to 50")

# # The follow two codes may result in different result
# # 1. many questions with yes/no
# if rand_num > 50:
#   print(rand_num,"is larger than 50")
# if rand_num <= 5:
#   print(rand_num, "is less than or equal to 5")
# if rand_num <= 10:
#   print(rand_num, "is less than or equal to 10")
# if rand_num <= 15:
#   print(rand_num, "is less than or equal to 15")
# if rand_num <= 20:
#   print(rand_num, "is less than or equal to 20")
# if rand_num <= 25:
#   print(rand_num, "is less than or equal to 25")
# if rand_num <= 30:
#   print(rand_num, "is less than or equal to 30")
# if rand_num <= 35:
#   print(rand_num, "is less than or equal to 35")
# if rand_num <= 40:
#   print(rand_num, "is less than or equal to 40")
# if rand_num <= 45:
#   print(rand_num, "is less than or equal to 45")
# if rand_num <= 50:
#   print(rand_num, "is less than or equal to 50")

# # 2. a single multiple-choice question
# if rand_num > 50:
#   print(rand_num,"is larger than 50")
# elif rand_num <= 5:
#   print(rand_num, "is less than or equal to 5")
# elif rand_num <= 10:
#   print(rand_num, "is less than or equal to 10")
# elif rand_num <= 15:
#   print(rand_num, "is less than or equal to 15")
# elif rand_num <= 20:
#   print(rand_num, "is less than or equal to 20")
# elif rand_num <= 25:
#   print(rand_num, "is less than or equal to 25")
# elif rand_num <= 30:
#   print(rand_num, "is less than or equal to 30")
# elif rand_num <= 35:
#   print(rand_num, "is less than or equal to 35")
# elif rand_num <= 40:
#   print(rand_num, "is less than or equal to 40")
# elif rand_num <= 45:
#   print(rand_num, "is less than or equal to 45")
# elif rand_num <= 50:
#   print(rand_num, "is less than or equal to 50")

# ## else
# # 1. else block takes place all ALL if-blocks and elif-blocks returned false
# # 2. must have preceding if-block or elif-block
# # 3. you can decide to have or omit else-block, but you cannot have 2 or more else-blocks
# if rand_num > 50:
#   print(rand_num,"is larger than 50")
# elif rand_num <= 5:
#   print(rand_num, "is less than or equal to 5")
# elif rand_num <= 10:
#   print(rand_num, "is less than or equal to 10")
# elif rand_num <= 15:
#   print(rand_num, "is less than or equal to 15")
# elif rand_num <= 20:
#   print(rand_num, "is less than or equal to 20")
# else:
#   print(rand_num, "is a number between 20 and 50")

# HW (due May 10th, 2023): 
# 1. get user's birthday through keyboard input (1995,9,9)
birthdate = input("Enter Birthdate:(DD/MM/YYYY)")
day = birthdate[0:2] # 0th character & 1st character = day
month = birthdate[3:5] # 3th character & 4st character = month
year = birthdate[6:11] # 6th character ~ 10st character = year

print('string format', day, month, year) # '09' '09' '1995', we must convert to integer

day = int(birthdate[0:2]) # 0th character & 1st character = day
month = int(birthdate[3:5]) # 3th character & 4st character = month
year = int(birthdate[6:11]) # 6th character ~ 10st character = year

print('integer format', day, month, year) # 9 9 1995

# 2. tell their age as of now, (use year to find the age)
# - get today's date? google it.
# - reference: https://www.programiz.com/python-programming/datetime/current-datetime#:~:text=Get%20the%20current%20date%20and,class%20of%20the%20datetime%20module.&text=Here%2C%20we%20have%20used%20datetime,and%20time%20in%20another%20format.

# - logic to find the age
# if birth_date is before today's date, age = today's year - year of birth - 1
# else age = today's year - year of birth
# how to compare two dates?
# reference: https://www.geeksforgeeks.org/comparing-dates-python/

# from datetime import date
# birth_date = date(day,month,year)
# print("input birth date", birth_date) 

# 3. tell their zodiac sign
# - reference: https://www.allure.com/story/zodiac-sign-personality-traits-dates
# - example: Aries (March 21 – April 19)
# - if (month is larger than or equal to 3 and day is larger than or equal to 21)
#       AND
#      (month is less than or equal to 4 and day is less than or equal to 19)




if month == 12:
  sign = 'Sagittarius'if (day < 22) else 'Capricorn'
          
elif month == 1:
  sign = 'Capricorn' if (day < 20) else 'Aquarius'
          
elif month == 2:
  sign = 'Aquarius' if (day < 19) else 'Pisces'
          
elif month == 3:
  sign = 'Pisces' if (day < 21) else 'Aries'
          
elif month == 4:
  sign = 'Aries' if (day < 20) else 'Taurus'
          
elif month == 5:
  sign = 'Taurus' if (day < 21) else 'Gemini'
          
elif month == 6:
  sign = 'Gemini' if (day < 21) else 'Cancer'
          
elif month == 7:
  sign = 'Cancer' if (day < 23) else 'Leo'
          
elif month == 8:
  sign = 'Leo' if (day < 23) else 'Virgo'
          
elif month == 9:
  sign = 'Virgo' if (day < 23) else 'Libra'
      
elif month == 10:
  sign = 'Libra' if (day < 23) else 'Scorpio'
          
elif month == 11:
  sign ='scorpio' if (day < 22) else 'Sagittarius'
          
print(sign)

