from requests import get


marks = [
    [80, 75, 90],
    [65, 70, 75],
    [90, 80, 95]
]

#printing individual marks

def get_marks():
    student_number = int(input("Enter Student Number: "))
    if (student_number)==0: 
        subject_number = int(input("Enter Subject Number: "))
        if (subject_number)==0:
            print(marks[0][0])
        elif (subject_number)==1:
            print(marks[0][1])
        elif (subject_number)==2:
            print(marks[0][2])
        else:
            print("NO STUDENT FOUND!")
        
            
        

get_marks()