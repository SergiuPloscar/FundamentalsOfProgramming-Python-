'''
Created on 28 nov. 2017

@author: SergiuP
'''
from Infrastructure.ComplexRepository import Repository
from Application.ComplexController import ComplexNumberController
def read_input():
    ''' Descr: Reads a natural number from console
        Data: 
        Preconditions:
        Result: n
        Postcondition: n is a natural number
    '''
    while True:
        try : 
            n=int(input())
            return n
        except ValueError :
            print("Please enter a number ")
def read_file():
    repo=Repository()
    ctrl=ComplexNumberController(repo)
    try:
        fin=open("C://Users/SergiuP/eclipse-workspace/Lab8/DataIn.txt","r")
        for line in fin:
            s=line.split()
            a=None
            b=None
            try:
                a=int(s[0])
                b=int(s[1])
            except Exception:
                pass
            finally:
                if(a!=None and b!= None):
                    ctrl.CreateNumber(a,b)
        fin.close()
        return ctrl                
    except IOError as ex:
        print("Reading file errors",ex)
    