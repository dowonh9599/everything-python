# 3. for loop

# 3.1 "range" function
# the range() function is used to generate a sequence of numbers (1,2,3,4,5,6,....).
# range(start, end), where start is inclusive, end is exclusive
range(10) # this is essentially 0 ~ 9
range(2,6) # this is essentially 2 ~ 5
print(range(10,20))

# 3.2 "in" function
# boolean Function which tests where value at LHS is in the list at RHS
alphabets = ["a", "b", "c", "d", "e", "f"]
print("testing whether a is in the list 'alphabets'", "a" in alphabets) # This should return true
print("testing whether g is in the list 'alphabets'", "g" in alphabets) # This should return false

# 3.3 Getting Started with for loop
item_list = ['MacBook', 'Phone', 'Mask', 'Shoes', 'Charger', 'Paper']


# This is essentially the same thing with
# print("Macbook")
# print("Phone")
# print("Mask")
# print("Shoes")
# print("Charger")
# print("Paper")
for item in item_list:
	print(item) # print(item) is repeated for every jump from one item to next in item_list
	
# Or we can do:


# This is essentially the same thing with
# print(item_list[0]) => "MacBook"
# print(item_list[1]) => "Phone"
# print(item_list[2]) => "Mask"
# print(item_list[3]) => "Shoes"
# print(item_list[4]) => "Charger"
# print(item_list[5]) => "Paper"
for i in range(len(item_list)): # = for i in range(6) = for i in (0,1,2,3,4,5)
	print(item_list[i])

# Quick Practice 1: Fibonacci Sequence
# using for loop, and range function, print: 0 1 4 9 16 25 36 49 64 81
for i in range(10):
	print (i ** 2,end=" ")
print()

# Quick Practice 2: Find cumulative sum
num_list = [1,9,6,20,12,40,32,41] # cumulative sum = 161
# using for loop, but not using range function, print the cumulative sum of num_list

sum = 0

for i in num_list:
	sum += i
print(sum)

# 3.4 Loop Control
# 3.4.1 break statement
print("break statement usage:")
for i in range(10):
	if i == 6:
		break # complete stop here
	print(i, end=" ")
print()

# 3.4.2 continue statement
print("continue statement usage:")
for i in range(10):
	if i == 6:
		continue # do not run code below this, resume from next iteration
	print(i, end=" ")
print()

# 3.4.3 pass statement
print("pass statement usage:")
for i in range(10):
	if i == 6:
		pass # do nothing
	print(i, end=" ")

# Loop control practice
