'''
Created on 31 oct. 2017

@author: SergiuP
'''
import Domain.Changes
import UI.output
import GlobalList
def test_mul_from_to():
    assert mul_from_to(10,0,2,[10,20,45,30])==[10,20]
    assert mul_from_to(2,0,2,[10,20,44,30])==[10,20,44]
    assert mul_from_to(5,0,2,[12,23,44,30])==[]
    assert mul_from_to(10,0,3,[10,20,45,30])==[10,20,30]
    assert mul_from_to(1,0,2,[10,20,45,30])==[10,20,45]
def mul_from_to(mult,index1,index2,l):
    ''' Descr: Returns the list of scores from one index to another, that are a multiple of a given value
        Data: mult,index1,index2,l
        Preconditions: mult is a natural number, mult!=0
                       index1<=index2
                       l cannot be an empty list
        Result: new_list
        Postconditions: the length of new_list<=the length of l
    '''
    new_list=[]
    if index1<0 or index2>=len(l) or index2 < index1 :
        print("Wrong indexes")
    else :
        for i in range(index1,index2+1):
            if l[i]%mult==0:
                new_list.append(l[i])
        return new_list
    
    
def test_min_from_to():
    assert min_from_to(0, 2, [90,20,15,60])==15
    assert min_from_to(1, 1, [90,20,15,60])==20
    assert min_from_to(1, 3, [90,10,15,60])==10
    assert min_from_to(0, 0, [90])==90
    assert min_from_to(0, 3, [20,20,20,20])==20
def min_from_to(index1,index2,l):
    ''' Descr: Calculates the minimum of the scores from index1 to index2
        Data: index1,index2,l
        Preconditions: index1<=index2
                       l cannot be an empty list
        Result: min
        Postconditions: min >=0 
    '''
    if index1<0 or index2>=len(l) or index2 < index1 :
        print("Wrong indexes")
    else:
        return min(l[index1:index2+1])
def avg_from_to(index1,index2,l):
    ''' Descr: Calculates the average of the scores from index1 to index2
        Data: index1,index2,l
        Preconditions: index1<=index2
                       l cannot be an empty list
        Result: avrg
        Postconditions: avrg >=0
    '''
    avrg=0
    if index1<0 or index2>=len(l) or index2 < index1 :
        print("Wrong indexes")
    else :
        for i in range(index1,index2+1):
            avrg+=l[i]
        avrg=float(avrg/(index2-index1+1))
        return avrg
def test_avg_from_to():
    assert avg_from_to(0, 2, [10,10,10])==10.0
    assert avg_from_to(0, 2, [10,20,30,40])==20.0
    assert avg_from_to(0, 2, [10,20,30,40])==20.0 
    assert avg_from_to(1, 1, [10,30,40,50])==30.0
    assert avg_from_to(1, 2, [10,15,10,5])==12.5
def test_sorted():
    assert sorted([20,30,10,60])==[3,1,0,2]
    assert sorted([90,80,70,60])==[0,1,2,3]
    assert sorted([20,20,20,20])==[0,1,2,3]
    assert sorted([])==[]
    assert sorted([20])==[0]
def sorted(l):
    ''' Descr: From a list of natural numbers forms a new list with the indexes of the first list,
               sorted descdendingly by their value
        Data: l
        Precondition: l is a list of natural numbers from 0 to 100
        Result: new_list
        Postcondition: new list has the same length as l
    '''
    GlobalList.prev_list=l[:]
    new_list=[]
    maxim=0
    while(len(l)>0 and max(l)!=-1):
        maxim=max(l)
        for i in range(len(l)):
            if(l[i]==maxim):
                new_list.append(i)
                l[i]=-1
    return new_list
def test_sorted_and_greater_than():
    assert sorted_and_greater_than(50,[100,80,40])==[0,1]
    assert sorted_and_greater_than(50,[20,70,40,60,90])==[4,1,3]
    assert sorted_and_greater_than(50,[30,20,40])==[]
    assert sorted_and_greater_than(50,[100,80,60])==[0,1,2]
    assert sorted_and_greater_than(50,[])==[]
def sorted_and_greater_than(score,l):
    ''' Descr: From a given list of natural numbers it forms a new list with the indexes from the first list
               but sorted and only if the value at those indexes is greater than a given value
        Data: score,l
        Precondition: score is a natural number from 0 to 100
                      l is a list of such scores
        Result new_list
        Postcondition: new_list has a length <= than l
    '''
    sorted_list=sorted(l)
    new_list=[]
    for i in range(len(sorted_list)):
        if(GlobalList.prev_list[sorted_list[i]]>score):
            new_list.append(sorted_list[i])
    return new_list
    
