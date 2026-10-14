# Q21. Student Marks

print("\n" + "=" * 50)
print("Q21. STUDENT MARKS")
print("=" * 50)

marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")



# Q22. Positive, Negative and Zero


print("\n" + "=" * 50)
print("Q22. POSITIVE, NEGATIVE AND ZERO")
print("=" * 50)

positive_count = 0
negative_count = 0
zero_count = 0

positive_sum = 0
negative_sum = 0

for i in range(10):
    num = int(input("Enter number: "))

    if num > 0:
        positive_count = positive_count + 1
        positive_sum = positive_sum + num

    elif num < 0:
        negative_count = negative_count + 1
        negative_sum = negative_sum + num

    else:
        zero_count = zero_count + 1

print("\nPositive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)
print("Positive Sum:", positive_sum)
print("Negative Sum:", negative_sum)



# Q23. Student Performance Analyzer


print("\n" + "=" * 50)
print("Q23. STUDENT PERFORMANCE ANALYZER")
print("=" * 50)

passed = 0
failed = 0
above_75 = 0

highest = 0
lowest = 100

for i in range(1, 11):

    print("\nStudent", i)

    python_marks = int(input("Enter Python marks: "))
    java_marks = int(input("Enter Java marks: "))
    sql_marks = int(input("Enter SQL marks: "))

    total = python_marks + java_marks + sql_marks
    percentage = total / 3

    print("Total:", total)
    print("Percentage:", percentage)

    if percentage >= 90:
        print("Result: Excellent")
    elif percentage >= 75:
        print("Result: Very Good")
    elif percentage >= 60:
        print("Result: Good")
    elif percentage >= 40:
        print("Result: Average")
    else:
        print("Result: Fail")

    if percentage >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

    if percentage >= 75:
        above_75 = above_75 + 1

    if percentage > highest:
        highest = percentage

    if percentage < lowest:
        lowest = percentage

print("\n----- Final Result -----")
print("Number of students passed:", passed)
print("Number of students failed:", failed)
print("Highest percentage:", highest)
print("Lowest percentage:", lowest)
print("Students scoring 75 or above:", above_75)



# Q24. Sum of Numbers


print("\n" + "=" * 50)
print("Q24. SUM OF NUMBERS")
print("=" * 50)

n = int(input("Enter a number: "))

i = 1
total = 0

while i <= n:
    total = total + i
    i = i + 1

print("Sum =", total)



# Q25. Multiplication Table


print("\n" + "=" * 50)
print("Q25. MULTIPLICATION TABLE")
print("=" * 50)

num = int(input("Enter number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)



# Q26. Number Pattern

print("\n" + "=" * 50)
print("Q26. NUMBER PATTERN")
print("=" * 50)

for i in range(1, 6):

    for j in range(1, i + 1):
        print("*", end=" ")

    print()



# Q27. Stop When Number is Found


print("\n" + "=" * 50)
print("Q27. STOP WHEN NUMBER IS FOUND")
print("=" * 50)

while True:

    num = int(input("Enter a positive number or 0 to stop: "))

    if num == 0:
        break

    print("Number entered:", num)


# Q28. List Operations


print("\n" + "=" * 50)
print("Q28. LIST OPERATIONS")
print("=" * 50)

marks = [80, 65, 90, 75, 88, 55, 92, 70, 78, 60]

print("All Marks:", marks)
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))

total = sum(marks)
print("Total Marks:", total)

average = total / len(marks)
print("Average Marks:", average)

count = 0

for mark in marks:
    if mark > 75:
        count = count + 1

print("Students scoring more than 75:", count)



# Q29. Dictionary - Student Information




student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85,
    "course": "Python"
}

# Display student's name
print("Name:", student["name"])

# Display student's marks
print("Marks:", student["marks"])

# Update marks
student["marks"] = 90

# Add city
student["city"] = "Pune"

# Display all keys
print("Keys:", student.keys())

# Display all values
print("Values:", student.values())


# Q30. Collection-Based Problem

print("\n" + "=" * 50)
print("Q30. COLLECTION-BASED PROBLEM")
print("=" * 50)

numbers = [10, 20, 10, 30, 20, 40, 50, 30, 60]

# Remove duplicate values using Set
number_set = set(numbers)

# Convert Set to List
number_list = list(number_set)

# Sort the List
number_list.sort()

# Convert List to Tuple
number_tuple = tuple(number_list)

# Display final Tuple
print("Final Tuple:", number_tuple)

# Create Dictionary containing number as key and square as value
square_dict = {}

for num in number_list:
    square_dict[num] = num * num

print("Square Dictionary:", square_dict)



