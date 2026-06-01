""" #2. Area of Rectangle: A = length * breadth
len=float(input('ENTER LENGTH :'))
breadth=float(input('ENTER BREADTH :'))
area_of_rec=len*breadth
print(f"Area of Rectangle : {area_of_rec}")

#Area of Rectangle : 30

#1. Simple Interest: SI = (P * R * T) / 100
""" 
""" p=float(input('ENTER PRINCIPLE :'))
r=float(input('ENTER RATE OF % :'))
t=float(input('ENTER TIME :'))
simple_interest=(p*r*t)/100
print(f"Simple Interest : {simple_interest}") """ """

#3. Perimeter of Rectangle: 2 * (length + breadth)
len=float(input('ENTER LENGTH :'))
breadth=float(input('ENTER BREADTH :'))
Perimeter_of_rectangle= 2* (len + breadth)
print(f"Perimeter of Rectangle : {Perimeter_of_rectangle}")

#4. Swap Two Variables using a third variable

#5. Convert Celsius to Fahrenheit: F = (C * 9/5) + 32
c=float(input('ENTER CELSIUS :'))
Celsius_to_Fahrenheit= (c* 9/5) + 32
print(f"Fahrenheit : {Celsius_to_Fahrenheit}")

 #6. Calculate Square and Cube of a Number
n=int(input('ENTER NO. :'))
square = n*n
cube=n*n*n
print(f"Square of {n} : {square}")
print(f"Cube of {n} : {cube}") 

#7. Calculate Total and Average of 3 Marks
 a=float(input('ENTER First Marks :'))
b=float(input('ENTER Second Marks:'))
c=float(input('ENTER Third Marks :'))
Avergae_marks=(a+b+c)/3
print(f"Total Average : {Avergae_marks}")  

#8. Convert Minutes to Seconds
min=float(input('ENTER Time(in min) :'))
Minutes_to_Seconds= min*60
print(f"Seconds : {Minutes_to_Seconds}")

#9. Calculate GST Amount: price + 18%
p=float(input('ENTER PRICE :'))
GST_Amount= p + (p*18/100)
print(f"GST Amount on {p} :{GST_Amount}")

#10. Area of Circle: π * r * r
r=float(input('ENTER Radius :'))
AREA_OF_CIRCLE=  22/7 * r * r
print(f'Area of Circle :{AREA_OF_CIRCLE}')

#11. Compound Interest: A = P (1 + r/100)^t
P=float(input('ENTER PRINCIPLE :'))
r=float(input('ENTER RATE OF INTEREST : '))
t=float(input('ENTER TIME : '))
A= P*(1 + r/100)**t
print(f'Compound Interest = {A}')

#12. BMI Calculator: weight / (height * height)
Weight=float(input('Enter Weight : '))
Height=float(input('Enter Height :'))
BMI = Weight / (Height*Height)
print(f'BMI : {BMI}') """

#13. Total Salary = Basic + HRA(20%) + DA(40%)
b=float(input('ENTER BASIC SALARY : '))
HRA=float(input('ENTER HRA : '))
DA=float(input('ENTER DA : '))
Total_Salary= b + (HRA*20/100) + (DA*40/100)
print(f'Toatal Salary is : {Total_Salary}')