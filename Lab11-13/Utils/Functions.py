
def numcode_comparison(a,b,l):
    if a.getNumericCode() < b.getNumericCode():
        return True
    return False

def nr_of_patients_age_comparison(a,b,l):
    nra=0
    nrb=0
    for i in range(len(a.getListOfPatients())):
        
        age=2018-(19*100 + int(a.getListOfPatients()[i].getNumericCode()[1:3]))
        if (age > l):
            nra=nra+1
            
    for i in range(len(b.getListOfPatients())):
        age=2018-(19*100 + int(b.getListOfPatients()[i].getNumericCode()[1:3]))
        if(age>l):
            nrb=nrb+1
    if nra<nrb:
        return True
    return False

def departments_comparison(a, b, l):
    if len(a.getListOfPatients())<len(b.getListOfPatients()):
        return True
    return False

def patients_comparison(a, b, l):
    if(a.getLastName()<b.getLastName()):
        return True
    elif(a.getLastName()==b.getLastName() and a.getFirstName()<b.getFirstName()):
        return True
    return False

def find_by_age(a, param):
    for i in range(len(a.getListOfPatients())):
        age=2018-(19*100 + int(a.getListOfPatients()[i].getNumericCode()[1:3]))
        if(age<param):
            return True
    return False

def find_by_string(a,param):
    if(param in a.getFirstName() or param in a.getLastName()):
        return True
    return False

def find_by_fname(a,param):
    for i in range(len(a.getListOfPatients())):
        if(a.getListOfPatients()[i].getFirstName()==param):
            return True
    return False
        
   
    

        
    
