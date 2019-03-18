'''
Created on 12 dec. 2017

@author: SergiuP
'''
from Utils.Sort_Search_Bt import isSorted,isSearched
from Utils.Functions import numcode_comparison, departments_comparison, patients_comparison, nr_of_patients_age_comparison, find_by_age
from Utils.Functions import find_by_string, find_by_fname
from UI.Output import printlist
from Infrastructure.DRepository import DepartmentRepository

class ControllerClass:
    def __init__(self,prepo,drepo):
        self.__patientrepo=prepo
        self.__departmentrepo=drepo
    def AddPatientAtDepartment(self,fname,lname,code,disease,nr):
        P=self.__patientrepo.CreatePatient(fname,lname,code,disease)
        if P !=None:
            self.__patientrepo.AddPatient(P)
            ok=1
            for i in range (len(self.__departmentrepo.getDatalist())):
                if(self.__departmentrepo.getDatalist()[i].getNumber()==nr):
                    ok=0
                    if(self.__departmentrepo.getDatalist()[i].findPatientByNumericCode(code)==None):
                        if(self.__departmentrepo.getDatalist()[i].getNumberOfBeds()>len(self.__departmentrepo.getDatalist()[i].getListOfPatients())):
                            l=self.__departmentrepo.getDatalist()[i].getListOfPatients()
                            l.append(P)
                            self.__departmentrepo.getDatalist()[i].setListofPatients(l)
                            return 0
                        else:
                            return 4
                    else:
                        return 1
            if(ok==1):
                return 2
        else:
            return 3
                
    def DelPatientAtDepartment(self,code,nr):
        for i in range (len (self.__departmentrepo.getDatalist())):
            if(self.__departmentrepo.getDatalist()[i].getNumber()==nr):
                self.__departmentrepo.getDatalist()[i].delPatientByNumericCode(code)
    def CreateDepartmentC(self,name,nr,nrbeds,listp):
        return self.__departmentrepo.CreateDepartment(name,nr,nrbeds,listp)
    def CreatePatientC(self,fname,lname,numcode,disease):
        return self.__patientrepo.CreatePatient(fname,lname,numcode,disease)
    def AddDepartmentC(self,D):
        self.__departmentrepo.AddDepartment(D)
    def DelDepartmentC(self,nr):
        self.__departmentrepo.DelByNr(nr)
    def AddPatientC(self,P):
        self.__patientrepo.AddPatient(P)
    def DelPatientC(self,code):
        self.__patientrepo.DelByNumericCode(code)
    def SortByNC(self):
        for i in range(len(self.__departmentrepo.getDatalist())):
            self.__departmentrepo.getDatalist()[i].setListofPatients(isSorted(self.__departmentrepo.getDatalist()[i].getListOfPatients(),numcode_comparison, 0))
    def SortByNrOfPatientsAboveAge(self,a):
        isSorted(self.__departmentrepo.getDatalist(), nr_of_patients_age_comparison, a)
    def SortDepartamentsAndPatients(self):
        isSorted(self.__departmentrepo.getDatalist(), departments_comparison,0)
        for i in range(len(self.__departmentrepo.getDatalist())):
            self.__departmentrepo.getDatalist()[i].setListofPatients(isSorted(self.__departmentrepo[i].getListOfPatients(),patients_comparison, 0))
    def FindByUnderAge(self,a):
        printlist(isSearched(self.__departmentrepo.getDatalist(),find_by_age,a))
    def FindByString(self,nr,string):
        if self.__departmentrepo.FindByNr(nr)!=None:
            printlist(isSearched(self.__departmentrepo.FindByNr(nr).getListOfPatients(),find_by_string,string))
        else:
            raise IndexError
    def FindByFname(self,a):
        printlist(isSearched(self.__departmentrepo.getDatalist(),find_by_fname,a))          
    def PrintPatients(self):
        printlist(self.__patientrepo.getData())
    def PrintDepartments(self):
        printlist(self.__departmentrepo.getDatalist())
    def PrintAtDepartment(self,nr):
        if self.__departmentrepo.FindByNr(nr)!=None:
            printlist(self.__departmentrepo.FindByNr(nr).getListOfPatients())
        else:
            raise IndexError
        
                    
                
                    
    
            