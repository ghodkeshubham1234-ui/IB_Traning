data=[3,12,18,21,24,30,35,42]
a =list(filter(lambda x : (x >20 and x % 3 ==0),data))
print(a)
