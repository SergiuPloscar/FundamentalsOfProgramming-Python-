'''
Created on 14 nov. 2017

@author: SergiuP
'''
import numpy as np
def test_turn_2d_into_numpy_matrix():
    assert [[1,2,3],[2,3,4],[3,4,5]]==turn_2d_into_numpy_matrix([[1,2,3],[2,3,4],[3,4,5]]).tolist()
    assert [[1,2,3]]==turn_2d_into_numpy_matrix([[1,2,3]]).tolist()
    try:
        assert [[1,2],[2,3,4],[3,4,5,6]]==turn_2d_into_numpy_matrix([[1,2],[2,3,4],[3,4,5,6]]).tolist()
    except IndexError:
        assert True
    try:
        assert [[]]==turn_2d_into_numpy_matrix([[]]).tolist()
    except IndexError:
        assert True
    try:
        assert [[1,1],[1,1],[1]]==turn_2d_into_numpy_matrix([[1,1],[1,1],[1]]).tolist()
    except IndexError:
        assert True
def turn_2d_into_numpy_matrix(v):
    ''' Descr: Turns a 2D vector into a Numpy matrix
        Data: v
        Preconditions: v is a non empty 2D vector and the vectors inside must all have the same lengths
        Results: a
        Postcondition: a is a numpy matrix
    '''
    if len(v)==0 or len(v[0])==0:
        raise IndexError
    for i in range (len(v)-1):
        if len(v[i])!=len(v[i+1]):
            raise IndexError
    a=np.matrix(v)
    return a
def test_add_scalar_numpy():
    assert add_scalar_numpy(turn_2d_into_numpy_matrix([[1,2],[2,3]]),1).tolist()==[[2,3],[3,4]]
    assert add_scalar_numpy(turn_2d_into_numpy_matrix([[1,2],[2,3]]),0).tolist()==[[1,2],[2,3]]
    assert add_scalar_numpy(turn_2d_into_numpy_matrix([[1,2],[2,3]]),-1).tolist()==[[0,1],[1,2]]
    try:
        assert add_scalar_numpy(turn_2d_into_numpy_matrix([[1,2],[2]]),1).tolist()==[[2,3],[3]]
    except IndexError:
        assert True
    try:
        assert add_scalar_numpy(turn_2d_into_numpy_matrix([[]]),1).tolist()==[[]]
    except IndexError:
        assert True
    
def add_scalar_numpy(v,scalar):
    ''' Descr: Adds a scalar to a numpy matrix
        Data: v,scalar
        Preconditions: v is a non empty numpy matrix
                       scalar is an integer
        Results: v
        Postcondition: 
    '''
    v+=scalar
    return v
def test_add_two_matrices():
    assert add_two_matrices([[1,2,3],[4,5,6]],[[4,5,6],[7,8,9]])==[[5,7,9],[11,13,15]]
    assert add_two_matrices([[1,1,1]],[[3,3,3]])==[[4,4,4]]
    try:
        assert add_two_matrices([[2,1,4],[4,7,8]],[[3,5,6]])==False
    except IndexError:
        assert True
    try:
        assert add_two_matrices([[2,1]],[[3,5,6]])==False
    except IndexError:
        assert True
    try:
        assert add_two_matrices([],[])==False
    except IndexError:
        assert True
def add_two_matrices(m1,m2):
    ''' Descr: Adds two 2D vectors using Numpy
        Data: m1,m2
        Preconditions: m1 and m2 are two 2D vectors that need to have the same length
                       the vectors they contain also need to have the same length
                       m1 and m2 cannot be empty
        Results: m3
        Postcondition: m3 cannot be empty
    '''
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
        raise IndexError

    m3=np.add(turn_2d_into_numpy_matrix(m1),turn_2d_into_numpy_matrix(m2))
    return m3.tolist()
def test_substract_two_matrices():
    assert substract_two_matrices([[1,2,3],[4,5,6]],[[4,5,6],[7,8,9]])==[[-3,-3,-3],[-3,-3,-3]]
    assert substract_two_matrices([[1,5,7]],[[3,3,3]])==[[-2,2,4]]
    try:
        assert substract_two_matrices([[2,1,4],[4,7,8]],[[3,5,6]])==False
    except IndexError:
        assert True
    try:
        assert substract_two_matrices([[2,1]],[[3,5,6]])==False
    except IndexError:
        assert True
    try:
        assert substract_two_matrices([],[])==False
    except IndexError:
        assert True
def substract_two_matrices(m1,m2):
    ''' Descr: Substracts two 2D vectors using Numpy
        Data: m1,m2
        Preconditions: m1 and m2 are two 2D vectors that need to have the same length
                       the vectors they contain also need to have the same length
                       m1 and m2 cannot be empty
        Results: m3
        Postcondition: m3 cannot be empty
    '''
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
        raise IndexError
    m3=np.subtract(turn_2d_into_numpy_matrix(m1),turn_2d_into_numpy_matrix(m2))
    return m3.tolist()
