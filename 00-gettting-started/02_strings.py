last_name="Kim"
first_name="Ryan"

# length function: find the number of elements in list
fruits = ["Apple", "Banana", "Orange", "Kiwi"] # total number of elements in this list is 4
print("Total number of elements in the list called 'fruits' is", len(fruits))

# How to use len() with string
# "Ryan" => ["R", "y", "a", "n"]
print("Total number of characters in the word 'Ryan' is", len("Ryan"))
print("We can also just pass the variable that has string in it. The string in the variable 'last_name' has", len(last_name), 'letters')

# Features of String
## 1. String is scriptable!
## e.g. "Ryan" => ["R", "y", "a", "n"]
print("first character (index = 0) of 'Ryan' is", "Ryan"[0]) # first character (index = 0) of "Ryan" is "R"
print("second character (index = 1) of 'Ryan' is", first_name[1]) # second character (index = 1) of "Ryan" is "y"
print("third character (index = 2) of 'Ryan' is", first_name[2]) # third character (index = 2) of "Ryan" is "a"
print("fourth character (index = 3) of 'Ryan' is", first_name[3]) # fourth character (index = 3) of "Ryan" is "n"

# 2. Strings can concatenate (stick together)
print("My name is", first_name + " " + last_name) # "Ryan" + " " + "Kim" = "Ryan Kim"

# 3. Strings can iterate (repeat)
print((first_name) * 5)

# 4. String is sliceable
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

## Slicing 1: slicing out a substring (part of string) from index i to j:
### Formula: alphabets[i:(j+1)]
#### -> This slices the string from i to j

## For example, "ABCDE" is a substring of string "alphabets" from i=0 to j=4
print(alphabets[0:5]) # this is equivalent to alphabets[0:(4+1)] -> This slices the string from i=0 to j=4 -> returns "ABCDE"
## Similarly, "CDEFGHIJKLM" is a substring of string "alphabets" from i=2 to j=12
## To slice the alphabets from i=2 to j=12 -> alphabets[i=2:((j=12) + 1)]
print(alphabets[2:13]) # This returns "CDEFGHIJKLM"



## Slicing 2: slicing from beginning to j, slicing from i to end:
### Formula: alphabets[:(j+1)] # if slicing starts from beginning, you can leave it empty.
### Formula: alphabets[i:] # if slicing finishes at the end, you can leave it empty.

## For example, we've seen:
print("will return ABCDE", alphabets[0:5]) # This returns "ABCDE"
print("will return ABCDE too", alphabets[:5]) # This is also equivelent since it starts from beginning

## Similarly, to pull out "XYZ," last three letters in "alphabets":
print("will return XYZ", alphabets[23:25]) # This returns "XYZ"
print("will return XYZ too", alphabets[23:]) # This is also equivelent since it ends at the last letter of alphabets


## Slicing 3: slicing from index i to j, but for every n number of steps.
### Formula: alphabets[i:(j+1):n] # This slices the string from i to j for n number of steps.

## For example, to pull out "BDFH" which are those of (i, i+2, (i+2)+2. ((i+2)+2)+2))
alphabets[1:8:2] # This returns "BDFH", by pulling out i=1,3,5,7.

## Similarly, to pull out "BDFH" which are every 3rd letter of alphabets[1:15]
alphabets[1:15:3] # This returns "BEHKN", by pulling out i = 1,4,7,10,13

## Slicing 4: slicing in reverse manner from index j to i
### Formula: alphabets[i:(j-1):n] # This slices the string from j to i in reverse direction.

## Remember that the index of last letter is -1
alphabets[-1] # This returns "Z"

## Let's say we pick up the substring upto "X" from "Z" in reverse direction,
alphabets[-4] # This is the 5th letter from the back, which is "W"

# The key thing is, we set the step to be -1 in order to run reverse direction.
# This means,
# • i = -1 
# • j = -4
# • n = -1

# Summing up,
alphabets[-1:-5:-1] # This returns "ZYXW"
alphabets[-1:-5:-2] # This returns "ZX"
alphabets[25:21:-1] # This also returns "ZYXW", is equivalent to above.

# Homework
# 1. Try to slice "HIJKL" (Slicing #1)
# 2. Try to slice "UVWXYZ" (Slicing #2)
# 3. Try to slice "GIKLN" (Slicing #3)
# 2. Try to slice "SRQPO" (Slicing #4)