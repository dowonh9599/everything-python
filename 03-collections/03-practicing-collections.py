"""
1. List Operations: Create a list of 5 elements and perform the following operations:
- Append a new element to the list.
- Insert an element at a specific index.
- Remove an element.
- Sort the list.
- Reverse the list.
"""
L1 = [
    "b",
    "a",
    "d",
    "e",
    "c",
]
print("appending f...", L1.append("f"))
print("inserting z at index 0...", L1.insert(0, "z"))
print("removing e from L1...", L1.remove("e"))
print("sort by ascending (alphabetical) order...", L1.sort())
print("reversing the order of L1", L1.reverse())


"""
2. Dictionary Operations: Create a dictionary with 3 key-value pairs and perform the following operations:
- Add a new key-value pair to the dictionary.
- Update the value of an existing key.
- Remove a key-value pair from the dictionary.
- Check if a key exists in the dictionary.
- Print all keys.
- Print all values.
"""
# YOUR CODE FOR Q2 HERE

"""
3. Tuple Operations: Create a tuple of 4 elements and perform the following operations:
- Try to modify an existing element of the tuple (you should get an error).
- Convert the tuple to a list.
- Add an element to the list.
- Convert the list back to a tuple.
"""
# YOUR CODE FOR Q3 HERE

"""
4. List to Dictionary: Create a list of tuples, where each tuple contains a key and a value. Convert this list of tuples into a dictionary.
"""
# YOUR CODE FOR Q4 HERE

"""
5. Dictionary to List: Create a dictionary and convert it into a list of tuples, where each tuple is a key-value pair from the dictionary.
"""
# YOUR CODE FOR Q5 HERE

"""
6. Nested Data Structures: Create a list of dictionaries. Each dictionary should contain a product and its price. Find the product with the highest price.
"""
# YOUR CODE FOR Q6 HERE


### CHALLENGE ###
# C1. Word Count in a String:
# Write a function to count the occurrence of each word in a given string. The function should return a dictionary where the keys are the unique words and the values are the word counts.
def word_count(string):
    # Your code here
    pass


# C2. Invert a Dictionary:
# Write a function that inverts a dictionary. The keys should become values and the values should become keys. Assume all values of the original dictionary are unique.


def invert_dict(d):
    # Your code here
    pass


# C3. Merge Two Dictionaries:
# Write a function that merges two dictionaries. If there is a key collision, prefer the value from the second dictionary.


def merge_dicts(d1, d2):
    # Your code here
    pass


# C4. Dictionary to List of Tuples:
# Write a function that converts a dictionary into a list of tuples, where each tuple is a key-value pair.


def dict_to_tuples(d):
    # Your code here
    pass


# C5. Group Anagrams:
# Given a list of strings, group anagrams together. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
def group_anagrams(words):
    # Your code here
    pass


# C6. Least Frequent Element:
# Given a list, find the element that appears least frequently. Return a tuple containing the element and its count. If there's a tie, return any of them.
def least_frequent(lst):
    # Your code here
    pass


# test
word_count("pen pineapple pen pen apple pen")

baseball_terms = {
    "double play": "A double play occurs when two offensive players are ruled out within the same play.",
    "shutout": "a shutout refers to the act by which a single pitcher pitches a complete game and does not allow the opposing team to score a run.",
    "Mendoza Line": ".200 batting average",
    "bullpen": "a group of relief pitchers as a whole, whose job is to replace starting pitchers and finish games",
}
kendo_terms = {
    "shinai": "bamboo sword used for practice and competition in Kendo",
    "bogu": "protective equipment worn by practitioners during practice and competition.",
    "dojo": "The training hall or practice space where Kendo is practiced.",
    "men": "A target area in Kendo corresponding to the head or face.",
    "kote": "A target area in Kendo corresponding to the wrist or forearm.",
    "do": "A target area in Kendo corresponding to the torso or trunk.",
}

invert_dict(baseball_terms)
merge_dicts(baseball_terms, kendo_terms)


keys = ["name", "age", "school", "favorite_sports"]
values = ["Ryan", 13, "HKIS", "baseball"]
D2 = dict(zip(keys, values))
dict_to_tuples(D2)
group_anagrams(["pen", "pineapple", "apple"])

lst = [
    "apple",
    "banana",
    "cherry",
    "apple",
    "cherry",
    "cherry",
    "dragonfruit",
    "mango",
    "apple",
    "banana",
]
least_frequent()
