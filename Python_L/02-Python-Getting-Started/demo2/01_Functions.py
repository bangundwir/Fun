# # Functions
# print("Hello Wolrd")
# str(3) == "3"
# int("15") == 15
# username = input("Enter the user's name: ")

# student = []

# def get_students_titlecase():
#     students_titlecase = []
#     for student in students:
#         students_titleacase = student.title()
#     return students_titlecase

# def print_students_titlecase():
#     students_titlecase = []
#     for student in students:
#         students_titleacase = student.title()
#     print (students_titlecase)

# def add_sutdent(name):
#     students.append(name)

#===================================#

# Funtions Arugment
# Code yang disempurnakan

student = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase():
    student_titlecase = get_students_titlecase()
    print (students_titlecase)

def add_sutdent(name, student_id):
    students.append(name)

student_list = get_students_titlecase()

add_student("Mark")



