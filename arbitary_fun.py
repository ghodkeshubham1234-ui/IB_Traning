
'''
def mul(*num):
    res=1
    print(num)
    for n in num:
        res*=n
    return res
print(mul(1,2,3,4,5))
print()

def display_names(name,*marks):
    print('Name:',name)
    print('Marks :',marks)
  
display_names('abc',90,80,85)
'''

def max_num(*num):
    max1=num[0]
    for i in range(len(num)):
        if num[i]> max1 :
            max1=num[i]
    return max1

list=[]
n=int(input('enter number:'))
for i in range(n):
    inp1=int(input(f'Enter number {i+1}:'))
    list.append(inp1)
a=tuple(list)
print(max_num(*a))
 
