# Logical Operators
11 > 7 # '>' larger than
11 >= 11 # '>=' larger than or equal to
11 < 11 # '<=' less than
11 <= 11 # '<=' less than or equal to

11 == 11 # '==' equal to
10 != 11 # '!=' not equal to

value = 10
value > 0 and value < 100 # 'and' => left and right condition must be true to result true, else false
value > 0 or value < 5 # 'or' => at least either the left or the right must be true to result true, else false
not value == 20 # 'not' => negates the result of condition

# examples
not (5 > 7) # not (False) = True

a = True
b = False
c = True
d = False

a and c # True and True = True
a and b # True and False = False
b and c # False and True = False
b and d # False and False = False

a or c # True or True = True
a or b # True or False = True
b or c # False or True = True
b or d # False or False = False

# Example: Entering the male's restroom at HKIS needs two condition:
# 1. one has to be male
# 2. one has to be part of HKIS Community

is_male = input("Are you a male? (y/n)")
if is_male == "y":
	is_male = True
else:
	is_male = False

is_HKIS = input("Are you part of the HKIS Community (y/n)")
if is_HKIS == "y":
	is_HKIS = True
else:
	is_HKIS = False

entering_male_restroom_allowed = is_male and is_HKIS

# Letter Grade Calculator (must use logical operator!!)
# 1. ask for user's mark (0-100)
# 2. tell the letter grade
### How does letter grade work
# 97-100 = A+
# 94-96 = A
# 90-93 = A-
# 87-89 = B+
# 84-86 = B
# 80-83 = B-
# 77-79 = C+
# 74-76 = C
# 70-73 = C-
# 60-69 = D
# below 60 = F