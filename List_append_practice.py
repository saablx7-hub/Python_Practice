#1. Append a String
#Create a list of fruits: ["apple", "banana"]. Append "mango" to the list and print the final list.
""" fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)
 """
#2. Append User Input
#Ask the user to enter 3 favorite colors one by one. Append each to a list and display the list.
""" colour =[]
for x in range(3):
    a= input("Enter colour :")
    colour.append(a)
print(colour)
 """
#3. Append in a Loop
#Create an empty list. Append the square of numbers from 1 to 5 into it using a loop. Print the list
""" squares =[]
for x in range(6):
    a = x*x
    squares.append(a)
print(squares) """

#4. Append Numbers Based on Condition
#From the range 1 to 20, append only numbers divisible by 3 into a list. Print the final list.
""" a =[]
for x in range(1,21):
    if x%3 == 0:
        a.append(x)
print(a) """

""" 5. Append a List as a Single Element
Given:
list1 = [1, 2]
list2 = [3, 4]
Use append() to add list2 to list1. Print list1. What will be the length of list1? """
""" list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
print(list1)
print(len(list1))
 """
""" 6. Append Dictionaries to a List
Write a program that takes 2 user inputs: name and age. Append them as a dictionary to a list. Repeat for 3
users. """

#7. Append to Nested List
#Create a list: students = [["Alice", 85], ["Bob", 90]]. Append a new student ["Charlie", 88] using append().
""" students = [["Alice", 85], ["Bob", 90]]
students.append(["Charlie", 88])
print(students) """

#9. Using Append with Condition from List
#Given: scores = [45, 67, 23, 90, 88]. Append only scores > 50 to a new list called passed.
""" scores = [45, 67, 23, 90, 88]
Passed = []
for x in (scores):
    if x > 50:
        Passed.append(x)
print(Passed) """

#10. Append and Sort
#Take 5 numbers as input from the user, append them to a list. Sort the list and print it
""" numbers = []
for x in range(5):
    a= int(input("Enter Your Number :"))
    numbers.append(a)
print(numbers) """

#11. Take 10 values from the user and split even numbers in even list and odd numbersa in odd list .
""" numbers= []
even_numbers=[]
odd_numbers=[]
for x in range(10):
    a = int(input("Enter your number :"))
    numbers.append(a)
print(numbers)
for x in (numbers):
    if x%2 ==0:
        even_numbers.append(x)
        
    else:
        odd_numbers.append(x)
        
print(even_numbers)
print(odd_numbers) """

#1. Daily Expense Tracker
#Create an empty list called expenses.
#Ask the user to enter daily expenses for 7 days and store each amount using append ().
#Finally, print the complete expense list. 
Expenses = []
for x in range(7):
    a=input(f"Enter your Day{x+1} Expenses :")
    Expenses.append(a)
print(Expenses)
total = 0
for x in Expenses:
    total = total + int(x)
print(total)

#2. Employee Attendance System
#You are given an empty list present_employees.
#Take employee IDs from the user until they type "done" and add each ID to the list using
#append (). 
