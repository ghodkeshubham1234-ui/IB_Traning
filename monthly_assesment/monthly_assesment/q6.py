
emp = ['a', 'b', 'c', 'd', 'e']

attendance = [
    ['p','a','l','p','a','l','p','a','l','p'],
    ['p','a','l','p','a','l','p','a','p','p'],
    ['p','p','l','p','a','p','p','a','l','p'],
    ['p','p','l','p','a','p','p','a','p','p'],
    ['p','p','l','p','a','p','p','a','l','p']
]

Total_Working_Days = 10
total_present = 0
total_absent = 0
total_leave = 0
for i in range(len(emp)):
    present = 0
    absent = 0
    leave = 0
    for j in attendance[i]:
        if j == 'p':
            present += 1
        elif j == 'a':
            absent += 1
        elif j == 'l':
            leave += 1

    attendance_percentage = present / Total_Working_Days * 100
    
    dict = {}
    dict[emp[i]] = present

    total_present += present
    total_absent += absent
    total_leave += leave

    if attendance_percentage >= 75:
        status = 'Eligible'
    else:
        status = 'Low Attendance'

    print('Employee Name:', emp[i],'Present Days:', present,'Attendance Percentage:', attendance_percentage, '%','Attendance Status:', status)
    

    if attendance_percentage < 75:
        print('Below 75%')

print('total_present',total_present)
print('total_absent',total_absent)
print('total_leave',total_leave)
print('Employee Present Days:',dict)

highest_present = 0
highest_employee = ''

for name in dict:

    if dict[name] > highest_present:
        highest_present = dict[name]
        highest_employee = name

print('Highest Present Employee:', highest_employee)
print('Highest Present Days:', highest_present)

        
   


