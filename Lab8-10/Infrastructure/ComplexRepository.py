'''
Created on 28 nov. 2017

@author: SergiuP
'''

class Repository:
    ''' Keeps a list of complex numbers '''
    def __init__(self):
        self.__data=[]
    def addComplex(self,c):
        self.__data.append(c)
    def delIndex(self,index):
        ''' Descr: Deletes the complex number at the given index
            Data: index
            Preconditions: index is an integer number
            Result: 
            Postcondition: 
        '''
        if index >=0 and index <=len(self.__data):
            del self.__data[index]
        else:
            raise IndexError
    def delAll(self):
        ''' Descr: Deletes all the complex numbers in the list
            Data: 
            Preconditions: 
            Result: 
            Postcondition: 
        '''
        self.__data.clear()
    def getAll(self):
        ''' Descr: Returns all the complex numbers in the list
            Data: 
            Preconditions: 
            Result: 
            Postcondition: 
        '''
        return self.__data
    def getIndex(self,index):
        ''' Descr: Returns the complex number at the given index
            Data: index
            Preconditions: index is an integer number
            Result: 
            Postcondition: 
        '''
        if index >=0 and index <=len(self.__data):
            return self.__data[index]
        else:
            raise IndexError
    def __str__(self):
        for i in range (len(self.__data)):
            print(self.__data[i])
    def getLength(self):
        ''' Descr: Returns the number of complex numbers in the list
            Data: 
            Preconditions: 
            Result: 
            Postcondition: 
        '''
        return len(self.__data)