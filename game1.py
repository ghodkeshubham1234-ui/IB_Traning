import random
# Guess a nummber
#print('1.Attempt 1\n2.Attempt2\n3.Attempt3')
while(True):
    print('Game loading.......!')
    ip1=input('can you start game? Y|N :')
    if(ip1=='N' or ip1=='n'):
        print('No')
        break
    name=input('enter player name')
    act_num=int(random.randint(1,10))
    score=0
    print(act_num)
    print('guess a number in 3 attempt')
    #att=int(input('attempt_no'))
    #print('attempt 1')
    for i in range(1,4):
        print('attempt',i)
        gess=int(input('Guess number between (1-10):'))
        if(act_num==gess):
            if(i==1):
                score+=100
                print("\033[32mCongratulation you own in 1 attempt\033[0m")
                print('Score is',score)
                break
            elif(i==2):
                #print("1st attempt is wrong,only 2 attempt left")
                score+=80
                print('Congratulation you own in 2 attempt')
                print('Score is',score)
                break
            elif(i==3):
                #print("2nd attempt is wrong,last attempt left")
                score+=60
                print('Congratulation you own in 3 attempt')
                print('Score is',score)
                break
        else:
                print('your',i,'th was fail')
                
    else:
        print('Attempt lemit is exceed','The actual number is',act_num)
                
    res=input('Do you want to Play Again ? Y/N:')
    if(res=='N' or res=='n'):
        print("Thanks for play this game")
        break
    
    '''elif(att==2):
        att+=1
        print('attempt 2')
        gess=int(input('gess number between (1-10):'))
        if(act_num==gess):
            score+=80
            print('Congratulation you own in 2 attempt')
            print('Score is',score)
    elif(att==3):
        print('attempt 3')
        gess=int(input('gess number between (1-10):'))
        if(act_num==gess):
            score+=60
            print('Congratulation you own in 3 attempt')
            print('Score is',score)'''
   
    '''if(att==1):
        gess=int(input('gess number between (1-10):'))
        if(act_num==gess):
            score+=100
            print('Congratulation you own in 1 attempt')
            print('Score is',score)
    elif(att==2):
        gess=int(input('gess number between (1-10):'))
        if(act_num==gess):
            score+=80
            print('Congratulation you own in 2 attempt')
            print('Score is',score)
    elif(att==3):
        gess=int(input('gess number between (1-10):'))
        if(act_num==gess):
            score+=60
            print('Congratulation you own in 3 attempt')
            print('Score is',score)
    else:
        print('Attempt lemit is exceed')'''
   
    
    

    
    
