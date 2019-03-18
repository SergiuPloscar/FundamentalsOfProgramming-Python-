'''
Created on 14 nov. 2017

@author: SergiuP
'''
import Domain.WithNumpy
def test_add_scalar():
    assert add_scalar([[1,2,3],[10,12,23],[11,22,3]],2)==[[3,4,5],[12,14,25],[13,24,5]]
    assert add_scalar([[1,2,3],[10,12,23],[11,22,3]],0)==[[1,2,3],[10,12,23],[11,22,3]]
    assert add_scalar([[1,2,3],[10,12,23],[11,22,3]],-5)==[[-4,-3,-2],[5,7,18],[6,17,-2]]
    assert add_scalar([[1,2,3]],10)==[[11,12,13]]
    assert add_scalar([],5)==[]
def add_scalar(v,scalar):
    ''' Descr: Adds a scalar to a 2D vector
        Data: v,scalar
        Preconditions: v is a 2D vector
                      scalar is a integer number
        Results: v
        Postcondition 
    '''
    for i in range(len(v)):
        for j in range(len(v[i])):
            v[i][j]=v[i][j]+scalar
    return v
def test_add_two_vectors():
    assert add_two_vectors([[1,2,3],[4,5,6]],[[4,5,6],[7,8,9]])==[[5,7,9],[11,13,15]]
    assert add_two_vectors([[1,1,1]],[[3,3,3]])==[[4,4,4]]
    try:
        assert add_two_vectors([[2,1,4],[4,7,8]],[[3,5,6]])==False
    except IndexError:
        assert True
    try:
        assert add_two_vectors([[2,1]],[[3,5,6]])==False
    except IndexError:
        assert True
    assert add_two_vectors([],[])==[]           
def add_two_vectors(v1,v2):
    ''' Descr: Adds two 2D vectors
        Data: v1,v2
        Preconditions: v1,v2 are two 2D vectors that must have the same length and contain vectors of the same length
        Results: v3
        Postcondition 
    '''
    if len(v1)!=len(v2):
        raise IndexError
    v3=v1[:]
    for i in range(len(v1)):
        for j in range(len(v1[i])):
            if(len(v1[i])!=len(v2[i])):
                raise IndexError
            v3[i][j]=v1[i][j]+v2[i][j] 
    return v3
def test_substract_two_vectors():
    assert substract_two_vectors([[1,2,3],[4,5,6]],[[4,5,6],[7,8,9]])==[[-3,-3,-3],[-3,-3,-3]]
    assert substract_two_vectors([[1,5,7]],[[3,3,3]])==[[-2,2,4]]
    try:
        assert substract_two_vectors([[2,1,4],[4,7,8]],[[3,5,6]])==False
    except IndexError:
        assert True
    try:
        assert substract_two_vectors([[2,1]],[[3,5,6]])==False
    except IndexError:
        assert True
    assert substract_two_vectors([],[])==[]
def substract_two_vectors(v1,v2):
    ''' Descr: Substracts two 2D vectors
        Data: v1,v2
        Preconditions: v1,v2 are two 2D vectors that must have the same length and contain vectors of the same length
        Results: v3
        Postcondition 
    '''
    if len(v1)!=len(v2):
        raise IndexError
    v3=v1[:]
    for i in range(len(v1)):
        for j in range(len(v1[i])):
            if(len(v1[i])!=len(v2[i])):
                raise IndexError
            v3[i][j]=v1[i][j]-v2[i][j] 
    return v3
def test_multiplication():
    assert multiplication([[1,2,3],[10,12,23]],[[4,2],[1,2],[1,2]])==[[9,12],[75,90]]
    assert multiplication([[1,2,3],[4,5,6]],[[7,8],[9,10],[11,12]])==[[58,64],[139,154]]
    try:
        assert multiplication([[1],[2]],[[4,2],[1,2],[1,2]])==False
    except IndexError:
        assert True
    try:
        assert multiplication([[1,2,3],[10,12,23]],[[2],[2]])==False
    except IndexError:
        assert True
    try:
        assert multiplication([[]],[[4,2],[1,2],[1,2]])==False
    except IndexError:
        assert True
def multiplication(v1,v2):
    ''' Descr: Multiplies two 2D vectors
        Data: v1,v2
        Preconditions: v1,v2 are two non empty 2D vectors
                       the vectors in v1 must have the same length as v2 does
        Results: v3
        Postcondition 
    '''
    if len(v1)==0 or len(v2)==0 or len(v1[0])==0 or len(v2[0])==0:
        raise IndexError
    if(len(v1[0])!=len(v2)):
        raise IndexError
    v4=[]
    for i in range ( len(v1)):
        v3=[]
        for j in range (len(v2[0])):
            S=0
            for k in range(len(v2)):
                S+=v1[i][k]*v2[k][j]
            v3.append(S)
        v4.append(v3)
    return v4
