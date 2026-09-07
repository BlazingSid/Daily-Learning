marks = [
    [80, 75, 90],
    [65, 70, 75],
    [90, 80, 95]
]

#sum of individual students 
for i, rows in enumerate(marks):
    print(f"Student No {i} has Total Marks of : {sum(rows)}")

#sum of all Students marks
total_marks = 0
for i in range(len(marks)):
    for j in range(len(marks[0])):
        total_marks += marks[i][j]

print(f"The Total Marks of All Students Is : {total_marks}")