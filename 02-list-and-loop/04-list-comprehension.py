# 1. List Part II

# This section handles more advanced level of list manipulations from 02-list-and-loop/02_list.py

# Recap: List Basics
nums1 = [1, 2, 3]
nums2 = [4, 5, 6, 7]

print(len(nums1))  # prints the length of the list nums1, 3
print(len(nums2))  # prints the length of the list nums2, 4

print(nums1[2])  # prints the 3rd element of the list nums1, 3
print(nums2[1])  # prints the 2nd element of the list nums1, 5

# ...and all other basic features that list module of python provides (refer to 02-list-and-loop/02_list.py)
# - sort
# - append
# - remove
# - index
# - insert

#############################################################################################################

# 1.1 List concatenation / repetition (sticking two lists together / repeating the list)
nums = nums1 + nums2
# returns [1,2,3,4,5,6,7,8]
print("returns the concatenated list of nums1 and nums2:", nums)
print("returns a list with nums2 repeated 5 times", nums2 * 5)

# 1.2 Casting (converting)
# 1.2.1 Casting list to string
print("casts the nums1 to string", str(nums1))
print(
    "casts nums1 to string, then concatenate string '...is the str format of nums1':\n",
    str(nums1) + "...is the str format of nums1",
)

# 1.2.2 Casting string to list
target_string = "RyanKim"
print("this is the target:", target_string)
print("this casts the target_string to list format:", list(target_string))
target_string_li = list(target_string)
print("this is the 4th element of the target_string_li:", target_string_li[3])
print(
    "of course...to find the 4th element of any string, you don't need to cast to list:",
    target_string[3],
)

# 1.3 List Comprehension
word = "RYAN"

# How would you generate a list that has ["RRRRR", "YYYYY", "AAAAA", "NNNNN"]?
# logic:
# - tear out every letters in the variable "word",
# - repeat each 5 times,
# - then return as a list ordered according to the order of letters in "RYAN"

li = []
for letter in word:
    li.append(letter * 5)
print("This gets us what we want:", li)

### But is this an efficient way of solving this problem? let's time it. ###
import time

# start timer
start = time.time()  # timestamp starting to run code

li = []
for letter in word:
    li.append(letter * 5)

# end the the timer
end = time.time()  # timestamp code finished running
time_taken = end - start  # seconds
time_taken_in_ns = time_taken * 10**9  # in nanoseconds

print(
    "report: the above code of generating ['RRRRR', 'YYYYY', 'AAAAA', 'NNNNN'] with for loop took:",
    time_taken_in_ns,
    "ns",
)

# can we improve this? use list comprehension

# start timer
start = time.time()  # timestamp starting to run code

# this basically serves the same purpose
# syntax
# <variable> = [<code with iterator> for <iterator> in <list>]
li = [letter * 5 for letter in word]

# end the the timer
end = time.time()  # timestamp code finished running
time_taken = end - start  # seconds
time_taken_in_ns = time_taken * 10**9  # in nanoseconds

print(
    "report: the above code of generating ['RRRRR', 'YYYYY', 'AAAAA', 'NNNNN'] with list comprehension took:",
    time_taken_in_ns,
    "ns",
)

# list comprehension drillu
foods = ["brger", "fish", "carrot", "pizza", "olives"]
preferences = ["burger", "pizza"]

# How would you generate a list that has True if the given food in list foods is one of ryan's favorite food?
# expected result: [True, False, False, True, False], since only the "burger" (index = 0) and "pizza" (index = 3) are listed in preferences

# solution 1: with for loop
are_favorites = []
for food in foods:
    if food in preferences:
        are_favorites.append(True)
    else:
        are_favorites.append(False)

# solution 2: improved version of solution 1
are_favorites = []
for food in foods:
    are_favorites.append(food in preferences)

# solution 3: with list comprehension
are_favorites = [food in preferences for food in foods]

for i in range(len(foods)):
    # if the ith element in are_favorites is True, print "it is favorite food"
    if are_favorites[i]:
        print(foods[i], "is Ryan's favorite food.")
    # else, print "it is not a favorite food"
    else:
        print(foods[i], "is NOT Ryan's favorite food.")

# so what's good about list comprehension over list?
# 1. more efficient, shorter code.
# 2. more readable

# what's different between list comprehension vs. for loop?
# for loop: just repeating codes, whatever code you have written in the for loop body.
#           if your goal is to repeat the code, use for loop.
# list comprehension: "returns a new list" with a certain rules being applied to each elements you are comprehending the list from.
#                     if you need a new list generated, please use list comprehension.
