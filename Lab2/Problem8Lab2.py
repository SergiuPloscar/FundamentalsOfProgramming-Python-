print(" Please enter a number ")
n=int(input())
def prime(n):
    ''' This function takes as argument the number given by the user
    and verifies if it is prime or not by going through every number smaller
    than it, up until its half and checking if it has any divisors. The function
    returns True if the number is prime and False otherwise '''
    if(n<=1):
        return False
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            return False
    return True
def nearest_prime(n):
    ''' This function takes as argument the number given by the user and
    goes both upwards and downwards, step by step, trying to find the
    nearest prime number. If there are two numbers at equal distance, both prime
    it returns the lower number. Otherwise it returns the closest prime number.'''
    stop1=False
    stop2=False
    bigger=n
    lower=n
    while stop1 == False and stop2 == False :
        bigger+=1
        lower-=1
        if prime(bigger)==True :
            stop1=True
        if prime(lower)==True :
            stop2=True
    if stop2 == True:
        return lower
    return bigger
print( " The nearest prime number is " , nearest_prime(n) )

            
        
