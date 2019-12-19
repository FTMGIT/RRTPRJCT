import kivy
kivy.require('1.11.1')
import math
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from mpl_toolkits.axes_grid.axislines import SubplotZero
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from RationalTheorem import *

import matplotlib.pyplot as plt
import numpy as np

class MyGrid(GridLayout):

    Builder.load_file('rrt2.kv')

    FacListC = []
    FacListA = []
    PossibleRoots = []
    Roots = []
    storeA = 0
    storeB = 0
    storeC = 0
    digits = 0

    def Polynomial(self):

        try:
            self.a = float(self.a1.text)
            self.b = float(self.b1.text)
            self.c = float(self.c1.text)

        except ValueError:
            print('There must be an input on all three boxes')
        try:
            RationalRoots(self.a, self.b, self.c)
            RationalRoots.GetFactorsOfC(self, self.FacListC)
            RationalRoots.GetFactorsOfA(self, self.FacListA)
            RationalRoots.FactorDivision(self, self.PossibleRoots)
            RationalRoots.RootCheck(self, self.Roots)

            self.factorsOfC.text = str(self.FacListC)
            self.factorsOfA.text = str(self.FacListA)
            self.possibleRoots.text = str(self.PossibleRoots)
            self.roots.text = str(self.Roots)

        except ZeroDivisionError:
            self.d1.text = "Linear Equation, Zero \"a\" input"

        return self.a, self.b, self.c

    def listlength(self):
        length_check = len()

    def dign(self, n):

        if int(n) > 0:
            digits = int(math.log10(int(n))) - 1

        elif int(n) == 0:
            digits = 1

        elif int(n) < 0:
            digits = int(math.log10(int(-n))) - 1
        return digits


    def ShowPolynomial(self):
        try:
            self.d1.text = str(self.a) + "x^2 " + "+ " + str(self.b) + "x " + "+ " + str(self.c)
            return self.d1.text
        except AttributeError:
            print('test')


    def ClearAll(self):

        self.a1.text = ''
        self.b1.text = ''
        self.c1.text = ''

        self.FacListC.clear()
        self.FacListA.clear()
        self.PossibleRoots.clear()
        self.Roots.clear()

    def StoreVariables(self):

        try:
            self.storeA = self.a1.text
            self.storeB = self.b1.text
            self.storeC = self.c1.text
            print(self.storeA, self.storeB, self.storeC)

        except TypeError:
            print('TypeError on StoreVariables')

    def ShowGraph(self):



        try:

            #self.storeA = self.a1.text
            #self.storeB = self.b1.text
            #self.storeC = self.c1.text

            self.firstdig = str(abs(int(self.storeC)))

            self.d1 = self.dign(int(self.storeC))

            self.varn = int(self.firstdig[0]) * 10**self.d1

            x = np.linspace(-self.varn * 6, self.varn * 6, 100)
            y = int(self.storeA) * x**2 + int(self.storeB) * x + int(self.storeC)

            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('zero')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')

            plt.plot(x, y, 'r')
            plt.show()

        except TypeError:

            self.firstdig = str(abs(int(self.c1.text)))

            self.d1 = self.dign(int(self.c1.text))

            self.varn = int(self.firstdig[0]) * 10**self.d1

            x = np.linspace(-self.varn * 6, self.varn * 6, 100)
            y = int(self.a1.text) * x**2 + int(self.b1.text) * x + int(self.c1.text)

            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('zero')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')

            plt.plot(x, y, 'r')
            plt.show()


class MainScreen(Screen):
    pass

class CalculatorScreen(Screen):
    pass

class GraphScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file('screensetup.kv')

class MyApp(App):
    def build(self):
        return presentation


if __name__ == '__main__':
    MyApp().run()