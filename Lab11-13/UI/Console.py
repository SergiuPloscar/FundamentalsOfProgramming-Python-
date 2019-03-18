from UI.Input import read_input
class ConsoleUI:
    ''' Prints the menu and runs the options chosen '''
    def __init__(self,ctrl):
        self.__ctrl = ctrl
    @staticmethod
    def printMenu():
        ''' Descr: Prints the option menu
        Data:
        Preconditions:
        Result: s
        Postcondition: s is the string that represents the menu
        '''
        s="\n Menu \n"
        s+="Choose an option \n "
        s+="\t 1.Add patient \n "
        s+="\t 2.Delete patient \n  "
        s+="\t 3.Add department \n "
        s+="\t 4.Delete department \n "
        s+="\t 5.Add patient to a department \n "
        s+="\t 6.Delete patient at department \n "
        s+="\t 7.Sort the patients in departments by numeric code\n "
        s+="\t 8.Sort departments by number of patients above a limit \n "
        s+="\t 9.Sort departments by nr of patients and patients alphabetically \n "
        s+="\t 10.Show departments with the age under \n "
        s+="\t 11.Show patients with name containing string at given department \n "
        s+="\t 12.Show departments with patients with first name \n "
        s+="\t 13.Show all patients \n "
        s+="\t 14.Show all departments \n "
        s+="\t 15.Show patients in department \n"
        s+="\t 0.Exit"
        print(s)
    def menu(self):
        while True:
            ConsoleUI.printMenu()
            op=read_input()
            if(op==1):
                print("Give patient data (fname,lname,numcode,disease)")
                fname=input()
                lname=input()
                numcode=input()
                disease=input()
                if(self.__ctrl.CreatePatientC(fname,lname,numcode,disease)!=None):
                    self.__ctrl.AddPatientC(self.__ctrl.CreatePatientC(fname,lname,numcode,disease))
                else:
                    print("Incorrect numcode")
            elif(op==2):
                print("Give numcode of patient")
                numcode=input()
                self.__ctrl.DelPatientC(numcode)
            elif(op==3):
                print("Give department data(name, nr, nr of beds)")
                name=input()
                nr=read_input()
                nr_of_beds = read_input()
                self.__ctrl.AddDepartmentC(self.__ctrl.CreateDepartmentC(name,nr,nr_of_beds,[]))
            elif(op==4):
                print("Give department nr")
                nr=read_input()
                self.__ctrl.DelDepartmentC(nr)
            elif(op==5):
                print("Give patient data (fname,lname,numcode,disease)")
                fname=input()
                lname=input()
                numcode=input()
                disease=input()
                print("Give department nr")
                nr=read_input()
                if (self.__ctrl.AddPatientAtDepartment(fname,lname,numcode,disease,nr)==0):
                    print("Patient added")
                elif (self.__ctrl.AddPatientAtDepartment(fname,lname,numcode,disease,nr)==1):
                    print("Patient already exists")
                elif (self.__ctrl.AddPatientAtDepartment(fname,lname,numcode,disease,nr)==2):
                    print("Department doesnt exist")
                elif (self.__ctrl.AddPatientAtDepartment(fname,lname,numcode,disease,nr)==3):
                    print("Wrong patient data")
                elif (self.__ctrl.AddPatientAtDepartment(fname,lname,numcode,disease,nr)==4):
                    print("Not enough beds")
            elif(op==6):
                print("Give numcode of patient")
                numcode=input()
                print("Give department nr")
                nr=read_input()
                self.__ctrl.DelPatientAtDepartment(numcode,nr)
            elif(op==7):
                self.__ctrl.SortByNC()
            elif(op==8):
                print("Give age")
                age=read_input()
                self.__ctrl.SortByNrOfPatientsAboveAge(age)
            elif(op==9):
                self.__ctrl.SortDepartamentsAndPatients()
            elif(op==10):
                print("Give age")
                age=read_input()
                self.__ctrl.FindByUnderAge(age)
            elif(op==11):
                print("Give department nr")
                nr=read_input()
                print("Give string")
                string=input()
                try:
                    self.__ctrl.FindByString(nr,string)
                except IndexError:
                    print("Department doesn't exist")
            elif(op==12):
                print("give name")
                name=input
                self.__ctrl.FindByFname(name)
            elif(op==13):
                self.__ctrl.PrintPatients()
            elif(op==14):
                self.__ctrl.PrintDepartments()
            elif(op==15):
                print("Give department nr")
                nr=read_input()
                self.__ctrl.PrintAtDepartment(nr)
            elif(op==0):
                exit()
            else:
                print("Give option")           
            
                
            
        
