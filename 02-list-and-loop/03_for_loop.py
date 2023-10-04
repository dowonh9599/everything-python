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
# Write a prime number detector function
# What is prime number?
# - divisble by 1 and itself only

# Big Hint: when determining prime number, "no need to test further" if there's at least 1 number that results in num % i == 0
# e.g. if num = 10, while testing i = [2,9], "no need to test [6,9]"" since at i = 5, 10 % 5 = 0, meaning we already know 10 is not a prime number since it is divisible by 5.
# by saying "no need to test", it is implies "break" statement must be used to stop the loop.
def is_prime(num: int) -> bool:
	is_prime_num = False
	print("input:",num)

	if num < 2:
		pass
	
	for i in range(2, num): # this way, you can prevent the num itself being tested since range excludes "num" itself
		# e.g. num = 10, then num is tested with i = [2,9]
		# the last test will be 10%9 = 1
		# this way, no matter what number is passed to num, it will always end up with (n) % (n-1) = 1 -> and is_prime_num is overriden to True.
		if num % i == 0:
				is_prime_num = False
		else:
				is_prime_num = True

	# ===TO HERE===
	return is_prime_num

print("10 is a prime number:", is_prime(10)) # should return False
print("13 is a prime number:", is_prime(13)) # should return True
print("20000 is a prime number:", is_prime(20000)) # should return False
print("59595 is a prime number:", is_prime(59595)) # should return False
print("10091 is a prime number:",is_prime(10091)) # should return True
print("24799 is a prime number:",is_prime(24799)) # should return True
print("68927 is a prime number:",is_prime(68927)) # should return True
print("92479 is a prime number:",is_prime(92479)) # should return True
print("92479 is a prime number:",is_prime(92450)) # should return True
