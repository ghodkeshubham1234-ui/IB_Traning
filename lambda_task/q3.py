data=[6,22,46,4,2,12,60,80]
a =list(filter(lambda x:  (x%2==0 and x>20) ,data))
print(a)
