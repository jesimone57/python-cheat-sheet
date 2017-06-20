#!/usr/local/bin/python3

# Example Python program to determine the word frequency in text

import re
import sys
if sys.version_info[0] < 3:
	raise Exception("Must be using python 3")

# sample text
text = "Mary  had  a little   lamb whose fleece was white as snow \t\tand everywhere that mary \twent the lamb was sure to go."

# normalize the text to lower case
text_lower = text.lower()

# compute frequency
freq_dict = {}
for word in re.split('\s+', text_lower):
    word = word.strip('.')
    word = word.strip(',')
    word = word.strip('?')
    word = word.strip('!')
    
    if word not in freq_dict:
        freq_dict[word] = 1
    else:
        freq_dict[word] += 1

# summarize results 
print ("Input Text:  "+text)       
for (key, value) in freq_dict.items():
    print("Word "+key+" appears "+str(value)+" times")

print ("Done")
