# Python Cheat Sheet

[Python Standard Library](https://docs.python.org/3/library/index.html)
[Python Language Reference](https://docs.python.org/3/reference/index.html)

Examples drawn from 

[https://www.tutorialspoint.com/python/](https://www.tutorialspoint.com/python/)

### Python 2 and 3 are incompatible
In python 2 print is a statement but in python 3 print is a function.

<pre>
print ("hello") # python 2 or 3
print "hello"   # only python 2.  Error in Python 3
</pre>

###  Checking The Python Version
<pre>
import sys
if sys.version_info[0] < 3:
	raise Exception("Must be using python 3")
</pre>

### Code Blocks

<pre>
# A group of individual statements, which make a single code block are called suites in Python.
# Compound or complex statements, such as if, while, def, and class require a header line and a suite.

# since no braces to define code blocks, python uses indentation to define code blocks.
 
if True:
	print ("yes")
	print ("ok")
else:
	print ("no")
	print ("not ok")
</pre>

NOTE: indentation in Python is strictly enforced!

see [https://www.tutorialspoint.com/python/python_basic_syntax.htm](https://www.tutorialspoint.com/python/python_basic_syntax.htm)


### Line Continuation

<pre>
# line continuation uses \ to continue the line
print 1+\
1+\
1
</pre>

### Assignment

<pre>
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string
hello = 'Joe said "Hi"'   # a string with quotes
car = "Bob's car is fast" # a string with quotes

print counter
print miles
print name
print (counter, name, car, hello)   # prints 100 John Bob's car is fast Joe said "Hi"
</pre>

### Multiple Assignment

<pre>
a = b = c = 1
a,b,c = 1, 2, "john"
a,b,c = (1,2,3)  # assignment from a tuple
a,b,c = ["fred", "john", "mary"] # assignment from a list		
</pre>

### Five Standard Data Types

* number
* string 
* list
* tuple 
* dictionary


### Numbers

<pre>
# numbers may be: int, long, float or complex
d = 5
e = 51234524L  # denotes a long
f = -21.9      # denotes a float
g = 3+2j + 4+6j  # denotes a complex number 7+8j
h = 2e3        # denotes 2000.0
i = 1e-2       # denotes 0.01
k = 0x69	   # hex 69 equals decimal 105
import math ; print math.sqrt(5)  # -> 2.2360679775

del d  # will delete d
del a,b,c
</pre>

### Strings 

<pre>
# use either single ' or double " quotes
# substrings use the slice operator [ ]
str = 'Hello World!'
print (len(str))

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times -> 'Hello World!Hello World!'
print str + "TEST" # Prints concatenated string

print str[-1]	   # last char off the end of string -> '!'
print str[-2]	   # second char off the end of string -> 'd'
</pre>

### Strings Functions

<pre>
a = "   \t\tFRED   \n"
print(a.strip())  # -> 'FRED'
print(a.lower())  # -> 'fred'
</pre>

### Lists

<pre>
# Lists are the most versatile of python's compound data types.
# We use [ ] to define a list.
# all items in a list may be different data types
# sublists use the slice operator [ ]

a = [1, 2L, 5.9, "john", 3+2j]
print a 

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
empty = []
empty += [1]  # add item to empty list


print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times  -> [123, 'john', 123, 'john']
print list + tinylist # Prints concatenated lists  -> ['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
print list[-1]      # last item off the back of the list -> 70.2
print list[-2]      # second to last item off the back of the list -> 'john'
list[0] = "frank"   # assignment
print 'john' in list      # -> True
print 'frank' not in list # -> True
</pre>

### Tuples

<pre>
# Unlike lists, however, tuples are enclosed within parentheses.
# Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, 
# while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
# Tuples can be thought of as read-only lists.

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete tuple
print tuple[0]        # Prints first element of the tuple
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints tuple two times -> (123, 'john', 123, 'john')
print tuple + tinytuple # Prints concatenated tuples -> ('abcd', 786, 2.23, 'john', 70.2, 123, 'john')
tuple[0] = 1     # error: TypeError: 'tuple' object does not support item assignment
</pre>

### Dictionary
 
<pre>
# Python's dictionaries are kind of hash table type. 
# They work like associative arrays or hashes found in Perl and consist of key-value pairs. 
# A dictionary key can be almost any Python type, but are usually numbers or strings. 
# Values, on the other hand, can be any arbitrary Python object.

# Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed 
# using square braces ([]).
# NOTE: Dictionaries have no concept of order among elements.

# NOTE: Both keys and values can be variables.  For example
a=1
b=2
c = {a:b, b:a}
print c    # ->  {1: 2, 2: 1}

dict = {}
dict['one'] = "This is one"  # add to dict
dict[2]     = "This is two"  # add to dict
print dict     # we get -> {2: 'This is two', 'one': 'This is one'}

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one']       # Prints value for 'one' key -> 'This is one'
print dict[2]           # Prints value for 2 key -> 'This is two'
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values
</pre>

### Data Type Conversion

<pre>
print (float(3))     # -> 3.0
print (long(5.0))    # -> 5L
print (hex(255))     # -> '0xff'
print (int(1.000))   # -> 1
</pre>

### Operator Precedence
<pre>
** 			# exponentiation
~ + -   	# unary not, unary positive and unary negative
* / % //	# multiply, divide, modulo and floor
+ -			# addition and subtraction
>> <<		# right and left bitwise shift
&			# bitwise and
^ |			# bitwise exclusive or and regular or
<= <> >=	# comparison operators
< > == !=	# equality operators: less, greater, equal and not equal
= %= /= //= -= += *= **= 	# assignment operators
is is not	# identity operators
in not in	# membership operators
not or and	# logical operators
</pre>

### If statement
<pre>
# Python programming language assumes any non-zero and non-null values as TRUE, 
# and if it is either zero or null, then it is assumed as FALSE value.

print 0 == True   # -> False
print 1 == True   # -> True

### Single line if
var = 100
if ( var  == 100 ) : print "Value of expression is 100"
print "Good bye!" 
</pre>

### multiline If
<pre>
a = 5
if (a == 5) :
	print "a is 5"
	print 'yes it is'
else:
	print "a is not 5"
	print "no it is not"
</pre>

### Looping For and While
<pre>
for x in range(1,10):
	print (x)

for x in range(1,100,5):
	print (x)

x=1
while x<10:
	print(x)
	x +=1
</pre>	
	
### Classes
<pre>
class Parent:        # define parent class
	parentAttr = 100
	def _init_(self):
		print "Calling parent constructor"
		
	def parentMethod(self):
		print 'Calling parent method'
		
	def setAttr(self, attr):
		Parent.parentAttr = attr
		
	def getAttr(self):
		print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
	def _init_(self):
		print "Calling child constructor"
		
	def childMethod(self):
		print 'Calling child method'

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
</pre>

### Import Libraries
<pre>
import math
print (math.sqrt(10))
</pre>
