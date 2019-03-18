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