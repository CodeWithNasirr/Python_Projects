# # Example usage
original_list = [1, 2, 3, 4, 5]

results=[]
for i in range(len(original_list)-1):
    sum=original_list[i]+original_list[i+1]
    print(sum)
#     results.append(sum)

# results.append(original_list[-1])

# # print(results)
# # # Output: [3, 5, 7, 9, 5]

# # function

def adder(list):
    return [list[i] + list[i+1] for i in range(len(list)-1)] + [list[-1]]


original_list = [1, 2, 3, 4, 5]
results=adder(original_list)
print(results)