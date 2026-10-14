data=[
    {'name':'shubham','salary':50000},
    {'name':'om','salary':25000},
    {'name':'nishant','salary':45000},
    {'name':'sahil','salary':35000},
    {'name':'yash','salary':55000}]

print('********************************************')

data.sort(key=lambda x :x['salary'])
print(data)
print('********************************************')
a=list(filter(lambda x : x['salary']>=45000,data))
print(a)
