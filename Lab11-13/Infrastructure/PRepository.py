'''
Created on 12 dec. 2017

@author: SergiuP
'''
from Domain.PatientClass import Patient
class PatientRepository:
    def __init__(self):
        self.__data=[]
    def CreatePatient(self,fname,lname,code,disease):
        try:
            P=Patient(fname,lname,code,disease)
            return P
        except ValueError:
            return None
        
    def AddPatient(self,P):
        if self.FindByNumericCode(P.getNumericCode())==None:
            self.__data.append(P)
    def DelByNumericCode(self,code):
        for i in range(len(self.__data)-1,-1,-1):
            if(self.__data[i].getNumericCode==code):
                del self.__data[i]
                    
    def FindByNumericCode(self,code):
        for elem in self.__data:
            if(elem.getNumericCode()==code):
                return elem
        return None  
    def UpdateAtNumericCod(self,code,fname,lname,disease):
        for i in range(len(self.__data)):
            if(self.__data[i].getNumericCode()==code):
                self.__data[i].setFirstName(fname)
                self.__data[i].setLastName(lname)
                self.__data[i].setDisease(disease)
    def getData(self):
        return self.__data