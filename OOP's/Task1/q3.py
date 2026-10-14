class card:
    print('='*55)
    print("         ISBM         ")
    print('='*55)
   
    School_name= "ISBM "
    def __init__(self,s_name,r_no,div):
        self.s_name=s_name
        self.r_no=r_no
        self.div=div

    def display(self):
        print('Student Name:',self.s_name)
        print('Student Roll_no:',self.r_no)
        print('Student div:',self.div)
        print('\n')
c=card('shubham',1,'A')
c.display()
        
c=card('om',1,'B')
c.display()

c=card('pratik',1,'A')
c.display()

c=card('yash',1,'B')
c.display()
