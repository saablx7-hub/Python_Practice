""" p=int(input("Enter your principal :"))
r=float(input("Enter your Rate of interest :"))
t=int(input("Enter your Time :"))

def si(p,r,t):
    return (p*r*t)/100

print(si(p,r,t))
 """

 
a = int(input("Enter your first number :"))
b= int(input("Enter your second number :"))
operator = input("Enter your choice of operator(+.-,/,%,*) :")
if operator == "*":
    print(a*b)
elif operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "/":
    print(a/b)
elif operator == "%":
    print(a%b)
else:
    print("Error")