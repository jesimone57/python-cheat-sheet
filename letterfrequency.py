#!/usr/local/bin/python3

# Example Python program to determin the letter/character frequency in text

import sys
if sys.version_info[0] < 3:
	raise Exception("Must be using python 3")
    
# initialize the dictionary holding the results of the letter frequencies
freq_dict = {}
for i in list("abcdefghijklmnopqrstuvwxyz") : freq_dict[i] = 0  # initial count of 0 for each letter in list

# sample text
text = "Mary had a little lamb whose fleece was white as snow and everywhere that mary went the lamb was sure to go."

# normalize the text to lower case
text_lower = text.lower()

# replace (r) all non-word characters (\W) with an empty string ('')
import re
text_cleaned = re.sub(r'\W+', '', text_lower)

# compute frequency
for i in list(text_cleaned):
    freq_dict[i] += 1

# summarize results 
print ("Input Text:  "+text)       
for key in freq_dict:
    print("Letter "+key+" appears "+str(freq_dict[key])+" times")

print ("Done")
