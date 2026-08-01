"""Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line."""


if __name__ == '__main__':
    students_grade = []
    
    # 1. Collect inputs
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_grade.append([name, score])
        
    # 2. Sort the nested list by score (index 1)
    # If scores are equal, it automatically sorts by name (index 0)
    students_grade.sort(key=lambda x: (x[1], x[0]))
    
    # 3. Identify the absolute lowest score
    lowest_score = students_grade[0][1]
    second_lowest_score = None
    
    # 4. Find the actual second lowest score value by skipping the lowest
    for student in students_grade:
        if student[1] > lowest_score:
            second_lowest_score = student[1]
            break
            
    # 5. Print all student names that match this second lowest score
    for student in students_grade:
        if student[1] == second_lowest_score:
            print(student[0])