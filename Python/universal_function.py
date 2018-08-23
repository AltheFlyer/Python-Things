#UniversalFunction
#Allen Liu
#August 9, 2018
#A class for functions of any degree. And some Quadratic function utils

import math

#A Universal function that (should) be fit for any function of form:
#ax^n + bx^n-1 + cx^n-2 + ... + rx^2 + sx + t
#Works by recursively saving functions of lower degree
class UniversalFunction():

    #Arguments taken are the values of each coefficient,
    #from greatest to least degree
    def __init__(self, *args):
        #Get degree of function
        self.degree = len(args) - 1
        
        #a will be the value of the coefficient of the current degree
        self.a = args[0]

        #If degree isn't 0, creates another function 1 degree lower
        if (self.degree > 0):
            self.inner_function = UniversalFunction(*args[1:self.degree + 1])

    #Most of this is just string logic
    def __str__(self):
        if (self.degree == 0):
            if (self.a == 0):
                return ""
            else:
                return str(self.a)
        else:
            #Check the value of the coefficient of the current degree
            #Checks if = 0, if = 1, and if =-1
            #For a = 0, no string is shown
            #For a = 1, -1, only sign needs to be shown
            if (self.a == 0):
                high = ""
            elif (self.a == 1):
                high = "x"
            elif (self.a == -1):
                high = "-x"
            else:
                high = str(self.a) + "x"

            #Check the degree
            #Degree is not added if you wouldn't see it normally
            if (self.degree > 1 and self.a != 0):
                high += "^" + str(self.degree)

            #Add spacing, if the value exists
            if (self.a != 0):
                high += " "
        
            #Repeats until degree = 0
            end = self.inner_function.__str__()
            if (self.inner_function.a != 0 and end[0] != "-"):
                end = "+" + end
            return high + end

    #Function notation print
    def as_func(self):
        return "f(x) = " + self.__str__()
        
    #Recursion collects all of the values here
    def get_value(self, x):
        y = 0
        #When degree is 0, returns the constant
        if (self.degree == 0):
            y = self.a
        #Otherwise, get the value of the largest degree
        #Then get the values for each other degree recursively
        else:
            y = (self.a * x ** self.degree) + self.inner_function.get_value(x)
        return y

    #Print function table
    #Values inclusive
    def get_table(self, low, high):
        f = self.get_value
        out = ""
        out += "x\ty\n"
        for x in range(low, high + 1):
            #I just wanted function notation
            out += ("%d\t%.2f\n") % (x, f(x))
        return out

    #Check if quadratic
    def is_quadratic(self):
        return self.degree == 2
        
    #Get quadratic function, if degree is 2
    def as_quadratic(self):
        if (self.degree == 2):
            return QuadraticFunction(self.a, self.inner_function.a,
                                     self.inner_function.inner_function.a)
        else:
            return QuadraticFunction(0, 0, 0)

#Inheritance because why not
class QuadraticFunction(UniversalFunction):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.degree = 2
        self.inner_function = UniversalFunction(b, c)

    def get_discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def real_solutions(self):
        D = self.get_discriminant()
        if (D < 0):
            return 0
        elif (D == 0):
            return 1
        else:
            return 2
        
    def get_intercepts(self):
        D = self.get_discriminant()
        #Real intercepts
        if (D >= 0):
            positive = ((-1 * self.b + math.sqrt(D)) /
                    (2 * self.a))
            negative = ((-1 * self.b - math.sqrt(D)) /
                    (2 * self.a))
        #Imaginary intercepts
        else:
            positive = ComplexNumber(math.sqrt(-D) / (2 * self.a),
                    (-1 * self.b) / (2 * self.a))
            negative = ComplexNumber(-1 * math.sqrt(-D) / (2 * self.a),
                    (-1 * self.b) / (2 * self.a))
        return (str(positive), str(negative))        

#Complex numbers for quadratics
class ComplexNumber():

    def __init__(self, imaginary, real):
        self.imaginary = imaginary
        self.real = real

    #This is the only really important part
    def __str__(self):
        imag = ""
        if (self.imaginary == 0):
            return str(real)
        elif(self.imaginary == 1):
            imag = ""
        elif (self.imaginary == -1):
            imag = "-"
        else:
            imag = str(self.imaginary)
        imag += "i"
        return imag + ("" if self.real <= 0 else "+") + str(self.real)

class LinearFunction(UniversalFunction):

    def __init__(self, m, b):
        #Either a or m work for reference
        self.a = m
        self.m = m
        self.b = b
        self.degree = 1
        self.inner_function = UniversalFunction(b)

#Define the function
fun = UniversalFunction(-3, 0, 2)
print(fun.as_func())
print(fun.get_table(-5, 5))

quad = fun.as_quadratic()
print(quad.as_func())
print(quad.get_intercepts())
print(quad.real_solutions())

c = ComplexNumber(2.3, 5)
print(c)

line_a = LinearFunction(3, 1)
print(line_a.as_func())
print(line_a.get_table(-10, 10))

#User inputs
custom = UniversalFunction(*tuple(map(int, input("Enter values: ").split(' '))))
print(custom.as_func())
print(custom.get_table(-5, 5))
if (custom.is_quadratic):
    print("Quadratic!")
    print(custom.as_quadratic().get_intercepts())
