# 3.2 Tuples

# last collection type to learn in python
# @Tuple?
# They work exactly like lists, except that tuples can’t be changed in place (they’re immutable)
# usually written as a series of items in parentheses, not square brackets.

# 3.2.1 Tuple in a Nutshell
T = ()  # empty tuple
T2 = (
    "apple",
    "banana",
    "orange",
    "mango",
    "kiwi",
    "orange",
    "orange",
)  # tuple with 5 fruits.
T3 = ("pineapple", "grape", "Strawberry", "Watermelon", "Lemon")

# tuple functions
print("index value of kiwi in Tuple T2", T2.index("kiwi"))
print("total count of 'orange' in Tuple T2", T2.count("orange"))
print("output the length of T3, which is 5", len(T3))

# concatenation, iteration
T4 = T2 + T3
print("sticking two tuples together", T4)
print("iteraing tuples", T3 * 5)

# indexing and slicing
print(T2[1])  # 2nd item in T2 tuple, i.e. banana
print("slicing Tuple", T4[1:3])

# casting
T_in_L = list(T2)

# TypeError: 'tuple' object does not support item assignment
T["Hello"] = "world!"
print(T)
