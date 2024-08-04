# Given a list of lists where each sublist contains integers, write a Python function that flattens this list of lists into a single list containing only the even numbers.

# Input
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Output
[2, 4, 6, 8]


def flatten_and_filter_evens(list_of_lists):
    return [num for sub_list in list_of_lists for num in sub_list if num%2==0]


list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

x=flatten_and_filter_evens(list_of_lists)

print(x)