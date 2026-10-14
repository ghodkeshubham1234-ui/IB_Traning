data=[5,12,18,25,30,42,40,15,50]
a=list(sorted((filter(lambda x : x>=15 and x<=40,data)),reverse=True))
print(a)
