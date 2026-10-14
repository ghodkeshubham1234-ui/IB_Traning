
'''def max_num(*num):
    even_count=0
    odd_count=0
    for i in range(len(num)):
        if i% 2==0:
            even_count+=1
        else:
            odd_count+=1
    print('Even Count :',even_count)
    print('Odd Count :',odd_count)


list=[]
n=int(input('enter number:'))
for i in range(n):
    inp1=int(input(f'Enter number {i+1}:'))
    list.append(inp1)
a=tuple(list)
print(max_num(*a))
 


def max_num(*num):
    max1=num[0]
   
    for i in range(len(num)):
        if num[i]> max1 :
            max1=num[i]
    return max1
def min_num(*num):
    min1=num[0]
    for i in range(len(num)):
        if num[i]< min1 :
            min1=num[i]
    return min1



list=[]
n=int(input('enter number:'))
for i in range(n):
    inp1=int(input(f'Enter number {i+1}:'))
    list.append(inp1)
a=tuple(list)
print(max_num(*a))
print(min_num(*a))

 
def tot(*arg):
    total=0
    avg=0
    count=len(arg)
    for i in arg:
        total+=i
    print('Total',total)
    avg=total/count
    print('Average :',avg)
    print('count of number',count)
    for j in arg:
        if avg<j:
            print("Mark is greter than average",j)
    
list=[]
n=int(input('enter number:'))
for i in range(n):
    inp1=int(input(f'Enter number {i+1}:'))
    list.append(inp1)
a=tuple(list)
print(tot(*a))

unique=[]
def uniqe_val(*num):
    
    for i in num:
        if num[i] in num[i+1:]:
            continue
        unique.append(num[i])
        
        #if num.count(i)==1:
            #unique.append(i)
    print('Unique numbers are:',unique)
            
        
            
        

list=[]
n=int(input('enter number:'))
for i in range(n):
    inp1=int(input(f'Enter number {i+1}:'))
    list.append(inp1)
a=tuple(list)
uniqe_val(*a)
'''
unique=[]
def freq(target,*num):
    fre=0
    for i in num:
        if i == target:
            fre+=1
    print("Frequency of targrt no. is :",fre)
        
   

list=[]
n=int(input('enter number:'))
for i in range(n):
    inp1=int(input(f'Enter number {i+1}:'))
    list.append(inp1)
target=int(input('enter target  number :'))
a=tuple(list)
freq(target,*a)


'''
def pos_neg_zero(*num):
    pos_count=0
    neg_count=0
    zero_count=0
    pos=[]
    neg=[]
    zero=[]
    for i in num:
        if i > 0:
            pos.append(i)
            pos_count+=1
        if i < 0:
            neg.append(i)
            neg_count+=1
        if i==0:
            zero.append(i)
            zero_count+=1
    print('Positive Numbers :',pos)
    print('Negative Numbers :',neg)
    print('Zero Numbers :',zero)


    print('Positive Count :',pos_count)
    print('Negative Count :',neg_count)
    print('Zero Count :',zero_count)


list=[]
n=int(input('enter number:'))
for i in range(n):
    inp1=int(input(f'Enter number {i+1}:'))
    list.append(inp1)
a=tuple(list)
pos_neg_zero(*a)
'''
