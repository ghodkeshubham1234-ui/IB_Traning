class student:
    s_id=111
    age=23
    add='pune'
    def show(self):
        print('it is a show function')
    def display(self):
        print('it is a display function')

s1=student()
print(s1.s_id)
print(s1.age *2)
s1.show()
s1.display()
s2=student()
s2.show()
s2.display()

