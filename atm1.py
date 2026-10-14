
#balance=int(input('Enter Balance'))
print("1.Check Balance\n2.Deposite\n3.Withdrawal\n4.exit")
while(True):
    
    ch=int(input('select which operation want to perform :'))
    if ch==1:
        print('Balance =')
    elif(ch==2):
        print('Deposit')
        #deposit_amt=int(input('Enter Deposit amount'))
    elif(ch==3):
        print('Withdrawal')
    elif(ch==4):
        print('Thank you')
        break
    
