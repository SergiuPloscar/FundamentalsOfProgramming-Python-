print(" How many numbers are in the list ? ")
n=int(input())
l=[]
print(" Enter the numbers one by one, pressing enter after each number ")
for i in range(n):
    l.append(int(input()))
def product(l):
    ''' This function takes as argument the list of numbers introduced by the
    user and returns the product of those numbers by simplying
    multiplying them with one another '''
    p=1
    for elem in l:
        p=p*elem
    return p
print("The product of the given numbers is ",product(l))
