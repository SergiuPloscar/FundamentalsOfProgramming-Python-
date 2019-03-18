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
def create_2d():
    ''' Descr: Reads a 2D vector from console
        Data: 
        Preconditions:
        Result: v
        Postcondition: v is a 2D vector
    '''
    print("How many vectors are in the list ?")
    n=read_input()
    print("How long is each vector ?")
    m=read_input()
    v=[]
    print("Introduce the values one by one")
    for i in range (n):
        v1=[]
        for j in range(m):
            v1.append(read_input())
        v.append(v1)
    return v
            