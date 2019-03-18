'''
Created on 21 nov. 2017

@author: SergiuP
'''
import math
class Complex :
    ''' A complex number is formed of two parts: a real part and an imaginary part '''
    def __init__(self,r=0,i=0):
        try :
            int(r)
            int(i)
            self.__real=r
            self.__imaginary=i
        except:
            raise ValueError
        
    def getReal(self):
        return self.__real
    def getImaginary(self):
        return self.__imaginary
    def setReal(self,r):
        self.__real=r
    def setImaginary(self,i):
        self.__imaginary=i
    def __str__(self):
        if(self.__real==0 and self.__imaginary==0):
            return "0"
        elif(self.__real !=0 and self.__imaginary==0):
            return str(self.__real)
        elif(self.__real==0 and self.__imaginary!=0):
            return str(self.__imaginary)+"i"
        elif(self.__imaginary>0):
            return str(self.__real) + "+" +str(self.__imaginary) + "i"
        else:
            return str(self.__real) + "-" +str((self.__imaginary*-1))+ "i"
    def getModulus(self):
        ''' Descr: Returns the modulus of a complex number
            Data: 
            Preconditions:
            Result: p
            Postcondition: p is float
        '''
        p=math.sqrt((self.__real**2)+(self.__imaginary**2))
        return p
    def getArgument(self):
        ''' Descr: Returns the argument of a complex number
            Data: 
            Preconditions:
            Result: a
            Postcondition: a is float
        '''
        if (self.__real==0):
            return 0.0
        else:
            a=math.acos(self.__real/self.getModulus())
            return a
    def getConjugate(self):
        ''' Descr: Returns the conjugate of a complex number
            Data: 
            Preconditions:
            Result: aux
            Postcondition: aux is a complex number
        '''
        aux=Complex(self.__real,self.__imaginary*-1)
        return aux
    def MultiplyByReal(self,r):
        ''' Descr: Returns the result obtained by multiplying a complex number with a given real number
            Data:  r
            Preconditions: r is an integer number
            Result: aux
            Postcondition: aux is a complex number
        '''
        aux=Complex(self.__real*r,self.__imaginary*r)
        return aux
    def MultiplyByImaginary(self,i):
        ''' Descr: Returns the result obtained by multiplying a complex number with a given imaginary number
            Data:  i
            Preconditions: i is an integer number
            Result: aux
            Postcondition: aux is a complex number
        '''
        aux=Complex((self.__imaginary*i)*-1,self.__real*i)
        return aux
    def AddTwoComplexNumbers(self,other):
        ''' Descr: Returns the result obtained by adding a complex number to another complex number
            Data:  other
            Preconditions: other is a complex number
            Result: aux
            Postcondition: aux is a complex number
        '''
        aux=Complex(self.__real+other.getReal(),self.__imaginary+other.getImaginary())
        return aux
    def MultiplyTwoComplexNumbers(self,other):
        ''' Descr: Returns the result obtained by multiplying two complex numbers
            Data:  other
            Preconditions: other is a complex number
            Result: aux
            Postcondition: aux is a complex number
        '''
        aux=Complex(((self.__real*other.getReal())+(self.__imaginary*other.getImaginary()*-1)),((self.__real*other.getImaginary())+(self.__imaginary*other.getReal())))
        return aux
    def MatrixRepresentation(self):
        ''' Descr: Returns the matrix representation of a complex number
            Data:  
            Preconditions: 
            Result: l
            Postcondition: l is a list of lists
        '''
        l1=[]
        l2=[]
        l1.append(self.__real)
        l1.append(self.__imaginary*-1)
        l2.append(self.__imaginary)
        l2.append(self.__real)
        l3=[l1,l2]
        return l3
    def PowerOfComplex(self,power):
        ''' Descr: Returns the given power of a complex number
            Data: power
            Preconditions: power is a natural number 
            Result: c
            Postcondition: c is a complex number
        '''
        if(power<0):
            raise ValueError
        elif(power==0):
            return Complex(1,0)
        else:
            c=Complex(1,0)
            copy=Complex(self.__real,self.__imaginary)
            for i in range (power):
                c=c.MultiplyTwoComplexNumbers(copy)
            return c
                
    def SquareRootOfComplex(self):
        ''' Descr: Returns the square root of a complex number
            Data: 
            Preconditions: 
            Result: c
            Postcondition: c is a complex number
        '''
        c=Complex(int(math.sqrt(self.getModulus()*math.cos(self.getArgument()/2),)),int(math.sqrt(self.getModulus()*math.sin(self.getArgument()/2))))
        return c
    def ExponentialOfComplex(self):
        ''' Descr: Returns the exponential of a complex number
            Data: 
            Preconditions: 
            Result: c
            Postcondition: c is a complex number
        '''
        a=math.cos(self.__imaginary)
        b=math.sin(self.__imaginary)
        c=Complex(a,b)
        d=1
        for i in range (self.__real):
            d=d*math.e
        c=c.MultiplyByReal(d)
        return c
        
                   
