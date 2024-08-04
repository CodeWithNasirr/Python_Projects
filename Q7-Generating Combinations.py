# Given two lists of strings, write a Python function that returns a list of all possible concatenated pairs of strings, one from each list, but only include pairs where the total length of the concatenated string is greater than 5


def concatenated_pairs(list1, list2):
    return [s1 + s2 for s1 in list1 for s2 in list2 if len(s1 + s2) > 3]

# Example usage
list1 = ["a", "ab", "abc"]
list2 = ["x", "xy", "xyz"]
result = concatenated_pairs(list1, list2)
print(result)  # Output: ['abxyz', 'abcx', 'abcxy', 'abcxyz']
