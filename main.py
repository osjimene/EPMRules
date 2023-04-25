import easygui
import pandas as pd
import openpyxl
from modules.dataGrabber import get_filehash, get_filename, get_internalname, get_filedescription,get_productname,get_fileversion
import os
import subprocess


# Promp user to select file they want metadata from. 
file = easygui.fileopenbox(default=str())

#Get Fileinformation
filename = get_filename(file)
filehash = get_filehash(file)
internalname = get_internalname(file)
fileversion = get_fileversion(file)
filedescription = get_filedescription(file)
productname = get_productname(file)


#Parse collected data into a CSV format. 

#Open the desired csv/excel and append the new information to excel
print(f"Filename: {filename} \nFileHash: {filehash} \nInternalName: {internalname} \nVersion: {fileversion} \nFileDescription: {filedescription} \nProductName: {productname} ")
#Save and close the program.
