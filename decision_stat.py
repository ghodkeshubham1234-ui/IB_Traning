"""
num=int(input("Enter a number:"))
if(num >0):
    print(num,'Number is positive')
else:
    print(num,"Number is negatice")

"""
"""

print('########## Marksheet #########')
name=input('Enter your name : ')
eng=int(input('enter marks of English :'))
hin=int(input('enter marks of Hindi :'))
ma=int(input('enter marks of Marathi :'))
total_score=eng+hin+ma
Avg_score=total_score /3

if(Avg_score >=71):
    print('Congratulations',name, 'pass with Distinction','Percentage:',Avg_score,'%')

elif (Avg_score >= 56 and Avg_score <=70):
        print('Congratulations',name, 'pass with Firstlass','Percentage:',Avg_score,'%')
elif (Avg_score >= 36 and Avg_score <=55):
        print('Congratulations',name, 'pass with Second','Percentage:',Avg_score,'%')
else:
        print(name,"is Fail",'Percentage:',Avg_score,'%', )
        """

