def isSorted(l,f,param):
    for i in range(0, len(l)-1):
        for j in range (i+1, len(l)):
            if not f(l[i],l[j],param):
                aux=l[i]
                l[i]=l[j]
                l[j]=aux
    return l
def isSearched(l,f,param):
    new=[]
    for i in range ( len(l)):
        if f(l[i],param)== True :
            new.append(l[i])
    return new
def myBT(l,k,f):
    domain=[i for i in range(-1,len(l))]
    q,sol=0,[]
    sol.append(initSol(domain))
    while q>=0:
        isOK = False
        while isOK==False and sol[q]<getLast(domain):
            sol[q]=getNext(sol[q])
            isOK = f(sol,l)
            if(isOK==True):
                if isSolution(sol,k):
                    yield(sol)
                else:
                    q+=1
                    sol.append(initSol(domain))
            else:
                del(sol[q])
                q=-1
def initSol(domain):
    return domain[0]
def getNext(l):
    return l+1
def getLast(domain):
    return domain[len(domain)-1]
def isSolution(sol,size):
    return len(sol)==size

        
