'''
Functions
Coding using Functions By: Rahul Kharade
22OCT2023
'''

#Calculate batting average of batsman in last 10 matches
def last_10_matches_score(*runs):
    batting_average = 0
    number_of_matches=10
    
#For loop execute until last value    
    for runs in runs:
        batting_average = batting_average + runs /number_of_matches
    return batting_average

print('Batting average of last 10 matches:',last_10_matches_score(55,60,12,139,34,23,66,8,99,100))

