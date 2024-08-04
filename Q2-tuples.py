def product_except_self(input_tuple):
    result = []
    total_product = 1
    for num in input_tuple:
        total_product *= num
    for num in input_tuple:
        result.append(total_product // num)
    return tuple(result)

# Example usage
original_tuple = (1, 2, 3, 4)
result = product_except_self(original_tuple)
print(result)  # Output: (24, 12, 8, 6)
