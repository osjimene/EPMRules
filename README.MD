# EPM Rule Metatada Puller

The EPM Rule Metadata Puller is a Python Script that facilitates the use of PowerShell Commandlets iteratively over several executable files. It is designed to be easy to use and deploy in a cloud environment to store uploaded file metadata that can be further analyzed to create elevation rules for Endpoint Privilege Management Tooling.

The project includes several modules that can be used to create a cloud based MongoDB instance using CosmosDB OR locally for testign using the Tinydb functionality. These modules include:
-Database.py (The TinyDB functionality that will parse out information and store it in a local json db file)
-Mongo.py (The Simple module to connect to a CosmosDB instance configured as a MongoDB database)
-DataGrabber.py (Uses the EPM Commandlets Powershell functions to extract required metadata from uploaded files)


The project is designed to be used by IT Admins who need to pull functioning fileversion information over a large set of files for faster/easier rule creation in EPM. It can be easily integrated into existing scripts that push/post policies to Intune vie the Graph API.

Overall, The EPM Rule Metadata Puller is a lightweight and flexible tool for an Intune IT Admin that wants to facilitate the creation of elevation rules for their enterprise. This functionality has been a huge time-saver for me and my team when it comes to testing and deploying application rules in virtual environments before publishing in production tenants. 

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started
To get started with the EPM Rule Metadata Puller, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Choose whether to use the TinyDB or CosmosDB functionality by importing the appropriate module (`Database.py` or `Mongo.py`).
4. Run the `DataGrabber.py` script to extract metadata from uploaded files using the EPM Commandlets Powershell functions.
5. Store the extracted metadata in a local json db file (if using TinyDB) or in a CosmosDB instance configured as a MongoDB database (if using CosmosDB).
6. Analyze the stored metadata to create elevation rules for Endpoint Privilege Management Tooling.

That's it! With these steps, you should be able to use the EPM Rule Metadata Puller to easily extract and store metadata from uploaded files, and create elevation rules for your enterprise.

Note: For further simplicity in getting certificates tied to files, there is a /tmp directory in the root folder of the project that is where the Certificates are stored. If there are duplicate certificates, only 1 will be shown in the folder.

### Prerequisites

-Python 3.X
-Pip
-For MongoDB.py, notice the Connection string information is referencin the System Environment variable `Connection_String` Replace this and other similar values acordingly. (Any values starting with os.getenv are environment variables specific to your machine)

### Usage

Here's an example of how to use the EPM Rule Metadata Puller to extract metadata from a file:

```python
from DataGrabber import DataGrabber

# Create a new DataGrabber object
grabber = DataGrabber()

# Extract metadata from a file
metadata = grabber.extract_metadata('path/to/file')

# Print the metadata
print(metadata)

```
This will create a new `DataGrabber` object and use it to extract metadata from the specified file. The metadata will be returned as a dictionary, which can be printed to the console or used in other ways.

You can also use the `store_metadata` method to store the extracted metadata in a local json db file or in a CosmosDB instance:
```python
from DataGrabber import DataGrabber
from Database import Database

# Create a new DataGrabber object
grabber = DataGrabber()

# Create a new Database object
db = Database()

# Extract metadata from a file
metadata = grabber.extract_metadata('path/to/file')

# Store the metadata in the database
db.store_metadata(metadata)

```
This will create a new `Database` object and use it to store the extracted metadata in a local json db file or in a CosmosDB instance, depending on which module you imported.

Make sure to replace `path/to/file` with the actual path to the file that you want to extract metadata from. You can also customize the code to fit your specific needs



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.