'''
Functions
Coding using Functions By: Rahul Kharade
22OCT2023
'''

def calculate_distance_in_kilometer(kilometer):
    """
    Calculate distance in kilometer when input is in miles

    """
    return 1.6 * kilometer

# Get a radius value as a string
r = input("Provide a miles value: ")
# Convert it to a float
r_float = float(r)
# Call the function and create the variable for the return value
a = calculate_distance_in_kilometer(r_float)
print('Distance in kilometer is:', a)