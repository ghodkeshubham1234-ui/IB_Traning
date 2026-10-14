# 1

data={1:{'name':'Shubham','roll_no':1,'mark':90},
       2:{'name':'yash','roll_no':2,'mark':92},
        3:{'name':'sahil','roll_no':3,'mark':85}}
print(data)

print('*************************************************************')

#2

student_marks={'math':95,'english':80,'python':98,'java':75}
print(student_marks)
count=len(student_marks)
print(count)
total=0
for i  in student_marks.values():
    total+=i
print('Total:',total)
print('Avg',total/count)
temp=0
for i ,mark in  student_marks.items() :
   if mark> temp:
       temp=mark
       sub=i
print('Highest mark is:',temp,'subject is:',sub)
count=0
for i ,mark in  student_marks.items() :
   if mark>80:
       count+=1
       
       print('subject is:',i,' mark is:',mark)
print(count,"subject has mark >80")
    
print('*************************************************************')
#4
car={'brand':'toyota','model':'innova ','year':2024}
print('Model:',car['model'])
car['color']='Black'
print(car)
car.update({'year':2025})
print(car)

del car['model']
print(car)
print(car.keys())
print(car.values())
print(car.items())
print('*************************************************************')
