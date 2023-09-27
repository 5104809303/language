# students = {
#    "student1": { 
#     "name":"sandhya",
#     "age":24,
#     "roll number":438,
#     "subject":"maths",
#     "marks": 70
#     },

#    "student2": {
#     "name":"sweety",
#     "age":20,
#     "roll number":431,
#     "subject":"social",
#     "marks": 60
#     },
#    "student3": {
#     "name":"sai",
#     "age":21,
#     "roll number":422,
#     "subject":"english",
#     "marks": 75
#     },
#    "student4": {
#     "name":"munny",
#     "age":20,
#     "roll number":420,
#     "subject":"physics",
#     "marks": 50
#     }
# }

# #     "student1":student1,
# #     "student2":student2,
# #     "student3":student3,
# #     "student4":student4
# # }
# # emp_438=students.rollnumber1

# print(students)          

# # read = classes

# def read(students):
#     return students

# def add(students):
#     return students


# print("All student details")
# print("1.read")
# print("2.add")
# print("3.update")
# print("4.delete")

# cls="{}"

# option = input("select your option[1-4]: ")

# if option in ['1','2','3','4']:
#     print("selected option")
# if option=='1':
#     print("print all the student details")
#     print(cls.format(students))
# elif option =='2':
#      x=input("enter roll number:")
#     #  print("x"  + " " + "marks"+" "+"age"  +" "+"roll number" +" "+"subject")
#      students.append(student1)
#      print(f'add details of students {students}')
#     # print(students["student1"][""])
    
   

# else:
#     del students

#     print(students)

students = []
 
#  1 add student details 
def add_student():
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")
    age = int(input("Enter student's age: "))
    marks = float(input("Enter student's marks: "))

    student = {
        'name': name,
        'roll_number': roll_number,
        'age': age,
        'marks': marks
    }
    students.append(student)
    print("Student details added successfully!")

#add student details
def add_details():
   
    for student in students:
        print("student name:",student["name"])
        print("student roll number:",student["roll_number"])
        print("student age:",student["age"])
        print("student age:",student["age"])
        print()

#roll number
def student_roll_number():
    roll_number=input("enter the roll_number:")

    for student in students:
        if student['roll_number']==roll_number:
              print("student name:",student['name'])
              print("student roll number:",student['roll_number'])
              print("student age:",student['age'])
              print("student age:",student['age'])
              return
   
    print("student not found with the given rol number")
# Prompt the user for input
while True:
     choice = input("Enter your choice (1 -4):")
     if choice in ['1','2','3','4']:
        print("slect the choice")    
     if choice== '1':
         add_student()
     elif choice == '2':
         add_details()
     elif choice== '3':
         student_roll_number()
         break
     else:
          print("student details has deleted")
   
