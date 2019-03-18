'''
Created on 31 oct. 2017

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
    s+="\t 1.Add a new value at the end of the list \n "
    s+="\t 2.Insert a new value at a given index \n  "
    s+="\t 3.Remove the value at the given index \n "
    s+="\t 4.Remove the values from index1 to index2 \n "
    s+="\t 5.Change a value at a given index \n "
    s+="\t 6.Print the participants with a score of less than a value \n "
    s+="\t 7.Print the participants in descendant order by score \n "
    s+="\t 8.Print the participants in descendant order by score if it it greater than a given value \n "
    s+="\t 9.Test all assertions \n "
    s+="\t 10.See your change \n "
    s+="\t 11.Calculate the average of the scores from an index to another \n"
    s+="\t 12.Calculate the minimum of the scores from an index to another \n"
    s+="\t 13.Print the scores that are a multiple of a given value from one index to another \n"
    s+="\t 14.Leave only the scores in a list that are a multiple of a given value \n"
    s+="\t 15.Leave only the scores in a list that are a greater than a given value \n"
    s+="\t 16.Undo \n" 
    s+="\t 0.Stop \n "
    print(s)
    
def print_list(l):
    ''' Descr: Prints a list
        Data: l
        Preconditions: l is a list of n
        Result:
        Postconditions:
    '''
    print("Your list is         ",l)