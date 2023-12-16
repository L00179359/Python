'''
List Comprehensions
Coding using List Comprehensions By: Rahul Kharade
21OCT2023
'''

#First create list of temperature_in_kelvin
temperature_in_kelvin = (100,300,273,1000,140,516,320,725,828,930)
print('***************************************************************************')
#Convert kelvin to celcius
temperature_in_celcius = [(round(temp - 273.15,2)) for temp in temperature_in_kelvin]
print ('Temperature in celcius:', temperature_in_celcius)
print('***************************************************************************')

#Convert kelvin to Fahrenheit
temperature_in_fahrenheit = [(round(temp - 459.69,2)) for temp in temperature_in_kelvin]
print ('Temperature in Fahrenheit:', temperature_in_fahrenheit)

print('***************************************************************************')
