print('1.Addition \n2.Subtraction \n3. Multiplication \n4.Division \n 5.Modulus \n 6.Square \n7.cube \n8.Round')
while(True):
    ch=int(input('Which operation you want to perform:'))
    if ch == 1:
        num1=int(input('Enter number 1'))
        num2=int(input('Enter number 2'))
        add = num1 + num2
        print("Addition =",add)
    elif ch == 2:
        num1=int(input('Enter number 1'))
        num2=int(input('Enter number 2'))
        sub = num1 - num2
        print("Subtraction =",sub)
    elif ch == 3:
        num1=int(input('Enter number 1'))
        num2=int(input('Enter number 2'))
        mul = num1 * num2
        print("Multiplication =",mul)
    elif ch == 4:
        num1=int(input('Enter number 1'))
        num2=int(input('Enter number 2'))
        div = num1 / num2
        print("Division =",div)
    elif ch == 5:
        num1=int(input('Enter number 1'))
        num2=int(input('Enter number 2'))
        mod = num1 % num2
        print("Modulus =",mod)
    elif ch == 6:
        num1=int(input('Enter number 1'))
        sq = num1 * num1
        print("Square  =",sq)
    elif ch == 7:
        num1=int(input('Enter number 1'))
        cube = num1 * num1 * num1
        print("Cube  =",cube)
    elif ch==8:
        num=float(input('Enter float number :'))
        print(round(num))

        
    res=input('Do you want to continue ? Y/N:')
    if(res=='N' or res=='n'):
        print("Thanks for use this application")
        break