def test_less_than():
    assert less_than(40,[20,30,50,60])==[0,1]
    assert less_than(100,[20,30,50,60,90])==[0,1,2,3,4]
    assert less_than(10,[20,30,50,60])==[]
    assert less_than(40,[])==[]
    assert less_than(99,[99,99,80,100])==[2]       
def less_than(score,l):
    ''' Descr: From a list of scores returns the list of indexes that have an associated score smaller than
               a given score
        Data: score,l
        Preconditions: score is a natural number from 0 to 100
                       l is a list of such scores that cannot be empty
        Result new_list
        Postcondition: The length of new_list <= than the length of l           
    '''
    new_list=[]
    for i in range(len(l)):
        if(l[i]<score):
            new_list.append(i)
    return new_list
def data_examples():
    ''' Descr: Runs some examples
        Data: 
        Preconditions:
        Result:
        Postconditions:
    '''
    ex_list=[]
    print("Examples of what the program can do: ")
    print("You have an empty list.Elements 20,10,30 will be added to the end of the list")
    Domain.Changes.add(20,ex_list)
    Domain.Changes.add(10,ex_list)
    Domain.Changes.add(30,ex_list)
    UI.output.print_list(ex_list)
    print("Element 50 will be inserted at position 1")
    Domain.Changes.insert(50, 1,ex_list)
    UI.output.print_list(ex_list)
    print("The value at index 2 will be deleted")
    Domain.Changes.remove(2, ex_list)
    UI.output.print_list(ex_list)
    print("Elements 68 and 100 will be added at the end of the list and element 55 will be inserted at position 4")
    Domain.Changes.add(68,ex_list)
    Domain.Changes.add(100,ex_list)
    Domain.Changes.insert(55, 4, ex_list)
    UI.output.print_list(ex_list)
    print("Elements at indexes from 0 to 2 will be deleted ")
    Domain.Changes.remove_from(0, 2, ex_list)
    UI.output.print_list(ex_list)
    print("The value at index 1 will be replaced with 99")
    Domain.Changes.replace_with(1, 99, ex_list)
    UI.output.print_list(ex_list)
    print("The list of indexes where the value is lower than 80 will be printed now ")
    UI.output.print_list(less_than(80, ex_list))
    GlobalList.prev_list=ex_list[:]
    print("The list of indexes sorted descendingly by value will be printed now")
    UI.output.print_list(sorted(ex_list))
    ex_list=GlobalList.prev_list[:]
    print("The list of indexes sorted descendingly by value where the value is greater than 75 will be printed now")
    UI.output.print_list(sorted_and_greater_than(75,ex_list))
    ex_list=GlobalList.prev_list[:]
    print("Elements 61,19,24 will be added to the end of the list")
    Domain.Changes.add(61,ex_list)
    Domain.Changes.add(19,ex_list)
    Domain.Changes.add(24,ex_list)
    UI.output.print_list(ex_list)
    print("The average of the scores from index 0 to index 3 will be printed now ")
    print(avg_from_to(0, 3, ex_list))
    print("The smallest score from index 1 to index 4 will be printed now")
    print(min_from_to(1, 4, ex_list))
    print("The list of scores from index 1 to index 3 which are a multiple of 10 will be printed now")
    UI.output.print_list(mul_from_to(10,1,3,ex_list))
    print("The values that are not even will be removed")
    Domain.Changes.filter_mul(2, ex_list)
    UI.output.print_list(ex_list)
    print("The values smaller than 30 will be removed")
    GlobalList.prev_list=ex_list[:]
    Domain.Changes.filter_greater_than(30, ex_list)
    UI.output.print_list(ex_list)
    print("The last operation will be undone")
    UI.output.print_list(Domain.Changes.Undo(ex_list))
    
def run_assertions():
    ''' Descr: Runs all assertions
        Data: 
        Preconditions:
        Result:
        Postconditions:
    '''
    Domain.Changes.test_add()
    Domain.Changes.test_insert()
    test_less_than()
    Domain.Changes.test_remove()
    Domain.Changes.test_remove_from()
    Domain.Changes.test_replace_with()
    test_sorted()
    test_sorted_and_greater_than()
    test_min_from_to()
    test_mul_from_to()
    test_avg_from_to()
    Domain.Changes.test_filter_mul()
    Domain.Changes.test_filter_greater_than()

