#Rational Roots Theorem
#Python vr-3.7.x
#Numpy vr-1.17.2
#Matplotlib vr-3.1.1

import numpy as np
import matplotlib.pyplot as plt
import pandas
from math import *

class RationalRoots:

    #global FacListA
    #global FacListC
    #global PossibleRoots
    #global Roots
    
    #FacListA = []
    #FacListC = []
    #PossibleRoots = []
    #Roots = []

    #Function that declares the values of a, b, and c respectively
    def __init__(self, a, b, c):
        
        self.a = a
        self.b = b
        self.c = c

    #Takes the factors of A 
    def GetFactorsOfA(self, FacListA):
        self.FacListA = FacListA
        for y in range(1, abs(int(self.a)) + 1):
            if int(self.a) % y == 0:
                self.FacListA.append(y)
        return self.FacListA

    #Takes the factors of C
    def GetFactorsOfC(self, FacListC):
        self.FacListC = FacListC
        for y in range(1, abs(int(self.c)) + 1):
            if int(self.c) % y == 0:
                self.FacListC.append(y)
        return self.FacListC

    #Division Function for Factor List
    def FactorDivision(self, PossibleRoots):
        self.PossibleRoots = PossibleRoots
        for x in self.FacListC:
            for y in self.FacListA:
                Var = x / y
                if Var in self.PossibleRoots:
                    continue
                else:
                    self.PossibleRoots.append(Var)
                    self.PossibleRoots.append(Var * -1)

        return self.PossibleRoots

    #Checks for roots
    def RootCheck(self, Roots):


        '''Quadratic Formula used in case of irrational roots
        two values, one positive, and one negative'''
        try:
            self.QuadVarPos = (-1.0*(self.b) + sqrt(((self.b)**2.0)-(4.0*(self.a)*(self.c))))/(2.0*(self.a)) 

        except ValueError:
            print("No Real Roots")

        else:
            self.QuadVarPos= (-1.0*(self.b) + sqrt(((self.b)**2.0)-(4.0*(self.a)*(self.c))))/(2.0*(self.a)) 

        try: 
            self.QuadVarNeg = (-1.0*(self.b) - sqrt(((self.b)**2.0)-(4.0*(self.a)*(self.c))))/(2.0*(self.a))

        except ValueError:
            print("No Real Roots")

        else:
            self.QuadVarNeg = (-1.0*(self.b) - sqrt(((self.b)**2.0)-(4.0*(self.a)*(self.c))))/(2.0*(self.a)) 
   
        #Discriminant of Quadratic Formula
        self.QuadVarCheck = ((self.b**2) - (4*self.a*self.c))

       #Boolean Holder for logic tracking
        self.BoolHolder = False
        for x in self.PossibleRoots:


            '''Rational Roots Theorem is tested. The procedual approach
            takes in an argument from a polynomial of degree 2 and 3 terms'''
            self.RootVar = (float(self.a)*x**2) + (float(self.b) * x) + float(self.c)
            if self.RootVar == 0.0:
                self.Roots.append(x)
                self.BoolHolder = True
                print(x, "is a root.") 
        
        '''
        The initial value of x on the for loop is checked
        before the line is executed'''

        #Footnote: The Discriminant is checked on these lines

        if self.BoolHolder == False:
            
            if self.QuadVarCheck > 0.0:

                self.Roots.append(self.QuadVarPos)
                self.Roots.append(self.QuadVarNeg)
                print("Irrational Roots") 

            elif self.QuadVarCheck == 0.0:

                self.Roots.append(self.QuadVarPos)
                self.Roots.append(self.QuadVarNeg)
                print("One Root")

            elif self.QuadVarCheck < 0.0:
                print("No Real Roots") 

        return self.Roots




