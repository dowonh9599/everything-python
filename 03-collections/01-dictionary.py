# 1. Dictionary
# @Dictionary?
# - most flexible built-in data types in Python
# - unordered collection
# - key-value paired data structure

# 3.1 Dictionary Basics
# 3.1.1 Creating, modifying Dictionary
D = {}  # empty dictionary

# key: unique index to return paired value (double play, shutout, Mendoza Line, bullpen)
# value: data
baseball_terms = {
    "double play": "A double play occurs when two offensive players are ruled out within the same play.",
    "shutout": "a shutout refers to the act by which a single pitcher pitches a complete game and does not allow the opposing team to score a run.",
    "Mendoza Line": ".200 batting average",
    "bullpen": "a group of relief pitchers as a whole, whose job is to replace starting pitchers and finish games",
}

# prints the value paired to the key "double play"
print("double play means:", baseball_terms["double play"])

# can add more key-value pair to dictionary at anytime (mutable)
baseball_terms[
    "inning"
] = "An inning in which a pitcher faces only three batters and none safely reaches a base."

# check the whole dictionary "baseball_terms" to check if the word "inning" is added
print(baseball_terms)  # possible, but not recommended.
print()
print()
# how to print the dictionary more readable?
for k, v in baseball_terms.items():
    print(k, v)

kendo_terms = {
    "shinai": "bamboo sword used for practice and competition in Kendo",
    "bogu": "protective equipment worn by practitioners during practice and competition.",
    "dojo": "The training hall or practice space where Kendo is practiced.",
    "men": "A target area in Kendo corresponding to the head or face.",
    "kote": "A target area in Kendo corresponding to the wrist or forearm.",
    "do": "A target area in Kendo corresponding to the torso or trunk.",
}

# strucuture:
# sports_terms
# L baseball
#   L double play
#   L shutout
#   L Mendoza Line
#   L bullpen
# L kendo
#   L shinai
#   L bogu
#   L dojo
#   L men
#   L kote
#   L do
sports_terms = {"baseball": baseball_terms, "kendo": kendo_terms}

# print the definition of "kote" in "kendo"
print("the definition of kote in kendo is:", sports_terms["kendo"]["kote"])

# 3.1.2 Key, values in Dictionary
# 1. keys()
print("all keys in baseball_terms", baseball_terms.keys())
print("all keys in kendo_terms", kendo_terms.keys())
print("all keys in sports_terms", sports_terms.keys())  # ??

# 2. values()
print("all values in baseball_terms", baseball_terms.values())
print("all values in kendo_terms", kendo_terms.values())

# 3. items() => list of (key, value)
print("items in kendo_terms", kendo_terms.items())

# 3.1.3 various functions with Dictionary
# Contrstructing Dictionary
D1 = {}
D2 = {"name": "Ryan", "age": 13}  # create dictionary with two items, 'name' and 'age'
D3 = {
    "student_1": {"name": "Ryan", "age": 13}
}  # nesting dictionary in another dictionary
D4 = dict(
    name="Ryan", age=13
)  # another way of contructing dictionary, output the same thing with D2

keys = ["name", "age", "school", "favorite_sports"]
values = ["Ryan", 13, "HKIS", "baseball"]
D5 = dict(zip(keys, values))  # also output the same dictionary as D4, D2

# indexing Dictionary
D5["name"]  # Ryan
D5.get("name")  # Rytan

# adding items to Dictionary
D5["skill"] = "Python"
D5["num_classes"] = 10
D5["favorite_subject"] = ["Math", "PE", "Band"]
print("after adding three more items...", D5)
## using list comprehension
D5 = {"perfect_squares": x**2 for x in range(10)}
# equivalent to D5 = {"perfect_squares": [1,4,9,16, ... , 100]}

# removing items from Dictionary
D5.pop("skill")
print("after deleting skill...", D5)
del D5["school"]
print("after deleting school...", D5)
