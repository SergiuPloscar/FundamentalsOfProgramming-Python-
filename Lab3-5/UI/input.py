'''
Created on 31 oct. 2017

@author: SergiuP
'''
def read_input():
    ''' Descr: Reads a natural number from console
        Data: 
        Preconditions:
        Result: n
        Postcondition: n is a natural number
    '''
    while True:
        try : 
            n=int(input())
            return n
        except ValueError :
            print("Please enter a number ")
def create_list(n):
    ''' Descr: Creates a list of natural numbers
        Data: n
        Preconditions: n is a natural number
        Result: my_list
        Postcondition: my_list is a list of natural numbers from 0 to 100
    '''
    my_list=[]
    print(" Enter the scores of the participants one by one, pressing enter after each number ")
    for i in range (n):
        my_list.append(read_input())
    return my_list     