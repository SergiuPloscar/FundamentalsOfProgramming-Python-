'''
Created on 19 dec. 2017

@author: SergiuP
'''
from unittest import TestCase,main
from Domain.PatientClass import Patient
from Infrastructure.PRepository import PatientRepository
class PRepositoryTests(TestCase):
    def test_prepository(self):
        repo=PatientRepository()
        