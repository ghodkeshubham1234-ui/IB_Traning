my_dict={}
dict2={'id':34,'name':'shubham','age':23,'id':344}
print(dict2)
print(dict2['name'])
print(dict2['id'])
print(dict2['name'])
a=dict2.get('idd',"Not found")
print(a)
dict2['city']= 'Pune'
dict2['id']=101
print(dict2)
print(len(dict2))
print(dict2.pop('id'))
print(dict2)
dict2.popitem()
print(dict2)
dict2.clear()
print(dict2)

# del dict2
# print(dict2)

