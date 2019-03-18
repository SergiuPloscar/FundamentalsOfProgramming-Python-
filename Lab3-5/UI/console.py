'''
Created on 31 oct. 2017

@author: SergiuP
'''
import Domain.Changes
import Domain.Views
import UI.input
import UI.output
import GlobalList
def start():
    ''' Descr: Runs the entire app
        Data:
        Preconditions:
        Result:
        Postconditions:
    '''
    
    Domain.Views.data_examples()
    print("")
    print("How many participants? ")
    n=UI.input.read_input()
    my_list=UI.input.create_list(n)
    GlobalList.prev_list=my_list[:]
    while True:
        UI.output.print_menu()
        op=UI.input.read_input()
        if(op==1):
            print("Give score ")
            score=UI.input.read_input()
            Domain.Changes.add(score,my_list)  
        elif(op==2):
            print("Give score ")
            score=UI.input.read_input()
            print("Give index ")
            index=UI.input.read_input()
            Domain.Changes.insert(score, index, my_list)
        elif(op==3):
            print("Give index ")
            index=UI.input.read_input()
            Domain.Changes.remove(index,my_list)
        elif(op==4):
            print("Give index1 ")
            index1=UI.input.read_input()
            print("Give index2 ")
            index2=UI.input.read_input()
            Domain.Changes.remove_from(index1, index2, my_list)
        elif(op==5):
            print("Give index ")
            index=UI.input.read_input()
            print("Give score ")
            score=UI.input.read_input()
            Domain.Changes.replace_with(index, score, my_list)
        elif(op==6):
            print("Give score ")
            score=UI.input.read_input()
            UI.output.print_list(Domain.Views.less_than(score, my_list))
        elif(op==7):
            UI.output.print_list(Domain.Views.sorted(my_list))
            my_list=GlobalList.prev_list[:]
        elif(op==8):
            print("Give score ")
            score=UI.input.read_input()
            UI.output.print_list(Domain.Views.sorted_and_greater_than(score, my_list))
            my_list=GlobalList.prev_list[:]
        elif(op==9):
            Domain.Views.run_assertions()
            GlobalList.prev_list=my_list[:]
        elif(op==10):
            print("Your former list was ", GlobalList.prev_list)
        elif(op==11):
            print("Give index1")
            index1=UI.input.read_input()
            print("Give index2")
            index2=UI.input.read_input()
            print("Average is ",Domain.Views.avg_from_to(index1, index2, my_list))
        elif(op==12):
            print("Give index1 ")
            index1=UI.input.read_input()
            print("Give index2 ")
            index2=UI.input.read_input()
            print("Minimum is" ,Domain.Views.min_from_to(index1,index2,my_list)) 
        elif(op==13):
            print("Give mult ")
            mult=UI.input.read_input()
            print("Give index1 ")
            index1=UI.input.read_input()
            print("Give index2 ")
            index2=UI.input.read_input()
            UI.output.print_list(Domain.Views.mul_from_to(mult, index1, index2, my_list))
        elif(op==14):
            print("Give mult ")
            mult=UI.input.read_input()
            Domain.Changes.filter_mul(mult,my_list)
        elif(op==15):
            print("Give score ")
            score=UI.input.read_input()
            Domain.Changes.filter_greater_than(score,my_list)
        elif(op==16):
            my_list=Domain.Changes.Undo(my_list)    
        elif(op==0):
            UI.output.print_list(my_list)
            break
        else:
            print("Please choose a valid option")
        UI.output.print_list(my_list)
        