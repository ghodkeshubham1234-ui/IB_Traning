# 1 & 3

s=set()
print(s)
print(type(s))

#2
s1={1,2,3,4,5,6,6,6,6,6,7,8,9,10}
print(s1)


l=[1,2,3,4,5,5,4,3,2,1]
s2=set(l)
print(l)
print(s2)


#3
s3={}
print(type(s3))


#4
s1.add(11)
print(s1)
#5
s1.update([12,13,14,15])
print(s1)

# 6
s1.remove(15)
s1.discard(14)
print(s1)

#7

s1.discard(99)
print(s1)


#8
print(s1)
print(s1.pop())
print(s1)
#9
s4={1,2,3,4,5,6,6,6,6,6,7,8,9,10}
for i in s4:
    print("square of  ",i,"is ",i*i)


#10
for i in s4:
    if(i%2==0):
        print(i)
    
    
    
#11
count=0

for i in s4:
    count+=1
print("count:",count)
# 12

sum=0
for i in s4:
    sum+=i
print(sum)

#13

python_student={"rahul","amit","priya","neha"}
java_student={"amit","neha","rohan","karan"}

print("learning both :",python_student & java_student)
print("only python:",python_student - java_student)
print("only java:",java_student - python_student)
c=java_student | python_student
print(c)
unique_count=0
for i in c:
    unique_count+=1
print(unique_count)



my_set=(9,8,7,3,4,2,1)
count=0
for i in my_set:
    count+=1
    print("count:",count,"square:",i*i)


