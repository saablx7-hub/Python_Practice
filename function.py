#function - it is block of code which performs a particular task
#reusability

""" def sum():
    a=45
    b=49
    sum=a+b
    return sum

print(sum()) #calling of function """
""" 
def sum():
    a = 4
    b = 6
    total=a+b
    print(total)

sum() """
""" 
def sum(a,b,c,d): #a,b = parameters passed during definition of function
    print(a+b+c+d)

sum(46,9,8,9) #arguments = actuall values supply during call of function """

#no of parameters = no of arguments
#no of parameters != no of arguments ==> positional arguments error

#take value from users and sum it
fn = int(input('Enter first no:'))
sn = int(input('Enter second no:'))

def sum(a,b):
    return a+b

print(sum(fn,sn))