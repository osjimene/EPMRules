import easygui
from modules.dataGrabber import get_fileattributes, get_certificates
from modules.mongo import insert_data
import os


    # certoutput = r"C:\Users\osjimene\Projects\RuleCreator\Certificates"
    # import os

    # certoutput = os.path.join(os.getcwd(), 'Certificates')

# Prompt user to select files they want metadata from.
import easygui
files = easygui.fileopenbox(default=str(), multiple=True)

# Loop through each file and get its information.
for file in files:
    certoutput = r"C:\Users\osjimene\Projects\RuleCreator\Certificates"
    import os

    certoutput = os.path.join(os.getcwd(), 'Certificates')
    

    # Get file information.
    result = get_fileattributes(file, certoutput)

    # Parse the information into a json format.
    result_dict = {}
    for line in result.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            result_dict[key.strip()] = value.strip()

    # Get the number of files in the certificate folder.
    num_files = len([f for f in os.listdir(certoutput) if os.path.isfile(os.path.join(certoutput, f))])

    # Run a for loop to get the certificates in the certificate folder.
    for i in range(num_files):
        result = get_certificates(certoutput)
        result_dict.update(result)

    # Insert the data into the database.
    insert_data(result_dict)