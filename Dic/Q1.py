# How do you invert a dictionary (swap keys and values)?

my_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {v:k for k ,v in my_dict.items()}
print(inverted_dict)