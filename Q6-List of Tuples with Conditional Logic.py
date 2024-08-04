# Input
students_scores = [("Alice", 85, 90), ("Bob", 75, 35), ("Charlie", 95, 80), ("David", 60, 60)]

# Output
["Alice", "Charlie"]



def students(x):
    results=[]
    for name,num1,num2 in x:
        if num1 >80 or num2>80:
            results.append(name)
    return results


students_scores = [("Alice", 85, 90), ("Bob", 75, 35), ("Charlie", 95, 80), ("David", 60, 60)]

y=students(students_scores)
print(y)