a={10,20,30,40,50,60,70}
b={50,60,70,80,90,100,111}
"""
# union
a.union(b)
print(a)
print(a.union(b))

s1=a.union(b)
print(s1)
s2={1,2,3,4,5}
s3={4,5,6,7,8}

print(s3.union(s2))



print(a.intersection(b))
print(a&b)
"""
"""
print(a)
print(b)
print(a-b)
print(a.difference(b))
print(b-a)
# symmetric_difference
print(a.symmetric_difference(b))
print(a^b)
print(b^a)

"""

"""
s1={1,2,3,4,5,6,7}
s2={5,6,7}
print(s1.issubset(s2))
print(s2.issubset(s1))

print(s1.issuperset(s2))
print(s2.issuperset(s1))

print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))
"""

a={1,2,3,4,5,6}

print(5 in a)
print(5 not in a)

print(7 in a)
print(7 not in a)


fruit={"apple","orange","banana"}
print(fruit)
for i in fruit:
    print(i)
