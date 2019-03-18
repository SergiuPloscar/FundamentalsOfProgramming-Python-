'''
Created on 19 dec. 2017

@author: SergiuP
'''
from unittest import TestCase,main
from Domain.DepartmentClass import Department
from Domain.PatientClass import Patient
class DepartmentTest(TestCase):
    def test_getset(self):
        P1=Patient("Sergiu","Ploscar","1980709124933","Cold")
        l=[]
        l.append(P1)
        D1=Department("Psychology",1,5,l)
        self.assertEqual(D1.getName(),"Psychology")
        self.assertEqual(D1.getNumber(),1)
        self.assertEqual(D1.getNumberOfBeds(),5)
        self.assertEqual(D1.getListOfPatients(),l)
        D1.setName("Children's ward")
        D1.setNumber(3)
        D1.setNumberOfBeds(7)
        D1.setListofPatients([])
        self.assertEqual(D1.getName(),"Children's ward")
        self.assertEqual(D1.getNumber(),3)
        self.assertEqual(D1.getNumberOfBeds(),7)
        self.assertEqual(D1.getListOfPatients(),[])
    def test_find(self):
        P1=Patient("Sergiu","Ploscar","1980709124933","Cold")
        P2=Patient("Ana","Ioana","2980709124155","Cancer")
        P3=Patient("Ion","Cornel","1780205341555","Ebola")
        l=[]
        l.append(P1)
        l.append(P2)
        l.append(P3)
        D1=Department("Psychology",1,5,l)
        self.assertEqual(D1.findPatientByNumericCode("1980709124933"),P1)
        self.assertEqual(D1.findPatientByNumericCode("1780205341555"),P3)
        self.assertEqual(D1.findPatientByNumericCode("1780205321555"),None)
    def test_del(self):
        P1=Patient("Sergiu","Ploscar","1980709124933","Cold")
        P2=Patient("Ana","Ioana","2980709124155","Cancer")
        P3=Patient("Ion","Cornel","1780205341555","Ebola")
        l=[]
        l.append(P1)
        l.append(P2)
        l.append(P3)
        D1=Department("Psychology",1,5,l)
        D1.delPatientByNumericCode("1980709124933")
        self.assertEqual(D1.findPatientByNumericCode("1980709124933"),None)
        D1.delPatientByNumericCode("1242425353556")
        self.assertEqual(len(D1.getListOfPatients()),2)
    
if __name__=="__main__":
    main()