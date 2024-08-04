# Given a dictionary where keys are strings and values are lists of integers, write a Python function that returns a new dictionary where each key maps to the sum of the even numbers in its corresponding list.

# Input
input_dict = {
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9]
}

# Output
{"a": 2, "b": 10, "c": 8}


def sum_even_values(dic):
    return{key:sum(num for num in values if num%2==0) for key,values in dic.items()}

input_dict = {
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9]
}

x=sum_even_values(input_dict)
print(x)