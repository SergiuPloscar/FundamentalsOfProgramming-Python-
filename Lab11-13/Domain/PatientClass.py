
'''
Created on 12 dec. 2017

@author: SergiuP
'''
class Patient:
    def __init__(self,fname="",lname="",code="",disease=""):
        self.__firstname=fname
        self.__lastname=lname
        self.__numcode=code
        self.__disease=disease
        if len(self.__numcode)!=13 :
            raise ValueError
        for letter in self.__numcode:
            a=int(letter)
        if int(self.__numcode[0])>=3 or int(self.__numcode[0])<1 :
            raise ValueError
        a=int(self.__numcode[3])*10 + int(self.__numcode[4])
        if a<1 or a>12 :
            raise ValueError
        a=int(self.__numcode[5])*10 + int(self.__numcode[6])
        if a<1 or a>31 :
            raise ValueError
    def getFirstName(self):
        return self.__firstname
    def getLastName(self):
        return self.__lastname
    def getNumericCode(self):
        return self.__numcode
    def getDisease(self):
        return self.__disease
    def setFirstName(self,fname):
        self.__firstname=fname
    def setLastName(self,lname):
        self.__lastname=lname
    def setNumericCode(self,code):
        self.__numcode=code
    def setDisease(self,disease):
        self.__disease=disease
    def __str__(self):
        s=self.__firstname+" "+self.__lastname+ " with the numeric code: "+self.__numcode+ " suffering of " +self.__disease
        return s