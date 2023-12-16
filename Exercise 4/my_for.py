'''
Loop- For
Coding using For loop  By: Rahul Kharade
21OCT2023
'''

print ('*******************************************************************************')
#Check even and odd numbers from list
iterable_variable = [1,2,3,4,5,6,7,8,9,10]

for item in iterable_variable:
     if item %2 != 0:
        print('Odd numbers from list',item)
for item in iterable_variable:
    if item %2 == 0:
        print('Even numbers from list',item)


print ('*******************************************************************************')
#Use scan.ietms to get output
scan = {"ATU": "Cloud Computing", "NCI": "DevOps", "DBS": "Business Analyst"}
for university, course in scan.items():
    print(f"Found best courses in University : At {university} best course is {course}")
 
print ('*******************************************************************************')
  

