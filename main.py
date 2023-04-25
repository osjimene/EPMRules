import easygui
import pandas as pd
import openpyxl
from modules.dataGrabber import get_filehash, get_filename
import os
import subprocess


# Promp user to select file they want metadata from. 
file = easygui.fileopenbox(default=str())

#Get Fileinformation
filename = get_filename(file)
filehash = get_filehash(file)

#Parse collected data into a CSV format. 

#Open the desired csv/excel and append the new information to excel
print(filehash)
#Save and close the program.
