
'''
Create a folder called Templates
By: Rahul Kharade
21 DEC 2023
'''


import os

def create_folder():
    folder_name = "Templates"

    # Get the current working directory
    current_directory = os.getcwd()

    # Create the full path for the Templates folder
    folder_path = os.path.join(current_directory, folder_name)

    try:
        # Create the Templates folder
        os.mkdir(folder_path)
        print(f'The "{folder_name}" folder has been created successfully at: {folder_path}')
    except FileExistsError:
        print(f'The "{folder_name}" folder already exists at: {folder_path}')

if __name__ == "__main__":
    create_folder()
