import sys
import configparser
import os
import shutil
import matplotlib.pyplot as plt
import numpy as np
import webbrowser
import time
import subprocess

def FileListIteration(list_value):
    for i in range(len(list_value)):
        print(list_value[i])

IntelPathPrev='C://Users//nikhi//Ashling//RiscFree for Intel - Documents//INT//Testing//Previous_release//INT'
IntelPathCurrent='C://Users//nikhi//Ashling//RiscFree for Intel - Documents//INT//Testing//'

print(IntelPathPrev)
IntelPrev=[]
IntelCurrent=[]

IntelPrev=os.listdir(IntelPathPrev) 
IntelCurrent=os.listdir(IntelPathCurrent) 
Intel_Final_List=["current",*IntelPrev]



#showing list in console
print(Intel_Final_List)
#FileListIteration(Intel_Final_List)

#IntelInputText= input('Select any above: ')

#if (int(IntelInputText) == 0):
 #   print(IntelPathCurrent)
#else:
 #   print(IntelPrev[int(IntelInputText)-1])
