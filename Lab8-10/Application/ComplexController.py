'''
Created on 28 nov. 2017

@author: SergiuP
'''
from Domain.ComplexNumber import Complex
from UI  import Output
class ComplexNumberController():
    ''' Controler for operations on the complex number list '''
    def __init__(self,repo):
        self.__repo=repo
    def CreateNumber(self,real=0,imag=0):
        ''' Descr: Creates a complex number and adds it to the list
            Data: real,imag
            Preconditions:  real and imag are both integer numbers
            Result: 
            Postcondition: 
        '''
        c=Complex(real,imag)
        self.__repo.addComplex(c)
    def Clear(self):
        ''' Descr: Empties the repository list
            Data: 
            Preconditions:  
            Result: 
            Postcondition: 
        '''
        self.__repo.delAll()
    def GetIndex(self,index):
        ''' Descr: Returns the complex number at the given index
            Data: index
            Preconditions: index is an integer number
            Result: 
            Postcondition: 
        '''
        try:
            self.__repo.getIndex(index)
        except IndexError:
            print(" The index given is not in the repository")
    def DelIndex(self,index):
        ''' Descr: Deletes the complex number at the given index
            Data: index
            Preconditions: index is an integer number
            Result: 
            Postcondition: 
        '''
        try:
            self.__repo.delIndex(index)
        except IndexError:
            print(" The index given is not in the repository")
    def PrintAll(self):
        ''' Descr: Returns all the complex numbers in the list
            Data: 
            Preconditions: 
            Result: 
            Postcondition: 
        '''
        for elem in self.__repo.getAll():
            Output.printNumber(elem)
    def CartesianForm(self):
        ''' Descr: Returns the cartesian form of all the complex numbers in the list
            Data: 
            Preconditions: 
            Result: 
            Postcondition: 
        '''
        for elem in self.__repo.getAll():
            s="real = " + str(elem.getReal())+" and imaginary = " + str(elem.getImaginary())
            Output.printFile(s+"\n")
            s=""
    def PolarForm(self):
        ''' Descr: Returns the polar form of all the complex numbers in the list
            Data: 
            Preconditions: 
            Result: 
            Postcondition: 
        '''
        for elem in self.__repo.getAll():
            s="modulus = " + str(elem.getModulus())+" and argument = " + str(elem.getArgument())
            Output.printFile(s+"\n")
            s=""
    def Conjugate(self):
        ''' Descr: Returns the conjugate of all the complex numbers in the list
            Data: 
            Preconditions: 
            Result: 
            Postcondition: 
        '''
        for elem in self.__repo.getAll():
            Output.printFile(str(elem.getConjugate())+"\n")
    def MultiplyReal(self,real):
        ''' Descr: Prints the result obtained by multiplying all complex numbers with a given real number
            Data:  real
            Preconditions: real is an integer number
            Result: 
            Postcondition: 
        '''
        for elem in self.__repo.getAll():
            Output.printFile(str(elem.MultiplyByReal(real))+"\n")
    def MultiplyImaginary(self,imag):
        ''' Descr: Prints the result obtained by multiplying all complex numbers with a given imaginary number
            Data:  imag
            Preconditions: imag is an integer number
            Result: 
            Postcondition: 
        '''
        for elem in self.__repo.getAll():
            Output.printFile(str(elem.MultiplyByImaginary(imag))+"\n")
    def AddComplex(self,other):
        ''' Descr: Prints the result obtained by adding all complex numbers to a given complex number
            Data:  other
            Preconditions: other is a complex number
            Result: 
            Postcondition: 
        '''
        for elem in self.__repo.getAll():
            Output.printNumber(elem.AddTwoComplexNumbers(other))
    def MultiplyComplex(self,other):
        ''' Descr: Prints the result obtained by multiplying all complex numbers with a given complex number
            Data:  other
            Preconditions: other is a complex number
            Result: 
            Postcondition: 
        '''
        for elem in self.__repo.getAll():
            Output.printNumber(elem.MultiplyTwoComplexNumbers(other))
    def Matrix(self):
        ''' Descr: Prints the matrix representation of all complex numbers
            Data:  
            Preconditions: 
            Result: 
            Postcondition:
        '''
        for elem in self.__repo.getAll():
            l=elem.MatrixRepresentation()
            print(l[0])
            print(l[1])
            print("")
    def Power(self,power):
        ''' Descr: Prints the power of all complex numbers
            Data:  power
            Preconditions: power is a natural number
            Result: 
            Postcondition:
        '''
        for elem in self.__repo.getAll():
            Output.printNumber(elem.PowerOfComplex(power))
    def SquareR(self):
        ''' Descr: Prints the square root of all complex numbers
            Data:  
            Preconditions: 
            Result: 
            Postcondition:
        '''
        for elem in self.__repo.getAll():
            Output.printNumber(elem.SquareRootOfComplex())
    def Exponential(self):
        ''' Descr: Prints the exponential of all complex numbers
            Data:  
            Preconditions: 
            Result: 
            Postcondition:
        '''
        for elem in self.__repo.getAll():
            Output.printNumber(elem.ExponentialOfComplex())