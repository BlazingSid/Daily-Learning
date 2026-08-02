"""The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal."""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
def get_average_marks(student_marks, name):
    
    if name not in student_marks:
        return f"Error: '{name}' not found in the dictionary."
    
    marks = student_marks[name]
    if not marks:
        return f"{name} has no marks recorded."
        
    average = sum(marks) / len(marks)
    return f"{average:.2f}"
    
query_name = input()
print(get_average_marks(student_marks, query_name))
