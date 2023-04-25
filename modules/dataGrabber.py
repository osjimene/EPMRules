import os
import subprocess

#Get the filename of the file

def get_filename(file):
    filename = os.path.basename(file)
    return filename

def get_filehash(file):
    hash_algo = "SHA256"
    result = subprocess.run(["powershell", f"Get-FileHash -Path '{file}' -Algorith {hash_algo}"],capture_output=True, text=True)
    hash_value = result.stdout.split()[7]
    return hash_value

def get_internalname(file):
    result = subprocess.run(["powershell", f"(Get-Item '{file}').VersionInfo.InternalName"],capture_output=True, text=True)
    internalname = result.stdout
    return internalname

def get_fileversion(file):
    result = subprocess.run(["powershell", f"(Get-Item '{file}').VersionInfo.FileVersion"],capture_output=True, text=True)
    fileversion = result.stdout
    return fileversion

def get_filedescription(file):
    result = subprocess.run(["powershell", f"(Get-Item '{file}').VersionInfo.FileDescription"],capture_output=True, text=True)
    filedescription = result.stdout
    return filedescription

def get_productname(file):
    result = subprocess.run(["powershell", f"(Get-Item '{file}').VersionInfo.ProductName"],capture_output=True, text=True)
    productname = result.stdout
    return productname