'''
Created on 28 nov. 2017

@author: SergiuP
'''
from UI.Input import read_input
from Domain.ComplexNumber import Complex
class ConsoleUI:
    ''' Prints the menu and runs the options chosen '''
    def __init__(self,ctrl):
        self.__ctrl = ctrl
    @staticmethod
    def printMenu():
        ''' Descr: Prints the option menu
        Data:
        Preconditions:
        Result: s
        Postcondition: s is the string that represents the menu
        '''
        s="\n Menu \n"
        s+="Choose an option \n "
        s+="\t 1.Add a complex number to the repository \n "
        s+="\t 2.Del a complex number from the repository at a given index \n  "
        s+="\t 3.Show the repository \n "
        s+="\t 4.Clear the repository \n "
        s+="\t 5.Show the cartesian form of the numbers in the repository\n "
        s+="\t 6.Show the polar form of the numbers in the repository \n "
        s+="\t 7.Show the conjugate of the numbers in the repository \n "
        s+="\t 8.Multiply the complex numbers by a real number\n "
        s+="\t 9.Multiply the complex numbers by an imaginary number \n "
        s+="\t 10.Add a complex number to all the other complex numbers \n "
        s+="\t 11.Multiply a complex number with all the other complex numbers \n "
        s+="\t 12.Show the matrix representation of all complex numbers in the repository \n "
        s+="\t 13.Raise all complex numbers to a power \n "
        s+="\t 14.Square root of all complex numbers \n "
        s+="\t 15.Exponential of all complex numbers \n "
        s+="\t 0.Exit"
        print(s)
    def menu(self):
        while True:
            ConsoleUI.printMenu()
            op=read_input()
            fout=open("C://Users/SergiuP/eclipse-workspace/Lab8/DataOut.txt","w")
            fout.close()
            if(op==0):
                exit()
            elif(op==1):
                print("Give the real and imaginary part of the complex number")
                real=read_input()
                imag=read_input()
                try:
                    self.__ctrl.CreateNumber(real,imag)
                except ValueError:
                    print("Give numbers please")
            elif(op==2):
                print("Give index")
                index=read_input()
                self.__ctrl.DelIndex(index)
            elif(op==3):
                self.__ctrl.PrintAll()
            elif(op==4):
                self.__ctrl.Clear()
            elif(op==5):
                self.__ctrl.CartesianForm()
            elif(op==6):
                self.__ctrl.PolarForm()
            elif(op==7):
                self.__ctrl.Conjugate()
            elif(op==8):
                print("Give a number")
                real=read_input()
                self.__ctrl.MultiplyReal(real)
            elif(op==9):
                print("Give a number")
                imag=read_input()
                self.__ctrl.MultiplyImaginary(imag)
            elif(op==10):
                print("Give the real and imaginary part of the complex number")
                real=read_input()
                imag=read_input()
                self.__ctrl.AddComplex(Complex(real,imag))
            elif(op==11):
                print("Give the real and imaginary part of the complex number")
                real=read_input()
                imag=read_input()
                self.__ctrl.MultiplyComplex(Complex(real,imag))
            elif(op==12):
                self.__ctrl.Matrix()
            elif(op==13):
                print("Give power")
                power=read_input()
                self.__ctrl.Power(power)
            elif(op==14):
                self.__ctrl.SquareR()
            elif(op==15):
                self.__ctrl.Exponential()
    
            