'''
Loop- If,Elif and Else
Coding using If Else loops  By: Rahul Kharade
21OCT2023
'''

#Calculate grade obtained by student
#Insert your marks
marks=input("Enter your marks:")
print ('Marks obtained', marks)
#Marks Condition
if int(marks) >= 75:
    print ('Grade is Distinction:Excellent')
elif int(marks) >=60 and int(marks) <=74:
    print ('Grade is First Class:Better luck next time')
elif int(marks) >=50 and int(marks) <=59:
    print ('Grade is Second Class:Try hard next time')
elif int(marks) >=40 and int(marks) <=49:
    print ('Grade is Pass Class:Very disappoiting')
else : 
    print ('Failed:Bye Bye')


