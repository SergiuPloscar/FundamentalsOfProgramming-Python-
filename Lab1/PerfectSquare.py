n=int(input('Give number '))
d=0
for i in range(1,n+1):
    if(i*i==n):
        d=d+1
if d>0:
    print('Is perfect square')
else:
    print('Is not perfect square')
    
