'''
Created on 12 dec. 2017

@author: SergiuP
'''
from Domain.DepartmentClass import Department
class DepartmentRepository:
    def __init__(self):
        self.__datalist=[]
    def CreateDepartment(self,name,nr,nb,listp):
        D=Department(name,nr,nb,listp)
        return D
    def AddDepartment(self,D):
        if self.FindByNr(D.getNumber())==None:
            self.__datalist.append(D)
    def FindByNr(self,nr):
        for elem in self.__datalist:
            if elem.getNumber()==nr:
                return elem
        return None
    def DelByNr(self,nr):
        for i in range(len(self.__datalist)-1,-1,-1):
            if(self.__datalist[i].getNumber==nr):
                del self.__datalist[i]
    def UpdateAtNr(self,nr,name,nb,listp):
        for i in range(len(self.__datalist)):
            if(self.__datalist[i].getNumber()==nr):
                self.__datalist[i].setName(name)
                self.__datalist[i].setNumberOfBeds(nb)
                self.__datalist[i].setListOfPatients(listp)
                
    def getDatalist(self):
        return self.__datalist
    def setDatalist(self,l):
        self.__datalist=l
    def __getitem__(self,index):
        return self.__datalist[index]
    def __setitem__(self,index,a):
        self.__datalist[index]=a
        return self.__datalist[index]
                    