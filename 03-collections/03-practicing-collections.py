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

dictionary = {"a": "1", "b": "2", "c": "3"}
dictionary["d"] = "4"
dictionary["b"] = "5"
del dictionary["c"]
if "a" in dictionary:
    print("yes")
print("all values in dictionary", dictionary.values())
print("all keys in dictionary", dictionary.keys())

"""
3. Tuple Operations: Create a tuple of 4 elements and perform the following operations:
- Try to modify an existing element of the tuple (you should get an error).
- Convert the tuple to a list.
- Add an element to the list.
- Convert the list back to a tuple.
"""
T1 = (1, 2, 3, 4)
L1 = list(T1)
L1.append(5)
T1 = tuple(L1)
print(T1)
"""
4. List to Dictionary: Create a list of tuples, where each tuple contains a key and a value. Convert this list of tuples into a dictionary.
"""
# YOUR CODE FOR Q4 HERE
print("4. list of tuple to dict")
tuple_list = [("a", 1), ("b", 2), ("c", 3)]
tuple_list_to_dict = dict(tuple_list)  # converting list of tuples to dict
print("convert result:", tuple_list_to_dict)
print("test, should print 2:", tuple_list_to_dict["b"])

"""
5. Dictionary to List: Create a dictionary and convert it into a list of tuples, where each tuple is a key-value pair from the dictionary.
"""
# YOUR CODE FOR Q5 HERE
print("5. dict to list of tuple")
dictionary = {"a": "1", "b": "2", "c": "3"}
print(".items()", dictionary.items())
dict_to_tuple = list(dictionary.items())
print("convert result", dict_to_tuple)

"""
6. Nested Data Structures: Create a list of dictionaries. Each dictionary should contain a product and its price. Find the product with the highest price.
"""
# YOUR CODE FOR Q6 HERE
print("6. finding max in the list of dictionary")
groceries = [
    {"product": "apple", "price": 10},
    {"product": "banana", "price": 15},
    {"product": "orange", "price": 20},
]
# 1. find the highest price
most_expensive_fruit = max(groceries, key=lambda x: x["price"])
print("most expensive fruit found:", most_expensive_fruit)


### CHALLENGE ###
# C1. Word Count in a String:
# Write a function to count the occurrence of each word in a given string. The function should return a dictionary where the keys are the unique words and the values are the word counts.
def word_count(words: str):
    # Your code here
    word_count = {}

    # strategy
    # 1. split the string by space: "Hello world Hello" -> ["Hello", "world", "Hello"]
    print("current", words)
    words_split = words.split()
    print("after split", words_split)

    # Example: ['Hello', 'world', 'Hello']
    for w in words_split:
        # if word_count[w] is None, meaning doesn't exist, add key-value pair w: 1 (first occurrence found)
        if word_count.get(w) == None:
            word_count[w] = 1
        # else, get how many times the word's occurrence has been recorded, then add 1
        else:
            word_count[w] = word_count.get(w) + 1
    return word_count


# Test case 1
test_string_1 = "Hello world Hello"
print(word_count(test_string_1))  # Expected output: {'hello': 2, 'world': 1}


# Test case 2
test_string_2 = "The quick brown fox jumps over the lazy dog"
print(
    word_count(test_string_2)
)  # Expected output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

# Test case 3
test_string_3 = "A man a plan a canal Panama"
print(
    word_count(test_string_3)
)  # Expected output: {'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1}

# C2. Invert a Dictionary:
# Write a function that inverts a dictionary. The keys should become values and the values should become keys. Assume all values of the original dictionary are unique.

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


def invert_dict(d):
    # Your code here
    inv_map = {v: k for k, v in d.items()}
    return inv_map


# Test case for invert_dict
# Expected outcome: The definitions become keys, and the terms become values.
print(invert_dict(baseball_terms))


# C3. Merge Two Dictionaries:
# Write a function that merges two dictionaries. If there is a key collision, prefer the value from the second dictionary.


def merge_dicts(d1, d2):
    # Your code here
    pass


# Test case for merge_dicts
# Expected outcome: A new dictionary with all keys and values from both, with the second dictionary's values overriding any duplicates from the first.
print(merge_dicts(baseball_terms, kendo_terms))

# C4. Dictionary to List of Tuples:
# Write a function that converts a dictionary into a list of tuples, where each tuple is a key-value pair.

keys = ["name", "age", "school", "favorite_sports"]
values = ["Ryan", 13, "HKIS", "baseball"]
D2 = dict(zip(keys, values))


def dict_to_tuples(d):
    # Your code here
    pass


# Test case for dict_to_tuples
# Expected outcome: [('name', 'Ryan'), ('age', 13), ('school', 'HKIS'), ('favorite_sports', 'baseball')]
print(dict_to_tuples(D2))


# C5. Group Anagrams:
# Given a list of strings, group anagrams together. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

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


def group_anagrams(words):
    # Your code here
    pass


# Additional test case for group_anagrams
# Expected outcome: [['bat'], ['tab', 'abt'], ['rat', 'tar', 'art'], ['can'], ['act', 'cat']]
# Explanation: 'bat' has no anagrams in the list, 'tab', 'abt' are anagrams, 'rat', 'tar', 'art' are anagrams, 'can' has no anagrams, 'act' and 'cat' are anagrams.
print(group_anagrams(["bat", "tab", "rat", "can", "act", "tar", "cat", "art", "abt"]))


# C6. Least Frequent Element:
# Given a list, find the element that appears least frequently. Return a tuple containing the element and its count. If there's a tie, return any of them.
def least_frequent(lst):
    # Your code here
    pass


# Test case for least_frequent
# Expected outcome: Any element with the least frequency from the test list, along with its count (e.g., ('dragonfruit', 1) if 'dragonfruit' is the least frequent).
print(least_frequent(lst))
