'''
OS utilities
By: Rahul Kharade
16 DEC 2023
'''


def create_directory(directory_name: str) ->bool:
    # Use try/except to catch errors
    try:
        # Create the diretory
        os.mkdir(directory_name)
        # If this worked, return True
        return True
    except:
        # Give an explicit error message
        print(f"Error creating directory {directory_name}")
        # If this did not work, return False
        return False    