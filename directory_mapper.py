#DIRECTORY_MAP.py


#Imports
import os
try:
    import numpy as np
    module_name = 'numpy'
except ImportError:
    print (f"Trying to Install required module: numpy\n")
    os.system(f'python -m pip install numpy')
    # -- above lines try to install requests module if not present
    # -- if all went well, import required module again ( for global access)
import numpy as np

try:
    import pandas as pd
    module_name = 'pandas'
except ImportError:
    print (f"Trying to Install required module: {module_name}\n")
    os.system(f'python -m pip install {module_name}')
    # -- above lines try to install requests module if not present
    # -- if all went well, import required module again ( for global access)
import pandas as pd

try:
    from datetime import date
    module_name = 'datetime'
except ImportError:
    print (f"Trying to Install required module: {module_name}\n")
    os.system(f'python -m pip install {module_name}')
    # -- above lines try to install requests module if not present
    # -- if all went well, import required module again ( for global access) 
from datetime import date

try:
    import openpyxl
    module_name = 'openpyxl'
except ImportError:
    print (f"Trying to Install required module: {module_name}\n")
    os.system(f'python -m pip install {module_name}')
    # -- above lines try to install requests module if not present
    # -- if all went well, import required module again ( for global access)
import openpyxl

try:
    import re
    module_name = 're'
except ImportError:
    print (f"Trying to Install required module: {module_name}\n")
    os.system(f'python -m pip install {module_name}')
    # -- above lines try to install requests module if not present
    # -- if all went well, import required module again ( for global access)
import re

# Create main_path so files can be referenced from relative path within package folder
main_path = os.path.dirname(__file__)

# Takes user input from terminal
directory_input = input("Paste a filepath:")

today = date.today()

full_date = today.strftime("%y-%m-%d") # dd/mm/YY
print('File Date: ' + full_date)

directory_level = 0

treeFrame = pd.DataFrame({'Tree':[],'LINK':[]})
treeLevel = 0


def generate_directory_tree(path, indent=''):
    """Generates a directory tree diagram."""
    global treeLevel
    for entry in os.scandir(path):
        treeLevel += 1
        try:
            if entry.is_dir():
                treeFrame.loc[treeLevel, 'Tree'] = indent + '|__' + entry.name
            
                print(indent + '|__' + entry.name)
                generate_directory_tree(entry.path, indent + '|   ')
            if entry.is_file():
                treeFrame.loc[treeLevel,'Tree'] = indent + '|__' + entry.name
                treeFrame.loc[treeLevel,'LINK'] = path
                treeFrame.loc[treeLevel] = treeFrame.loc[treeLevel].apply(lambda x: f'=HYPERLINK("{path}", "{x.split("/")[-1]}")')

                print(indent + '|__' + entry.name)
        except:

            treeFrame.loc[treeLevel, 'Tree'] = indent + '|__' + entry.name + ' FOLDER ACCESS DENIED FOR USER GENERATING TREE'
            print(indent + '|__' + entry.name + ' FOLDER ACCESS DENIED FOR USER GENERATING TREE')


if __name__ == "__main__":
    generate_directory_tree(directory_input)



print(treeFrame)

directory_input = directory_input.replace('\\', '_')
directory_input = directory_input.replace(':', '')
print(directory_input)

file_name = full_date + ' (' + directory_input + ')' + '.xlsx'
maps_path = os.path.join(main_path, 'Directory Maps\\')

file_path = os.path.join(maps_path, file_name)

treeFrame.to_excel(file_path)

print('\n\nMap saved to: ' + file_path)
