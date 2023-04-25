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