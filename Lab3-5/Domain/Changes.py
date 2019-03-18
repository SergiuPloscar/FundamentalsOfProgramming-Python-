'''
Created on 31 oct. 2017

@author: SergiuP
'''
import GlobalList 
def test_add():
    assert add(98,[24,5,70])==[24,5,70,98]
    assert add(80,[])==[80]
    assert add(50,[40,50,50])==[40,50,50,50]
    assert add(24,[30])==[30,24]
    assert add(100,[20,100,10,4,25])==[20,100,10,4,25,100]
def add(score,l):
    ''' Descr: Adds a new value at the end of a list
        Data: score,l
        Preconditions: score is a natural number from 0 to 100 ,
                      l is a list of  natural numbers from 0 to 100 that can be empty
        Results: l
        Postcondition len(l) is greater by 1 and that new element is score
    '''
    
    GlobalList.prev_list=l[:]
    l.append(score)
    return l
def test_insert():
    assert insert(74,5,[20,50,20,11,100,40,80])==[20,50,20,11,100,74,40,80]
    assert insert(40,2,[0,50,20])==[0,50,40,20]
    assert insert(100,0,[])==[100]
    assert insert(20,1,[50])==[50,20]
    assert insert(30,3,[30,20,30,20])==[30,20,30,30,20]
def insert(score,index,l):
    ''' Descr: Inserts a new value at a given index
        Data score,index,l
        Preconditions: score is a natural number from 0 to 100 ,
                       index is a natural number from 0 to len(l)
                       l is a list of  natural numbers from 0 to 100 that can be empty
        Results: l
        Postcondition: len(l) is greater by 1 and that new element is score, positioned at the given index
    '''
    GlobalList.prev_list=l[:]
    if index>len(l):
        l.append(score)
    else:
        l.append(0)
        for i in range(len(l)-1,index,-1):
            l[i]=l[i-1]
        l[index]=score
    return l
def test_remove():
    assert remove(1,[10,20,30])==[10,30]
    assert remove(0,[100,20,30])==[20,30]
    assert remove(3,[20,10,90,20,50,60])==[20,10,90,50,60]
    assert remove(2,[10,20,30])==[10,20]
    assert remove(0,[50])==[]
def remove(index,l):
    ''' Descr: Removes the value at the given index
        Data index,l
        Preconditions: index is a natural number from 0 to len(l)-1
                       l is a list of  natural numbers from 0 to 100 that cannot be empty
        Result: l
        Postcondition: len(l) is smaller by 1 
    '''
    GlobalList.prev_list=l[:]
    try:
        del(l[index])
    except IndexError:
        print("Index is out of range")
    finally:
        return l
def test_remove_from():
    assert remove_from(1,3,[20,30,40,50])==[20]
    assert remove_from(2,3,[20,30,40,50])==[20,30]
    assert remove_from(0,1,[20,30,40,50,60])==[40,50,60]
    assert remove_from(1,1,[20,30,40])==[20,40]
    assert remove_from(0,1,[20,30])==[]
def remove_from(index1,index2,l):
    ''' Descr: Removes the values from index1 to index2 including those at index1 and index2
        Data: index1,index2,l
        Preconditions: index1 and index2 are natural numbers from 0 to len(l)-1
                       l is a list of  natural numbers from 0 to 100 that cannot be empty
                       index1 <= index2
        Result: l
        Postcondition: len(l) is smaller by index2-index1+1
    '''
    GlobalList.prev_list=l[:]
    for i in range(index2-index1+1):
        del(l[index1])
    return l
def test_replace_with():
    assert replace_with(0,100,[20,50])==[100,50]
    assert replace_with(2,50,[20,30,40])==[20,30,50]
    assert replace_with(0,10,[20])==[10]
    assert replace_with(1,40,[20,30,40])==[20,40,40]
    assert replace_with(2,100,[10,20,30,40])==[10,20,100,40]
def replace_with(index,score,l):
    ''' Descr: Changes a value at a given index
        Data: index,score,l
        Preconditions: index is a natural number from 0 to len(l)-1
                       score is a natural number from 0 to 100
                       l is a list of  natural numbers from 0 to 100 that cannot be empty
        Result: l
        Postcondition: len(l) is the same
    '''
    GlobalList.prev_list=l[:]
    try:
        l[index]=score
    except IndexError:
        print("Index is out of range")
    finally:
        return l
def test_filter_mul():
    assert filter_mul(10,[10,20,3])==[10,20]
    assert filter_mul(10,[1,2,3])==[]
    assert filter_mul(10,[10,20,30])==[10,20,30]
    assert filter_mul(10,[1,2,30])==[30]
    assert filter_mul(10,[10,2,3])==[10]
    
def filter_mul(mult,l):
    ''' Descr: Leaves only the scores in a list that are a multiple of a given value
        Data: mult,l
        Preconditions: mult is a natural number different from 0
                       l is a list of  natural numbers from 0 to 100 that cannot be empty
        Result: l
        Postcondition: the list <= elements than before
    '''
    GlobalList.prev_list=l[:]
    new_list=[]
    for i in range(len(l)):
        if(l[i]%mult!=0):
            new_list.append(i)
    for i in range(len(new_list)-1,-1,-1):
        del l[new_list[i]]
    return l   
def test_filter_greater_than():
    assert filter_greater_than(60,[20,70,30,80])==[70,80]
    assert filter_greater_than(60,[20,70,30,80,60])==[70,80]
    assert filter_greater_than(60,[20,10,30,50])==[]
    assert filter_greater_than(60,[120,70,130,80])==[120,70,130,80]
    assert filter_greater_than(60,[80])==[80]
def filter_greater_than(score,l):
    ''' Descr: Leaves only the scores in a list that are a greater than a given value
        Data: score,l
        Preconditions: score is a natural number different from 0 to 100
                       l is a list of  natural numbers from 0 to 100 that cannot be empty
        Result: l
        Postcondition: the list <= elements than before
    '''
    GlobalList.prev_list=l[:]
    new_list=[]
    for i in range(len(l)):
        if(l[i]<=score):
            new_list.append(i)
    for i in range(len(new_list)-1,-1,-1):
        del l[new_list[i]]
    return l   
def Undo(l):
    ''' Descr: Undoes the last operation
        Data: l
        Preconditions: l is a list of  natural numbers from 0 to 100
        Result: l
        Postcondition: 
    '''
    l=GlobalList.prev_list[:]
    return l
    