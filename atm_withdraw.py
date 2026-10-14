print("********************************************************************")

balance=int(input('enter your balance :' ))
w_amount=int(input('enter withdrawal amount  :' ))

if(w_amount <= 0):
    print('Invalid,please enter amount greter than 100')
elif(w_amount % 100 !=0):
    print('Enter amountin multiplis of 100')
elif(w_amount > balance):
    print('insufficient balance')
elif(w_amount > 50000):
    print('Daily withdrawal limit exceeds')
else:
    print('Withdrawal successful')
    print('withdrawal amount =',w_amount)
    print(' Available balance =',balance - w_amount)

    


print("********************************************************************")





print("********************************************************************")




