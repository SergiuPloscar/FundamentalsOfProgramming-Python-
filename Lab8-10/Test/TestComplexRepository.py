'''
Created on 28 nov. 2017

@author: SergiuP
'''
from unittest import  TestCase,main
from Infrastructure.ComplexRepository import Repository
from Domain.ComplexNumber import Complex
class ComplexRepositoryTests(TestCase):
    def test_addComplex(self):
        s=Repository()
        c=Complex(3,4)
        s.addComplex(c)
        self.assertEqual(s.getLength(),1)
        s=Repository()
        c=Complex(4)
        s.addComplex(c)
        self.assertEqual(s.getLength(),1)
        s=Repository()
        c=Complex()
        s.addComplex(c)
        self.assertEqual(s.getLength(),1)
        
    def test_delIndex(self):
        s=Repository()
        c=Complex(3,2)
        c1=Complex(4,5)
        c2=Complex(-1,3)
        s.addComplex(c)
        s.addComplex(c1)
        s.addComplex(c2)
        s.delIndex(0)
        self.assertEqual(s.getLength(),2)
        try : 
            s.delIndex(5)
        except IndexError:
            assert True
    def test_delAll(self):
        s=Repository()
        c=Complex(3,2)
        c1=Complex(4,5)
        c2=Complex(-1,3)
        s.addComplex(c)
        s.addComplex(c1)
        s.addComplex(c2)
        s.delAll()
        self.assertEqual(s.getLength(),0)
if __name__== "__main__" :
    main()