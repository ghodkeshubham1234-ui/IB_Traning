'''
Question: Student Management System
Write a menu-driven Python program to create a Student Management System using while True and match-case.

Store student details in a list of dictionaries.

Each student should have:

{
    "roll": 101,
    "name": "Rahul",
    "marks": 85
}
Display the following menu repeatedly:

===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. Display All Students
3. Search Student
4. Update Marks
5. Delete Student
6. Display Topper
7. Exit
Your program should perform the following operations:

Add Student: Accept roll number, name, and marks and add the student to the list. Duplicate roll numbers should not be allowed.
Display All Students: Display details of all students. If no students are available, display an appropriate message.
Search Student: Accept a roll number and display the student's details if found; otherwise display "Student not found".
Update Marks: Accept a roll number and update the marks of that student if the student exists.
Delete Student: Accept a roll number and delete the corresponding student from the list.
Display Topper: Find and display the student who has scored the highest marks.
Exit: Display a suitable message and terminate the program using break.

'''
student=[
 {
    "roll_number": '101',
    "name": "Rahul",
    "marks": 85
}]
while(True):
    
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print(" 1. Add Student")
    print(" 2. Display All Students")
    print(" 3. Search Student")
    print(" 4. Update Marks")
    print(" 5. Delete Student")
    print(" 6. Display Topper")
    print(" 7. Exit")
    
    ch=int(input("Enter your choice (1-7)"))
    match ch:

       case 1:
           print(" Add new Student :")
           roll_number=(input("Enter your roll number :"))
          # for i in range(len(student)):
           for i in student:
                   print(i)
                   '''if roll_number in studentj :
                       
                       print(student[j])
                       print("Roll Number already exists:")
                       break'''
           
           name=input("Enter your name :")
           marks=int(input ("Enter your mark (mark should be in betwen 0-100):"))
          ''' data={}
           data['roll_number']=roll_number
           data['name']=name
           data['marks']=marks
           print(data)
           student.append(data)
           print(student)'''

           
                     
       case 2:
           pass
           
       case 3:
           pass
       case 4:
           pass
       case 5:
           pass
       case 6:
           pass
       case 7:
           print('Thank you')
       






