'''
1.Student Performance
Create:
performance(**marks)

The function should display:

Highest marks
Lowest marks
Average
Passed students
Failed students
Number of students above average
'''
'''
def performance(**marks):
    name=list(marks.keys())
    score=list(marks.values())
    higest=max(score)
    lowest=min(score)
    avg=sum(score)/ len(score)

    passed=[]
    failed=[]
    abv_avg=0
    for i in score:
        if i >40:
            passed.append(i)
        else:
            failed.append(i)
        if i > avg:
            abv_avg+=1
    print('Highest =',higest)
    print('Lowest =',lowest)
    print('Average =',avg)
    print('Passed students',len(passed))
    print('Failed students',len(failed))
    print('Number of students above average',abv_avg) 
    print(name)
    print(score)
performance(om=80,rahul=35,aaryan=85,shubham=90,abc=29,pqr=33,a=88,b=76,c=38,d=91,x=56,y4=69)
'''
'''
def performance(**marks):
    name = list(marks.keys())
    score = list(marks.values())

    # Highest and lowest marks with names
    highest_name = max(marks, key=marks.get)
    lowest_name = min(marks, key=marks.get)
    highest = marks[highest_name]
    lowest = marks[lowest_name]

    # Average marks
    avg = sum(score) / len(score)

    passed = []
    failed = []
    abv_avg = []

    # Loop through names and scores together
    for n, s in marks.items():
        if s >= 40:
            passed.append(n)
        else:
            failed.append(n)
        if s > avg:
            abv_avg.append(n)

    # Display results
    print('Highest =', highest, 'by', highest_name)
    print('Lowest =', lowest, 'by', lowest_name)
    print('Average =', round(avg, 2))
    print('Passed students (', len(passed), '):', passed)
    print('Failed students (', len(failed), '):', failed)
    print('Students above average (', len(abv_avg), '):', abv_avg)

    # Debugging lists (optional)
    print('All names:', name)
    print('All scores:', score)


# Example usage
performance(om=80, rahul=35, aaryan=85, shubham=90, abc=29, pqr=33,
            a=88, b=76, c=38, d=91, x=56, y4=69)


Nested Function:
Number Analyzer

Create:
analyze_numbers(numbers)
Inside it create three nested functions:
find_even()
find_odd()
find_positive()

Display:

All even numbers
All odd numbers
All positive numbers


'''
All_even_numbers=[]
All_odd_numbers=[]
All_positive_numbers=[]
def analyze_numbers(numbers):
    
    def find_even(numbers):
        if numbers % 2==0:
            All_even_numbers.append(numbers)
    
            
    def find_odd(numbers):
        if numbers % 2!=0:
            All_odd_numbers.append(numbers)
       

    def find_positive(numbers):
        if numbers > 0:
            All_positive_numbers.append(numbers)
        
    for n in numbers:
        find_even(n)
        find_odd(n)
        find_positive(n)
    print('All_even_numbers =',All_even_numbers)
    print('All_odd_numbers =',All_odd_numbers)
    print('All_positive_numbers =',All_positive_numbers)

analyze_numbers([10,-5,2,0,-8,-12,14,13,-15,-16,-17,18,19,])

'''
*Employee Management*
Create:
employee(**details)

Accept:
name
basic_salary
bonus
department
bonus should have a default value of 5000.

Inside the function create a nested function:
calculate_salary()

Calculate and display:
Employee Name
Department
Basic Salary
Bonus
Total Salary
'''
def employee(**detail):
    def calculate_salary():
        return detail['basic_salary'] + detail['bonus']

   
    print("Employee Name:",detail['name'])
    print("Department:", detail['department'])
    print("Basic Salary:", detail['basic_salary'])
    print("Bonus:", detail['bonus'])
    print("Total Salary:", calculate_salary())



employee(name="Shubham", basic_salary=40000,bonus=5000 ,department="Data Science")

'''

 *Student Management*
Create:
student_report(**students)

Example:
student_report(
    Rahul=85,
    Amit=35,
    Sneha=92,
    Priya=67,
    Karan=28
)

The program should display:

Total Students
Highest Scorer
Lowest Scorer
Average Marks
Passed Students
Failed Students
Inside student_report(), create

 nested functions:

find_total()
find_average()
find_topper()
find_lowest()
check_result()

Create:

shopping_cart(**products)

Example:

shopping_cart(
    Laptop=50000,
    Mouse=1000,
    Keyboard=2000,
    Headphones=3000
)

The function should calculate:

Total amount
Discount
Tax
Final amount

Use a default parameter for discount:

discount=10

Inside the main function, create nested functions for:

calculate_total()
calculate_discount()
calculate_tax()
calculate_final_amount()

Condition: Don't use built-in functions like sum() for calculating the total.
'''
