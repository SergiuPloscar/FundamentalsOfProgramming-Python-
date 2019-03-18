'''
Created on 19 dec. 2017

@author: SergiuP
'''
from unittest import TestCase,main
from Domain.PatientClass import Patient
class PatientTest(TestCase):
    def test_patient(self):
        P1=Patient("Sergiu","Ploscar","1980709124933","Cold")
        self.assertEqual(P1.getFirstName(),"Sergiu")
        self.assertEqual(P1.getLastName(),"Ploscar")
        self.assertEqual(P1.getNumericCode(),"1980709124933")
        self.assertEqual(P1.getDisease(),"Cold")
        P1.setFirstName("Ana")
        P1.setLastName("Ioana")
        P1.setNumericCode("2980709125922")
        P1.setDisease("Cancer")
        self.assertEqual(P1.getFirstName(),"Ana")
        self.assertEqual(P1.getLastName(),"Ioana")
        self.assertEqual(P1.getNumericCode(),"2980709125922")
        self.assertEqual(P1.getDisease(),"Cancer")
        a=1
        try:
            P2=Patient("Ion","Vasile","19224","Cold")
        except ValueError:
            a=0
        self.assertEqual(a, 0)
        a=1
        try:
            P2=Patient("Ion","Vasile","19224a7891236","Cold")
        except ValueError:
            a=0
        self.assertEqual(a, 0)
        a=1
        try:
            P2=Patient("Ion","Vasile","3980709124933","Cold")
        except ValueError:
            a=0
        self.assertEqual(a, 0)
        a=1
        try:
            P2=Patient("Ion","Vasile","3981309124933","Cold")
        except ValueError:
            a=0
        self.assertEqual(a, 0)
        a=1
        try:
            P2=Patient("Ion","Vasile","3980756124933","Cold")
        except ValueError:
            a=0
        self.assertEqual(a, 0)
if __name__=="__main__":
    main()
