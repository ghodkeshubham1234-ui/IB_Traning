emp = ['a', 'b', 'c', 'd', 'e']

attendance = [
    ['p','a','l','p','a','l','p','a','l','p'],
    ['p','a','l','p','a','l','p','a','p','p'],
    ['p','p','l','p','a','p','p','a','l','p'],
    ['p','p','l','p','a','p','p','a','p','p'],
    ['p','p','l','p','a','p','p','a','l','p']
]

tota_working_day=10
total_presents=0
total_absents=0
total_leaves=0

for i in range(len(emp)):
    #print(i)
    present=0
    absent=0
    leave=0
    for j in attendance[i]:
        if 'p' in j:
            present+=1
        if 'a' in j:
            absent+=1
        if 'l' in j:
            leave+=1
    att_per=present / tota_working_day *100

total_presents+=present
total_absents+=absent
total_leaves+=leave
print('total_presents',total_presents)
print('total_absents',total_absents)
print('total_leaves',total_leaves)

    
    
        
