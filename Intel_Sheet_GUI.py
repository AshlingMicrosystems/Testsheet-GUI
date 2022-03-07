import openpyxl
import sys
import configparser
import os
import shutil
import matplotlib.pyplot as plt
import numpy as np
import webbrowser
import time
import subprocess
#import intel_test_sheet.py

# riscv.ini will be the deafult file if there is no commandline parameter
#if len(sys.argv)<=1:
#    IniFileName="Test_Sheet.ini";
#else:
IniFileName = sys.argv[1];
# Check commandline parameter file path/file are valid or not
# Print the error msg and exit the script if it is not valid
try:
    f = open(IniFileName)
    # Do something with the file
except IOError:
    print("Ini file does not exists/accessible in the following path:"+IniFileName)
    exit(0)


# reag the configurations from the ini file
read_config = configparser.ConfigParser()
read_config.read(IniFileName)

OsTypeWin               = read_config.get("OS-parameters", "OS_Win").strip()
OsTypeLin               = read_config.get("OS-parameters", "OS_Linux").strip()

if (OsTypeWin=="1"):
    print("Fetching Data for Windows sheet")
    PathWinXml=sys.argv[2]
    #print(PathWinXml+"RiscFreeTestCases_Intel_win.xlsm")
    PathWinXml = (PathWinXml+"//RiscFreeTestCases_Intel_win.xlsm")
    os.system('py ./supportive_files/intel_test_sheet.py "chart_win"  %s'%PathWinXml)
if (OsTypeLin=="1"):
    print("Fetching data for linux sheet")
    PathLinXml=sys.argv[2]
    PathLinXml = (PathLinXml+"//RiscFreeTestCases_Intel_Lin.xlsm")
    os.system('py ./supportive_files/intel_test_sheet.py "chart_lin" %s'%PathLinXml)