def test_sum_elements():
    assert sum_elements([[2,3],[4,5]])==14
    assert sum_elements([[2,0],[-1,5]])==6
    assert sum_elements([[2]])==2
    try:                    
        assert sum_elements([[]])==False
    except IndexError:
        assert True
    assert sum_elements([[2,3],[1]])==6
def sum_elements(v):
    ''' Descr: Finds the sum of all elements in a 2D vector
        Data: v
        Preconditions: v is a non empty 2D vector
        Results: S
        Postcondition
    '''
    if len(v)==0 or len(v[0])==0:
        raise IndexError
    else:
        S=0
        for i in range (len(v)):
            for j in range(len(v[i])):
                S+=v[i][j]
        return S
def test_product_elements():
    assert product_elements([[2,1],[3,2]])==12
    assert product_elements([[2],[3,2]])==12
    assert product_elements([[3,-2]])==-6
    assert product_elements([[2,1],[3,0]])==0
    try:
        assert product_elements([[]])==False
    except IndexError:
        assert True
def product_elements(v):
    ''' Descr: Finds the product of all elements in a 2D vector
        Data: v
        Preconditions: v is a non empty 2D vector
        Results: P
        Postcondition
    '''
    if len(v)==0 or len(v[0])==0:
        raise IndexError
    else:
        P=1
        for i in range (len(v)):
            for j in range(len(v[i])):
                P=P*v[i][j]
        return P
def test_average_elements():
    assert average_elements([[1,2,3],[10,12,26]])==9
    assert average_elements([[1,2,3]])==2
    assert average_elements([[12]])==12
    try:
        assert average_elements([[]])==False
    except IndexError:
        assert True
    assert average_elements([[2,3]])==2.5
    
def average_elements(v):
    ''' Descr: Finds the average of all elements in a 2D vector
        Data: v
        Preconditions: v is a non empty 2D vector
        Results: A
        Postcondition: A is float
    '''
    if len(v)==0 or len(v[0])==0:
        raise IndexError
    else:
        A=0
        for i in range (len(v)):
            for j in range(len(v[i])):
                A+=v[i][j]
        A=A/(len(v)*len(v[0]))
        return A
def test_minimum_elements():
    assert minimum_elements([[2,1],[3,2]])==1
    assert minimum_elements([[2],[3,2]])==2
    assert minimum_elements([[3,-2]])==-2
    assert minimum_elements([[0]])==0
    try:
        assert minimum_elements([[]])==False
    except IndexError:
        assert True
def minimum_elements(v):
    ''' Descr: Finds the minimum of all elements in a 2D vector
        Data: v
        Preconditions: v is a non empty 2D vector
        Results: mini
        Postcondition:
    '''
    if len(v)==0 or len(v[0])==0:
        raise IndexError
    else:
        mini=v[0][0]
        for i in range(len(v)):
            for j in range(len(v[i])):
                if v[i][j]<mini:
                    mini=v[i][j]
        return mini
def test_maximum_elements():
    assert maximum_elements([[2,1],[3,2]])==3
    assert maximum_elements([[3],[3,2]])==3
    assert maximum_elements([[-3,-2]])==-2
    assert maximum_elements([[0]])==0
    try:
        assert maximum_elements([[]])==False
    except IndexError:
        assert True
def maximum_elements(v):
    ''' Descr: Finds the maximum of all elements in a 2D vector
        Data: v
        Preconditions: v is a non empty 2D vector
        Results: maxi
        Postcondition:
    '''
    if len(v)==0 or len(v[0])==0:
        raise IndexError
    else:
        maxi=v[0][0]
        for i in range(len(v)):
            for j in range(len(v[i])):
                if v[i][j]>maxi:
                    maxi=v[i][j]
        return maxi
def run_assertions():
    test_add_scalar()
    test_add_two_vectors()
    test_average_elements()
    test_maximum_elements()
    test_minimum_elements()
    test_product_elements()
    test_substract_two_vectors()
    test_sum_elements()
    test_multiplication()
    Domain.WithNumpy.test_add_scalar_numpy()
    Domain.WithNumpy.test_turn_2d_into_numpy_matrix()
    Domain.WithNumpy.test_add_two_matrices()
    Domain.WithNumpy.test_substract_two_matrices()
    Domain.WithNumpy.test_multiply_two_matrices()
    Domain.WithNumpy.test_sum_elements_matrix()
    Domain.WithNumpy.test_product_elements_matrix()
    Domain.WithNumpy.test_average_elements_matrix()
    Domain.WithNumpy.test_minimum_elements_matrix()
    Domain.WithNumpy.test_maximum_elements_matrix()