class student:
    name='a'
    roll_no=1
    obtain_mark=100
    per=0

    def cal_per(self,total_marks):
        self.per=(self.obtain_mark / total_marks)*100
        print('percentage :',self.per)
        
    def result(self):
        
        if self.per > 35.0:
            print('Pass')
        else:
            print('fail')
            
    def show(self):
        print('Name :',self.name)
        print('Roll_no :',self.roll_no)
        print('Obtain_Mark :',self.obtain_mark)
        
s=student()
s.name=input('Enter your name :')
s.roll_no=int(input('Enter your roll no :'))
s.obtain_mark=int(input('Enter your Obtain_Mark :'))
#s.per=0
total_marks=int(input('Enter your total_marks :'))
s.cal_per(total_marks)
s.result()
s.show()
