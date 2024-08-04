# //Write a Python function that takes a list of tuples, where each tuple contains a student's name and their score, and returns a list of the names of students who scored above a certain threshold.

# Input
students_scores = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 88)]
threshold = 80

# Output
["Alice", "Charlie", "David"]

def student_in_threshold(students_scores,threshold):
    # return[name for name,score in students_scores if score>threshold] #listcomparesions
    results=[]
    for name,score in students_scores:
        if score > threshold:
            results.append(name)
    return results
    
students_scores = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 88)]
threshold = 80

x=student_in_threshold(students_scores,threshold)
print(x)