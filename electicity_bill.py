print("********************************************************************")

    
print("-------------  Electricity Bill --------------")
unit=int(input("Enter units of this month : "))
bill=0
if(unit < 0):
    print('Wrong input.please enter valid unit')
elif(unit > 0 and unit <101):
    bill=unit * 5
    
elif(unit > 101 and unit <201):
    bill=unit * 7
    
elif(unit >201 and unit <301):
    bill=unit * 10

elif(unit > 300):
    bill=unit * 15



print('Units =',unit)
print('Total Bill =',bill)

    

    
print("********************************************************************")
