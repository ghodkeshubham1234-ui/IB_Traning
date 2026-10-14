stud={'roll_no':24 ,
    'name':'Shubham',
      'course':"AI$DS",
      'age':23,
      'city':'Pune',
      'subject':['ML','DMV','IIOT','UI/UX']}
print(stud)
print(stud.items())
for i in stud:
    print(i)

for i in stud.items():
    print(i)

if "city" in stud:
    print('exists')
else:
    print('Not exixts')

    
print(stud['subject'][:2])
print(stud['subject'][-1])
print(stud['subject'][2])
print(stud['subject'][3])



print(stud.get('subject'))

print("**********************************************************************")

for i in stud['subject']:
    print(i)
