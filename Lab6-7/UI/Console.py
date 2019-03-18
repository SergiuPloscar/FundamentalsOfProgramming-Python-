'''
Created on 14 nov. 2017

@author: SergiuP
'''
import Domain.Operations
import Domain.WithNumpy
import UI.Input
import UI.Output
import copy
def start():
    ''' Descr: Runs the entire app
        Data:
        Preconditions:
        Result:
        Postconditions:
    '''
    print("First you must create a 2D vector")
    v=UI.Input.create_2d()
    UI.Output.print_menu()
    op=UI.Input.read_input()
    while op!=0:
        if(op==1):
            v=UI.Input.create_2d()
        elif(op==2):
            print("What is the scalar ?")
            scalar=UI.Input.read_input()
            v1=copy.deepcopy(v)
            UI.Output.print_2Dvector(Domain.Operations.add_scalar(v, scalar))
            v=copy.deepcopy(v1)
        elif(op==3):
            print("What is the other 2D vector?")
            v2=UI.Input.create_2d()
            try:
                v1=copy.deepcopy(v)
                UI.Output.print_2Dvector(Domain.Operations.add_two_vectors(v, v2))
                v=copy.deepcopy(v1)
            except IndexError:
                print("The vectors must have the same lengths")
        elif(op==4):
            print("What is the other 2D vector?")
            v2=UI.Input.create_2d()
            try:
                v1=copy.deepcopy(v)
                UI.Output.print_2Dvector(Domain.Operations.substract_two_vectors(v,v2))
                v=copy.deepcopy(v1)
            except IndexError:
                print("The vectors must have the same lengths")
        elif(op==5):
            print("What is the other 2D vector?")
            v2=UI.Input.create_2d()
            try:
                UI.Output.print_2Dvector(Domain.Operations.multiplication(v, v2))
            except IndexError:
                print("Multiplication is impossible because of the lenghts given")
        elif(op==6):
            try:
                print(Domain.Operations.sum_elements(v))
            except IndexError:
                print("Vector can't be empty")
        elif(op==7):
            try:
                print(Domain.Operations.product_elements(v))
            except IndexError:
                print("Vector can't be empty")
        elif(op==8):
            try:
                print(Domain.Operations.average_elements(v))
            except IndexError:
                print("Vector can't be empty")
        elif(op==9):
            try:
                print(Domain.Operations.minimum_elements(v))
            except IndexError:
                print("Vector can't be empty")
        elif(op==10):
            try:
                print(Domain.Operations.maximum_elements(v))
            except IndexError:
                print("Vector can't be empty")
        elif(op==11):
            UI.Output.print_2Dvector(v)
        elif(op==12):
            Domain.Operations.run_assertions()
        elif(op==13):
            print("What is the scalar ?")
            scalar=UI.Input.read_input()
            try:
                print(Domain.WithNumpy.add_scalar_numpy(Domain.WithNumpy.turn_2d_into_numpy_matrix(v), scalar))
            except IndexError:
                print("Change your vector to a non empty one , where the vectors inside have equal lengths")
        elif(op==14):
            print("What is the other 2D vector?")
            v2=UI.Input.create_2d()
            try:
                print(Domain.WithNumpy.add_two_matrices(v, v2))
            except IndexError:
                print("Change your vector to a non empty one , where the vectors inside have equal lengths")
        elif(op==15):
            print("What is the other 2D vector?")
            v2=UI.Input.create_2d()
            try:
                print(Domain.WithNumpy.substract_two_matrices(v, v2))
            except IndexError:
                print("Change your vector to a non empty one , where the vectors inside have equal lengths")
        elif(op==16):
            print("What is the other 2D vector?")
            v2=UI.Input.create_2d()
            try:
                print(Domain.WithNumpy.multiply_two_matrices(v, v2))
            except (IndexError,ValueError):
                print("The multiplication is impossible.Please change the vectors")
        elif(op==17):
            try:
                print(Domain.WithNumpy.sum_elements_matrix(v))
            except IndexError:
                print("Vector can't be empty")   
        elif(op==18):
            try:
                print(Domain.WithNumpy.product_elements_matrix(v))
            except IndexError:
                print("Vector can't be empty")
        elif(op==19):
            try:
                print(Domain.WithNumpy.average_elements_matrix(v))
            except IndexError:
                print("Vector can't be empty")
        elif(op==20):
            try:
                print(Domain.WithNumpy.minimum_elements_matrix(v))
            except IndexError:
                print("Vector can't be empty")
        elif(op==21):
            try:
                print(Domain.WithNumpy.maximum_elements_matrix(v))
            except IndexError:
                print("Vector can't be empty")
            
        
        UI.Output.print_menu()
        op=UI.Input.read_input()       
        
    
