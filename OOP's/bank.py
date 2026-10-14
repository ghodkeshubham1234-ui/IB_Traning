class bank :
    name='a'
    acc_no=1223
    real_amt=50000
    
    def deposit(self,dept_amt):
        print('Deposit amount :',dept_amt)
        self.real_amt+=dept_amt
        
    def withdrwal(self,w_amt):
        if self.real_amt > w_amt:
            self.real_amt=self.real_amt - w_amt
        print('withdrwal amount is :',w_amt)
        
    def check_bal(self):
        print('Available balance is :',self.real_amt)
    def display(self):
        print('Name :',self.name)
        print('Account no :',self.acc_no)
        print('Total Balance',self.real_amt)
b=bank()
b.name=input('enter your name:')
b.acc_no=int(input('enter your Account no  :'))
b.real_amt=int(input('enter your real balance :'))
dept_amt=int(input('enter your deposit amount :'))
b.deposit(dept_amt)
w_amt=int(input('enter your withrwal amount :'))
b.withdrwal(w_amt)
b.check_bal()
b.display()
        
