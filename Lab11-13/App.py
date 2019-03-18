from Infrastructure.PRepository import PatientRepository
from Infrastructure.DRepository import DepartmentRepository
from Controller.AppController import ControllerClass
from UI.Console import ConsoleUI
def start():
    repo1=PatientRepository()
    repo2=DepartmentRepository()
    ctrl=ControllerClass(repo1,repo2) 
    ui= ConsoleUI(ctrl)
    ui.menu()
start()