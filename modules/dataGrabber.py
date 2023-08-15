import os
import subprocess
import shutil
import time


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
def get_fileattributes(file, certoutput):
    hashalgorithm = "Sha256"
    result = subprocess.run(["powershell", rf"Import-Module 'C:\Users\osjimene\Projects\RuleCreator\modules\EpmTools\EpmCmdlets.dll'; Get-fileAttributes -FilePath '{file}' -CertOutputPath {certoutput} -HashAlgorithm '{hashalgorithm}'"],capture_output=True, text=True)
    fileattributes = result.stdout
    return fileattributes


def move_cert(src_folder, dst_folder):
    # Get the last file in the Certificates folder
    files = os.listdir(src_folder)
    file = files[-1]
    last_file = os.path.join(src_folder, files[-1])
    destination = os.listdir(dst_folder)
    if file in destination:
        os.remove(last_file)
    else:
        # Move the last file to the Tmp folder
        shutil.move(last_file, dst_folder)


def get_certificates(certoutput):
    certstore = r"C:\Users\osjimene\Projects\RuleCreator\Tmp"
    file = subprocess.run(["powershell", f"ls {certoutput} | Select-Object -Last 1 -ExpandProperty Name"],capture_output=True, text=True)
    encode = subprocess.run(["powershell", f"ls {certoutput} | Select-Object -Last 1 | Get-Content"],capture_output=True, text=True)
    move_cert(certoutput, certstore)
    # subprocess.run(["powershell", f"ls {certoutput} | Select-Object -Last 1 | rm"],capture_output=True, text=True)
    filename = file.stdout.strip()
    encoding = encode.stdout.strip()
    certificate = {filename: encoding}
    return certificate




