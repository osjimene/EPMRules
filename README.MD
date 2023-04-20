Create a Virtual Environment:

Open a command prompt and navigate to the directory where you want to create your virtual environment. Then run the following command:

python -m venv <name_of_your_venv>

3. Activate the Virtual Environment:

Once the virtual environment is created, you can activate it by running the following command:

<name_of_your_venv>\Scripts\activate

4. Install Packages:

Once the virtual environment is activated, you can install any packages you need using the pip command. For example, to install the requests package, you can run the following command:

pip install requests


Structure: 
├── main.py
├── modules
│   ├── module1.py
│   ├── module2.py
│   └── module3.py
├── tests
│   ├── test_module1.py
│   ├── test_module2.py
│   └── test_module3.py
└── utils
    ├── util1.py
    ├── util2.py
    └── util3.py