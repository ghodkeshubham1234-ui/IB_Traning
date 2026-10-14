name="  my name is    ghodke shubham shubham shubham sudhakar  "
loc='pune'
c='123abc'
print(len(name))
print(name)
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.strip())
#print(name.lstrip())
a=(name.lstrip())

print(len(a))
print(len(name.rstrip()))
print('***************')
a=name.find('shubham')
print(a)
b=name.find('shubham',a+1)
print(b)
name=name[:b]+".."+name[b +len('shubham'): ]
print(name)
print(name.replace('sudhakar','S'))
print(name.find('shubham'))
print(name.count('a'))
print(name.startswith('s'))
print(name.endswith('r'))
print(name.isalpha())
print(name.isdigit())
print(c.isalnum())
print(loc.isspace())
print(name.split())
print(name.join(loc))

s1='abc@def@ghi@jkl@mno@prq@stu@vwx@yz'
s=s1.split('@')
print(s1)
print(" ".join(s))

num=['10','20','30','40']
print("-".join(num))
