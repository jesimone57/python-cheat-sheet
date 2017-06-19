#!/usr/local/bin/python3

# Example Python program to count all the occurances of digits 0 through 9 in 
# all the integers from 1 to 1000.  Do any digits appear more of less times than others?
# let's find out ...

import sys
if sys.version_info[0] < 3:
	raise Exception("Must be using python 3")

# initialize the dictionary holding the results of all digit occurenences
digit_occurrences = {}
for i in list("0123456789") : digit_occurrences[i] = 0

for i in range(1, 1001):
    for j in list(str(i)):
        digit_occurrences[j] += 1
        
print(digit_occurrences)

max_occurrence_digit = max(digit_occurrences, key=digit_occurrences.get)
min_occurrence_digit = min(digit_occurrences, key=digit_occurrences.get)

print(str(max_occurrence_digit) + " appears the most:  " + str(digit_occurrences[max_occurrence_digit]) + " times") 
print(str(min_occurrence_digit) + " appears the least:  " + str(digit_occurrences[min_occurrence_digit]) + " times") 
