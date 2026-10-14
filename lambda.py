'''

power=lambda a : a**4
print(power(4))



multiply=lambda a,b: a*b
print(multiply(4,5))


even_odd=lambda n:'even'if n%2==0 else '0dd'
print(even_odd(11))
print(even_odd(14))


num=lambda n:'positive' if n >=0 else 'negative'
n=int(input('enter number :'))

print(num(n))


show=lambda : print('Hello')
show()

show=lambda a : print(a)
print(show(5))

'''
'''
max_num=lambda a,b,c: a if (a>b and a>c) else b if (b>c and b >a)  else c
print(max_num(7,3,12))
print(max_num(50,20,30))
print(max_num(10,80,30))


c_num=lambda n: 'positive' if n>0 else'negative' if n<0  else 'zero'
print(c_num(10))
print(c_num(-50))
print(c_num(0))

num=[1,2,3,4,5,6,7,8,9]
display=list(map(lambda x: x*x ,num))
print(display)

num=[1,2,3,4,5,6,7,8,9]
display=list(map(lambda x: x*x*x ,num))
print(display)


num=[1,2,3,4,5,6,7,8,9,10]
display=list(map(lambda x: x*7 ,num))
print(display)

num=[1,2,3,4,5,6,7,8,9,10]
#n_list=[15,15,15,15,15,15,15,15,15,15]
n_list=[25]*10
display=list(map(lambda x,n: x*n,num, n_list))
print(display)

num=[1,2,3,4,5,6,7,8,9]
display=list(filter(lambda x: x% 2==0,num))
print(display)

marks=[80,75,45,39,59,68,74,88,92]
display=list(filter(lambda x: x >75,marks))
print(display)

marks=[80,75,45,39,59,68,74,88,92]
display=list(filter(lambda x: x <40,marks))
print(display)



t1=[('c' ,19),('b' ,22),('a' ,17),('d' ,27),('e' ,15)]
t1.sort(reverse=True)
print(t1)
t1.sort(key=lambda x: x[1])
print(t1)


str1='infobean'
lengenth=lambda i:len(i)
print(lengenth(str1))



lengenth=lambda i:i.upper()
print(lengenth('infobean'))


lengenth=lambda i:i.lower()
print(lengenth('infobean'))
'''
stud=['shubham','om','abc','yash','sahil','a']
stud.sort(key=lambda i:len(i),reverse=True)
print(stud)
