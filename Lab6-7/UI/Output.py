'''
Created on 14 nov. 2017

@author: SergiuP
'''
def print_menu():
    ''' Descr: Prints the option menu
        Data:
        Preconditions:
        Result: s
        Postcondition: s is the string that represents the menu
    '''
    s="\n Menu \n"
    s+="Choose an option \n "
    s+="\t 1.Change your 2D vector \n "
    s+="\t 2.Add a scalar to your 2D vector \n  "
    s+="\t 3.Add two 2D vectors \n "
    s+="\t 4.Substract two 2D vectors \n "
    s+="\t 5.Multiply two 2D vectors \n "
    s+="\t 6.See the sum of elements in your 2D vector \n "
    s+="\t 7.See the product of elements in your 2D vector\n "
    s+="\t 8.See the average of elements in your 2D vector \n "
    s+="\t 9.See the minimum of elements in your 2D vectors \n "
    s+="\t 10.See the maximum of elements in your 2D vector \n "
    s+="\t 11.See your vector \n "
    s+="\t 12.Run your assertions \n "
    s+="\t 13.Add a scalar using numpy \n"
    s+="\t 14.Add two 2D vectors using numpy \n"
    s+="\t 15.Substract two 2D vectors using numpy \n"
    s+="\t 16.Multiply two 2D vectors using numpy \n"
    s+="\t 17.See the sum of the elements of the 2D vector using numpy \n"
    s+="\t 18.See the product of the elements of the 2D vector using numpy \n"
    s+="\t 19.See the average of the elements of the 2D vector using numpy \n"
    s+="\t 20.See the minimum of the elements of the 2D vector using numpy \n"
    s+="\t 21.See the maximum of the elements of the 2D vector using numpy \n"
    s+="\t 0.Exit menu \n "
    print(s)
    
def print_2Dvector(l):
    ''' Descr: Prints a list
        Data: l
        Preconditions: l is a list of n
        Result:
        Postconditions:
    '''
    print("Your 2D vector is         ",l)
