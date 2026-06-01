#1. Convert a string "123" into an integer and add 10. What is the result?

a=int("123")
b=10

sum=(a + b)
print(sum)

#2. Write a Python program to convert a floating-point number 45.67 into an integer.

a=int(45.67)
print(a)

#3. Convert the string "56.78" into a float and multiply it by 2.
a=float("56.78")
b=2
multiply= (a*b)
print(multiply)

#5. Convert an integer 100 into a string and print its type
a=str(100)
print(type(a))

""" #7. What happens when you try to convert the string "abc" into an integer using int("abc")?
a=int('abc')
print(a)
 """
#10. Write a Python program to take user input (as a string) and convert it to float, then display the result.
a=float("233")
print(a)

#4. Given a list of string numbers ["1", "2", "3", "4"], convert all elements into integers.
list1 = ["1", "2", "3", "4"]

print(len(list1))
print(type(list1))
""" 
for x in range(len(list1)):
    print(f"{x}:{list1[x]}:{type(list1[x])}")

for x in range(len(list1)):
    print(f"{x}:{list1[x]}:{type(int(list1[x]))}") """

print(f'{list1[0]}: {type(list1[0])}')
print(f'{list1[0]}: {type(int(list1[0]))}')


print(f'{list1[1]}: {type(list1[1])}')
print(f'{list1[1]}: {type(int(list1[1]))}')

print(f'{list1[2]}: {type(list1[2])}')
print(f'{list1[2]}: {type(int(list1[2]))}')

print(f'{list1[3]}: {type(list1[3])}')
print(f'{list1[3]}: {type(int(list1[3]))}')

#6. Convert a boolean value True into an integer. What output will you get?
bool=False
print(int(bool))