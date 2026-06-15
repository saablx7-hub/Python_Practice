student = ["Saatvik", "Aditya" , "Kushagra" , "Suhaan"]
""" for x in student:
    print(x)

print(len(student))

for z in range(2,11,3):
    print(z)
 """

""" for x in range(0,4):
    print(student[x]) """

""" for x in range(len(student)):
    print(student[x]) """

students = ["Saatvik" , "Aditya" , "Kushagra" , "Suhaan" , "Abeer"]
""" for x in students:
    print (x)

for x in range(0,4):
    print(student[x])

for x in range(len(student)):
    print(student[x])

 """
""" for x in students:
    print(x)
    if x == "Aditya":
        break
 """
""" for x in students:
    if x == "Aditya":
        continue
    print(x) """

#FOR LOOP NESTED
""" for x in range(5):
    for i in range(5):
        print("*", end=" ")
    print() """
    
""" for x in range(3):
    for i in range(3):
        print( i+1 , end=" ")
    print() """

""" for x in range(6):
    for i in range(x + 1):
        print("*" , end=" ")
    print() """
"""  (0,0)
(0,1)
(0,2)
(1,0)
... """

""" for x in range(3):
    for y in range(3):
        print(f"({x},{y})") """

"""  *
   ***
  *****
 *******
********* """

for x in range(6):
    for i in range(x + 1):
        print("*" , end="")
    print()

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
    
for x in [0, 1, 2]:
  pass
