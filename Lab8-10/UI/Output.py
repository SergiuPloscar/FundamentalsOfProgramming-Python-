'''
Created on 28 nov. 2017

@author: SergiuP
'''
def printNumber(n):
    print(n)
def printFile(l):
    try:
        fout=open("C://Users/SergiuP/eclipse-workspace/Lab8/DataOut.txt","a")
        fout.write(l)
        fout.close()
    except IOError as ex:
        print("Reading file errors",ex)