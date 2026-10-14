students=[]# it is going to collect multiple dictionary
#studen={}
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
        # add students
        case 1:
            roll=int(input("Please enter your roll number :"))
            for stud in students:
                if stud['roll_number']==roll:
                    print("Student alreary exixts")
                    break
                
            else:
                name=input("enter your name :")
                mark=int(input('enter your mark :'))
                stud={
                    'roll_number': roll,
                    'name':name,
                    'mark':mark}
                students.append(stud)
                print("Student added Successfully")
                
                         
        case 2:
           # Display all sstudents
           if len(students)== 0:
               print("No record Available")
           else :
               print(students)
               #print('Roll_no',stud['roll_number'])
               #print('Name',stud['name'])
               #print('Mark',stud['mark'])
        case 3:
            # Search Student
            roll_no=int(input('enter roll number'))
            for stud in students:
                if stud['roll_number']==roll_no:
                    print(" student found")
                    print(stud['roll_number'])
                    print(stud['name'])
                    print(stud['mark'])
                    break
                
            else:
                print("Student not found")


        case 4:
           # Update marks
           roll_no=int(input('enter roll number'))
           for stud in students:
               if stud['roll_number']==roll_no:
                   mark=int(input("enter a new mark :"))
                   stud['mark']=mark
                   print("Student mark updated ")
                   break
           else:
            print('Student not found')
           
        case 5:
           # delete student
            roll_no=int(input('enter roll number'))
            for stud in students:
               if stud['roll_number']==roll_no:
                   students.remove(stud)
                   print("Student deleted")
                   break
            else:
                print('Student not found')
        case 6:
           # display topper
           if len(students)== 0:
               print("No record Available")
           else :
               topper=students[0]
               for stud in students:
                   if stud['mark']> topper['mark']:
                       topper =stud

               print(topper['roll_number'])
               print(topper['name'])
               print(topper['mark'])
        case 7:
           print('Thank you')
           inp=input("do you want to exit from the application (Y/N)")
           if inp =='Y' or inp=='y':
               break
            
        
