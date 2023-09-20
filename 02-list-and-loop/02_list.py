# What is a list?
# list, as the name tell, is a "list of data".

num1 = 10
num2 = 20
num3 = 30
num4 = 40

num_multiple_of_10_v1 = [10, 20, 30, 40]  # group of values
num_multiple_of_10_v2 = [num1, num2, num3, num4]  # group of variables with values
num_multiple_of_10_v3 = [num1, 20, 30, num4]  # group of values & variables

# the three lists above essentially holds the same values
print(num_multiple_of_10_v1)
print(num_multiple_of_10_v2)
print(num_multiple_of_10_v3)

# Key facts about list
# 1. List can be empty
empty_list = []  # list with no elements (items) inside

# 2. List can store values of different types
random_list = ["ryan", "conner", 10, 2.3, False]
print(random_list)

# 3. Items in the list can be accessed by scripting
# SUM(1st item in the list "num_multiple_of_10_v1", and 3rd item in the list "num_multiple_of_10_v1")
print(num_multiple_of_10_v1[0] + num_multiple_of_10_v1[2])  # result: 10 + 30 = 40

# 4. total number of items in the list can be found easily
print(
    "total number of items in num_multiple_of_10_v1 is:", len(num_multiple_of_10_v1)
)  # total number of items in the list "num_multiple_of_10_v1" = 4

# 5. sort ASC/DESC, add, remove, replace item
num_multiple_of_10_v4 = [40, 20, 50, 10, 80, 60, 30]
num_multiple_of_10_v4.sort()  # sort the item asceding order
print("sorted ascending order:", num_multiple_of_10_v4)

num_multiple_of_10_v4 = [40, 20, 50, 10, 80, 60, 30]
num_multiple_of_10_v4.sort(reverse=True)  # sort the item descending order
print("sorted descending order:", num_multiple_of_10_v4)

num_multiple_of_10_v4 = [40, 20, 50, 10, 80, 60, 30]
num_multiple_of_10_v4.append(100)  # add new item
print("added 100 to the list:", num_multiple_of_10_v4)

num_multiple_of_10_v4 = [40, 20, 50, 10, 80, 60, 30]
num_multiple_of_10_v4.remove(80)  # remove existing item
print("removed 80 from the list:", num_multiple_of_10_v4)

num_multiple_of_10_v4 = [40, 20, 50, 10, 80, 60, 30]
index_of_20 = num_multiple_of_10_v4.index(20)  # get nth position of item
print("get the index of item=20:", index_of_20)

num_multiple_of_10_v4 = [40, 20, 50, 10, 80, 60, 30]
num_multiple_of_10_v4.insert(3, 120)  # insert 120 at index=3 (4th)
print("inserted 120 at index = 3 (4th)", num_multiple_of_10_v4)

num_multiple_of_10_v4 = [40, 20, 50, 10, 80, 60, 30]
last_item1 = num_multiple_of_10_v4[len(num_multiple_of_10_v4) - 1]  # get last item method 1
last_item2 = num_multiple_of_10_v4[-1]  # like walking the list backward (smarter way)
print(
    "The two variables, last_item1 and last_item2 must be the same",
    last_item1,
    last_item2,
)


# ... for more list functions, please visit https://www.programiz.com/python-programming/methods/list

## HW: due Sep 13, 2023
L1 = ["a", "b", "c", "d", "e", "f"]

# 1. print "abcdef" using while loop
i = 0  # variable which indicates the index number of item

# while i is less than len(L1)(=6)....
while i < len(L1):
    print(
        "should print 'abcdef'", L1[i], end=""
    )  # prints 'a' -> prints 'b' -> prints 'c' -> ...
    i += 1  # i increases from 0 to len(L1)(= 6)

# Q1: print "ace" using while loop (MUST!)
i = 0
while i < len(L1):
    print(L1[i], end="")
    i += 2
print()
# Q2: print "bdf" using while loop (MUST!)
i = 1
while i < len(L1):
    print(L1[i], end="")
    i += 2
print()
# Q3: print "fedcba" using while loop (MUST!)
i = 5
while i < len(L1) and i >= 0:
    print(L1[i], end="")
    i -= 1
print()
    
# Q4: print "afbecd" using while loop (MUST!)
# Solution 1: Good, but not robust (not always true depending on the length of L1)
L1 = ["a", "b", "c", "d", "e", "f"]

i = 0
j = -1
while i < 3 and j > -4:
    print(L1[i] + L1[j], end="")
    i += 1
    j -= 1
print()

# Solution 2: more "robust" (so-called good boiler plate, reusable in many cases)
L1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

i = 0 # always return the first element
j = -1 # always return last element
# plan:
# first loop: "af" i = 0, j = -1
# second loop: "be" i = 1, j = -2
# third loop: "cd" i = 2, j = -3

# total repeat needed: 3
# since total number of elements in the L1 is 6, you can just let the loop to go "half-way", but i goes forward, and j goes backward
repeat = 0
while repeat < len(L1)/2:
    print(L1[i] + L1[j], end="")
    i += 1
    j -= 1
    repeat += 1