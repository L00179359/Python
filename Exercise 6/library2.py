'''
The Python Standard Library
By: Rahul Kharade
26OCT2023
'''

from math import sqrt
print("Input lengths of the two short triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse to four places is: {hypo:1.4f}".format(hypo=c))