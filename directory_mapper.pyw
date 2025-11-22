# DIRECTORY_MAP.py


# Imports
import os
setup_input = input('\n\nRun first time setup? (y)\(n)\n')

if 'y' in setup_input or 'Y' in setup_input or '1' in setup_input:
    try:
        module_name = 'numpy'
        import numpy as np
    except ImportError:
        print (f"Trying to Install required module: {module_name}\n")
        os.system(f'python -m pip install {module_name}')
        # -- above lines try to install requests module if not present
        # -- if all went well, import required module again ( for global access)
    import numpy as np
    
    try:
        module_name = 'pandas'
        import pandas as pd
    except ImportError:
        print (f"Trying to Install required module: {module_name}\n")
        os.system(f'python -m pip install {module_name}')
        # -- above lines try to install requests module if not present
        # -- if all went well, import required module again ( for global access)
    import pandas as pd
    
    try:
        module_name = 'datetime'
        from datetime import date
    except ImportError:
        print (f"Trying to Install required module: {module_name}\n")
        os.system(f'python -m pip install {module_name}')
        # -- above lines try to install requests module if not present
        # -- if all went well, import required module again ( for global access) 
    from datetime import date
    
    try:
        module_name = 'openpyxl'
        import openpyxl
    except ImportError:
        print (f"Trying to Install required module: {module_name}\n")
        os.system(f'python -m pip install {module_name}')
        # -- above lines try to install requests module if not present
        # -- if all went well, import required module again ( for global access)
    import openpyxl
    
    '''
    try:
        import re
        module_name = 're'
    except ImportError:
        print (f"Trying to Install required module: {module_name}\n")
        os.system(f'python -m pip install {module_name}')
        # -- above lines try to install requests module if not present
        # -- if all went well, import required module again ( for global access)
    import re
    '''
else:
    print('\n')
# Create main_path so files can be referenced from relative path within package folder
main_path = os.path.dirname(__file__)

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
# Loop that runs so window can be used multiple times
while True:
    # Takes user input from terminal
    directory_input = input('\n\nPaste a filepath:')
    # Current date of map
    today = date.today()
    # Parsed current date
    full_date = today.strftime("%y-%m-%d") # dd/mm/YY
    # Print current date
    print('File Date: ' + full_date)
    
    directory_level = 0
    
    treeFrame = pd.DataFrame({'Tree':[],'LINK':[]})
    
    treeLevel = 0
    
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
    


