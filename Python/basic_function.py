#BasicFunction.py
#Allen Liu
#August 9, 2018
#Using python classes/functions to make a mathematical function like thing

#Does not obey order of operations
#A simple function of form mx + b
class LinearFunction():

    def __init__(self, coeff, const):
        self.coefficient = coeff
        self.constant = const

    def __str__(self):
        b = ""
        #No x included if coeff is 0
        if (self.coefficient == 0):
            mx = ""
            b = str(self.constant)
        #No need to show unecessary 1 as coeff
        elif (self.coefficient == 1):
            mx = "x"
            
        #-1 as coeff only shows the negative sign
        elif (self.coefficient == -1):
            mx = "-x"
        else:
            mx = str(self.coefficient) + "x"
            
        #Adds plus sign in from of positive values of b
        if (self.coefficient != 0):
            b = ("" if self.constant < 0 else "+") + str(self.constant)

        if (self.constant == 0):
            b = ""
            
        return mx + b

    def as_function(self):
        return "f(x) = " + self.__str__()

    def get_value(self, x):
        y = x * self.coefficient
        y += self.constant
        return y

class QuadraticFunction():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        #bx + c is a linear function
        self.linear = LinearFunction(b, c)

    def __str__(self):
        #linear function converts to string using LinearFunction class
        linear = str(self.linear)
        if (self.a == 0):
            a = ""
        elif (self.a == 1):
            a = "x^2"
        elif (self.a == -1):
            a = "-x^2"
        else:
            a = str(self.a) + "x^2"
        
        if (self.a != 0 and linear[0] != "-"):
            linear = "+" + linear

        return a + linear
    
    def as_function(self):
        return "f(x) = " + self.__str__()
    
    def get_value(self, x):
        y = self.a * x**2
        y += self.b * x
        y += self.c
        return y
"""
#Create Linear Function    
fun = LinearFunction(int(input("Enter Coefficient: ")),
                     int(input("Enter Constant: ")))
print(fun)

#Create method object
#Calling f is equivalent to calling the function
f = fun.get_value

low = int(input("Enter lowest value of x: "))
high = int(input("Enter highest value of x: "))
#Table of values:
print("x\ty")
for x in range(low, high + 1):
    #Yes, I did all of that to make somthing print f(x) literally
    print("%d\t%.2f" % (x, f(x)))
"""

#Now for quadratics:
quad = QuadraticFunction(int(input("Enter a: ")),
        int(input("Enter b: ")),
        int(input("Enter c: ")))
print(quad)
print(quad.as_function())

f = quad.get_value

low = int(input("Enter lowest value of x: "))
high = int(input("Enter highest value of x: "))
#Table of values:
print("x\ty")
for x in range(low, high + 1):
    #Yes, I did all of that to make somthing print f(x) literally
    print("%d\t%.2f" % (x, f(x)))
