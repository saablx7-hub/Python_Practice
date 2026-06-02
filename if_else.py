""" #1. Write a program to check if a number is positive or negative
a= -34
if a < 0:
    print("a is negative")

#2. Write a Python program to check whether a number is even or odd using if-else
a= float(input('ENTER NUMBER :'))
if a%2 == 0:
    print(f"[{a}] is Even")
else:
    print(f"{a} is odd") """

#3. Write a program to input a person's age and print 'Minor' if less than 18, 'Adult' if between 18 and
#60, and 'Senior' if 60 or above.
a= float(input("Enter your age :"))
if a < 18:
    print("Minor")
elif  a < 60:
    print('Adult')
elif a >= 60:
    print('Senior')

#4. Write a program that checks if a character entered is a vowel or a consonant
a= (input('ENTER ALPHABET :'))
if a == aeiouAEIOU:
    print("vowel")
else:
    print("consonant")