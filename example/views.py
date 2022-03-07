from multiprocessing import context
from django.shortcuts import render
from django.http    import  HttpResponse
import os
import sys
import shutil
import numpy as np
import subprocess
IntelPathPrev='C://Users//nikhi//Ashling//RiscFree for Intel - Documents//INT//Testing//Previous_release//INT//'
IntelPathCurrent='C://Users//nikhi//Ashling//RiscFree for Intel - Documents//INT//Testing//'
def folder_search():
    IntelPrev=[]
    IntelCurrent=[]
    IntelPrev=os.listdir(IntelPathPrev) 
    IntelCurrent=os.listdir(IntelPathCurrent) 
    Intel_Final_List=["current",*IntelPrev]
    return Intel_Final_List

# Create your views here.
# djangotemplates/example/views.py
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['sheets'] = folder_search()
        return data

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        value = self.request.GET.get('test_sheet')
        #temp = input(value)
        #print(temp)
        if (int(value) == 0):
            WinExcelPath=IntelPathCurrent.replace(" ", "*") 
            #Ini= WinExcelPath+"Test_Sheet.ini"
            os.system("py Intel_Sheet_GUI.py Test_Sheet.ini %s" %WinExcelPath )
        else:
            IntelPrev=os.listdir(IntelPathPrev) 
            prevRelease=IntelPrev[int(value)-1]
            #print(prevRelease)
            prevRelease = IntelPathPrev+prevRelease
            prevRelease=prevRelease.replace(" ", "*")    
            os.system("py Intel_Sheet_GUI.py Test_Sheet.ini %s"%prevRelease)
           # os.system('py ./Intel_Sheet_GUI.py value')
        return data
    