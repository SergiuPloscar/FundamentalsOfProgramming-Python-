print("Which is the number you want to verify?")
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
b=prime(n)
if b==True:
    print("The number is prime")
else:
    print("The number is not prime")
        
    
      