def test_multiply_two_matrices():
    assert multiply_two_matrices([[1,2,3],[10,12,23]],[[4,2],[1,2],[1,2]])==[[9,12],[75,90]]
    assert multiply_two_matrices([[1,2,3],[4,5,6]],[[7,8],[9,10],[11,12]])==[[58,64],[139,154]]
    try:
        assert multiply_two_matrices([[1],[2]],[[4,2],[1,2],[1,2]])==False
    except (ValueError,IndexError):
        assert True
    try:
        assert multiply_two_matrices([[1,2,3],[10,12,23]],[[2],[2]])==False
    except (ValueError,IndexError):
        assert True
    try:
        assert multiply_two_matrices([[]],[[4,2],[1,2],[1,2]])==False
    except (ValueError,IndexError):
        assert True
def multiply_two_matrices(m1,m2):
    ''' Descr: Multiplies two 2D vectors using Numpy
        Data: m1,m2
        Preconditions: m1 and m2 are two 2D vectors that need to have the same length
                       the vectors they contain also need to have the same length
                       m1 and m2 cannot be empty
        Results: m3
        Postcondition: m3 cannot be empty
    '''
    if len(m1)==0 or len(m2)==0 or len(m1[0])==0 or len(m2[0])==0:
        raise IndexError
    m3=np.dot(turn_2d_into_numpy_matrix(m1),turn_2d_into_numpy_matrix(m2),out=None)
    return m3.tolist()
def test_sum_elements_matrix():
    assert sum_elements_matrix([[2,3],[4,5]])==14
    assert sum_elements_matrix([[2,0],[-1,5]])==6
    assert sum_elements_matrix([[2]])==2
    try:                    
        assert sum_elements_matrix([[]])==False
    except IndexError:
        assert True
    try:
        assert sum_elements_matrix([])==False
    except IndexError:
        assert True
def sum_elements_matrix(m):
    ''' Descr: Finds the sum of all elements in a 2D vector using Numpy
        Data: m
        Preconditions: m is a non empty 2D vector
        Results: the sum as a result of a numpy function
        Postcondition
    '''
    if len(m)==0 or len(m[0])==0:
        raise IndexError
    m1=turn_2d_into_numpy_matrix(m)
    return m1.sum()
def test_product_elements_matrix():
    assert product_elements_matrix([[2,1],[3,2]])==12
    try:
        assert product_elements_matrix([])==False
    except IndexError:
        assert True
    assert product_elements_matrix([[3,-2]])==-6
    assert product_elements_matrix([[2,1],[3,0]])==0
    try:
        assert product_elements_matrix([[]])==False
    except IndexError:
        assert True
def product_elements_matrix(m):
    ''' Descr: Finds the product of all elements in a 2D vector using Numpy
        Data: m
        Preconditions: m is a non empty 2D vector
        Results: the product as a result of a numpy function
        Postcondition
    '''
    if len(m)==0 or len(m[0])==0:
        raise IndexError
    m1=turn_2d_into_numpy_matrix(m)
    return m1.prod()
def test_average_elements_matrix():
    assert average_elements_matrix([[1,2,3],[10,12,26]])==9
    assert average_elements_matrix([[1,2,3]])==2
    assert average_elements_matrix([[12]])==12
    try:
        assert average_elements_matrix([[]])==False
    except IndexError:
        assert True
    assert average_elements_matrix([[2,3]])==2.5
def average_elements_matrix(m):
    ''' Descr: Finds the average of all elements in a 2D vector using Numpy
        Data: m
        Preconditions: m is a non empty 2D vector
        Results: the average as a result of a numpy function
        Postcondition
    '''
    if len(m)==0 or len(m[0])==0:
        raise IndexError
    m1=turn_2d_into_numpy_matrix(m)
    return m1.mean()
def test_minimum_elements_matrix():
    assert minimum_elements_matrix([[2,1],[3,2]])==1
    try:
        assert minimum_elements_matrix([])==False
    except IndexError:
        assert True
    assert minimum_elements_matrix([[3,-2]])==-2
    assert minimum_elements_matrix([[0]])==0
    try:
        assert minimum_elements_matrix([[]])==False
    except IndexError:
        assert True
def minimum_elements_matrix(m):
    ''' Descr: Finds the minimum of all elements in a 2D vector
        Data: m
        Preconditions: m is a non empty 2D vector
        Results: the minimum as a result of a numpy function
        Postcondition:
    '''
    if len(m)==0 or len(m[0])==0:
        raise IndexError
    m1=turn_2d_into_numpy_matrix(m)
    return m1.min()
def test_maximum_elements_matrix():
    assert maximum_elements_matrix([[2,1],[3,2]])==3
    try:
        assert maximum_elements_matrix([])==False
    except:
        assert True
    assert maximum_elements_matrix([[-3,-2]])==-2
    assert maximum_elements_matrix([[0]])==0
    try:
        assert maximum_elements_matrix([[]])==False
    except IndexError:
        assert True
def maximum_elements_matrix(m):
    ''' Descr: Finds the maximum of all elements in a 2D vector
        Data: m
        Preconditions: m is a non empty 2D vector
        Results: the maximum as a result of a numpy function
        Postcondition:
    '''
    if len(m)==0 or len(m[0])==0:
        raise IndexError
    m1=turn_2d_into_numpy_matrix(m)
    return m1.max()
