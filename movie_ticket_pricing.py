print("********************************************************************")
age=int(input('Enter your age :'))
day=input('Enter Day (Sun,Mon,......)')
ticket_price=0
if (age <5):
    print('Free Ticket')
    ticket_price+=0
elif(age > 5 and age <13 ):
    print('Price of ticket is 100')
    ticket_price +=100
elif(age > 13 and age < 60 ):
    print('Price of ticket is 200')
    ticket_price +=200
elif(age > 60):
    print('Price of ticket is 120')
    ticket_price +=120

else:
    print("Try again")

if day == 'Wed':
    discount=ticket_price * 0.20
    print('Discount Amount =',discount)
    print('Final bill =',ticket_price - discount)

else:
    print('Final bill =',ticket_price)


    
    
    
    
       
