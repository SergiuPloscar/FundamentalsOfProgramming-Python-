'''
Created on 28 nov. 2017

@author: SergiuP
'''

from UI.Console import ConsoleUI
from UI.Input import read_file
def start():
    ctrl=read_file()
    ui=ConsoleUI(ctrl)
    ui.menu()
start()