'''def show(name,age,marks,address):
    print(name)
    print(age)
    print(marks)
    print(address)
show('Shubham',20,marks=80,address='Pune',)

def emp(name,sal,dep,id1):
    print(id1)
    print(name)
    print(sal)
    print(dep)
emp('Shubham',20000,dep="HR",id1=101)


def show(name,age,marks):
    print(name.upper())
    print(age)
    print(marks)
   
    count=len(marks)
    for i in marks:
        total+=i
    print("Average mark is :",total /count)
        
show('Shubham',age=20,marks=(80,90,85))

def show(name,age,eng,hindi,math):
    a=name.upper()
    res=eng+hindi+math
    avg=res/ 3
    #print("Average mark is :",avg)
    print(f" {a} your age is {age} & your average score is {avg}")      
show('Shubham',age=20,eng=80,hindi=85,math=90)

# keyword with arbitary
def data(**marks):
    print(marks)
    a=len(marks.items())
    b=sum(marks.values())
    print(b)
    avg=b/a
    print(avg)
    for sub,mark in marks.items():
        #print(sub)
        #print(mark)
        print(f"{sub} : {mark}")
data(eng=80,hindi=90,math=95)


def data(*marks,name,**details):
    print(name)
    print(marks)
    print(details)
   
data(80,90,95,name='Shubham',age=22,gender='Male',add='pune')

 #position matters when we combine arbitary argument and arbitary keyword argument ,
#write arbitary argument first and then  arbitary keyword argument


#Default Function
def addition(a=10,b=20):
    res=a+b
    return res
print('***************Addition of two numbers **************')
print(addition())
num1=int(input('Enter Number 1 :'))
num2=int(input('Enter Number 2 :'))
print(addition(num1,num2))

'''

# Nested function

def outer_fun(text):
    message=text
    def inner_fun():
        print(message)
    inner_fun()
outer_fun("Hello")

def pos_neg(num):
    def pos(n):
        return n>=0
    for n in num:
        if pos(n):
            print('Positive :',n)
        else:
            print('Negative :',n)
pos_neg([10,-5,2,0,-8])
