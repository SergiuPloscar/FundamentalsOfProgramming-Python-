'''
Created on 12 dec. 2017

@author: SergiuP
'''
class Department:
    def __init__(self,name="",nr=0,nb=0,listp=[]):
        self.__name=name
        self.__number=nr
        self.__numberofbeds=nb
        self.__listofpatients=listp
    def getName(self):
        return self.__name
    def getNumber(self):
        return self.__number
    def getNumberOfBeds(self):
        return self.__numberofbeds
    def getListOfPatients(self):
        return self.__listofpatients
    def setName(self,name):
        self.__name=name
    def setNumber(self,nr):
        self.__number=nr
    def setNumberOfBeds(self,nb):
        self.__numberofbeds=nb
    def setListofPatients(self,listp):
        self.__listofpatients=listp
    def findPatientByNumericCode(self,code):
        for i in range (len(self.__listofpatients)):
            if(self.__listofpatients[i].getNumericCode()==code):
                return self.__listofpatients[i]
        return None
    def delPatientByNumericCode(self,code):
        for i in range(len(self.__listofpatients)-1,-1,-1):
            if(self.__listofpatients[i].getNumericCode()==code):
                del self.__listofpatients[i]
        return None 
                
    def __str__(self):
        s=self.__name+" "+str(self.__number)+" "+str(self.__numberofbeds)
        return s