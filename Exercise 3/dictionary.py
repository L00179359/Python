'''
Dictionaries
Coding with Dictionaries  By: Rahul Kharade
Use below methods-
my_dictionary.keys()
my_dictionary.values()
my_dictionary.items()
21OCT2023
'''

#Create the initial dictionary
print("*********************************************************************************************************")
my_dictionary={"Company Name": "TCS", "Industry": "IT", "Total Employees": "500000+"}
#Print whole sentence
print('Company details are :' , (my_dictionary))
#Use dict.key to show key 
print (my_dictionary.keys())
#Use dict.values to show actual values
print (my_dictionary.values())
#Use dict.item to show keys and values
print (my_dictionary.items())

print("*********************************************************************************************************")

#Now update the company name and number of employee details
my_dictionary["Company Name"] = "Infosys"
my_dictionary["Total Employees"] = "300000+"

print("Update company name to Infosys")
print('Company details after update :' , (my_dictionary))

print("*********************************************************************************************************")
