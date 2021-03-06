# Python Cheat Sheet

[Python Standard Library](https://docs.python.org/3/library/index.html)

[Python Language Reference](https://docs.python.org/3/reference/index.html)

Examples drawn from 

[https://www.tutorialspoint.com/python/](https://www.tutorialspoint.com/python/)

### Python 2 and 3 are Incompatible
* In Python 2 print is a statement but in Python 3 print is a function.
<pre>
print ("hello")		# Python 2 or 3
print "hello"		# only Python 2.  Error in Python 3
</pre>

* In Python 2 long is a data type.  In Python 3 all integers are long and specifying a number as a long (3L), will yield a syntax error
<pre>
print (2L + 3L)		# in Python 2 -> 5
print (2L)		# in Python 3 -> SyntaxError: invalid syntax
</pre>

* In Python 2 integer division will truncate the answer to an integer.  
In Python 3 integer division will always return a float.
<pre>
print (3/2)		# Fractional part is truncated in Python 2 -> 1 
print (3/2)		# in Python 3 -> 1.5
</pre>

* In Python 2 rounding of numbers would always round up  
In Python 3 rounding changed to round to nearest even number
<pre>
print (round(2.5))   #  rounds to nearest even integer in python 3 ->  2
print (round(3.5))   #  rounds to nearest even integer in python 3 ->  4

print (round(2.5))   #  rounds up in python 2 ->  3.0
print (round(3.5))   #  rounds up in python 2 ->  4.0
</pre>

###  Checking The Python Version
<pre>
import sys
if sys.version_info[0] < 3:
	raise Exception("Must be using python 3")
</pre>

### Code Blocks (also called code suites)

* A group of individual statements, which make a single code block are called suites in Python.
* Compound or complex statements, such as if, while, def, and class require a header line and a suite.
* Since braces are not used to define code blocks, python uses indentation to define code suite (aka a block).
* **NOTE:** indentation in Python is strictly enforced!

<pre>
if True:
	print ("yes")
	print ("ok")
else:
	print ("no")
	print ("not ok")
</pre>

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

print (counter)
print (miles)
print (name)
print (counter, name, car, hello)   # prints -> 100 John Bob's car is fast Joe said "Hi"
</pre>

### Multiple Assignment

<pre>
a = b = c = 1
a,b,c = 1, 2, "john"
a,b,c = (1,2,3)  # assignment from a tuple
a,b,c = ["fred", "john", "mary"] # assignment from a list		
</pre>

### Command Line Parameters - Accessing and Using
* sys.argv is a list in Python, which contains the command-line arguments passed to the script.
* To use sys.argv, you will first have to import the sys module. 

<pre>
import sys
print( sys.argv )	# all command line params are in the sys.argv array
print( "This is the name of the script: ", sys.argv[0])
print( "Number of arguments: ", len(sys.argv))
print( "The arguments are: " , str(sys.argv))
print( "All other arguments besides the script name itself: " , str(sys.argv[1:]))
</pre>

output for the above script named args.py :
<pre>
python args.py one two three
['args.py', 'one', 'two', 'three']
This is the name of the script:  args.py
Number of arguments:  4
The arguments are:  ['args.py', 'one', 'two', 'three']
All other arguments besides the script name itself:  ['one', 'two', 'three']
</pre>

### Deleting Variables from Python's Namespace

<pre>
a = "Dog"
b = [ 1, 2, 3]
c = { 1: 2}
d = 5

del d  		# will delete d
del a,b,c	# will delete variables a, b and c

print ( d + 1) 	# NameError: name 'd' is not defined
</pre>

### Six Standard Data Types

* number
* string 
* list
* tuple 
* dictionary
* set

### Numbers

* In Python numbers may be: int, long (only in Python 2), float or complex

<pre>
d = 5
e = 51234524L  	# denotes a long in python 2.  NOTE: In python 3 Error -> SyntaxError: invalid syntax 
f = -21.9      	# denotes a float
g = 3+2j + 4+6j  # denotes a complex number 7+8j
h = 2e3        	# denotes 2000.0
i = 1e-2       	# denotes 0.01
j = 11112222333344441111222233334444
print (j * 2)	# 22224444666688882222444466668888
k = 0x69	# hex 69 equals decimal 105

import math ; print math.sqrt(5)  # -> 2.2360679775
</pre>

### Strings 

* String may use either single ' or double " quotes
* substrings use the slice operator [ ]

<pre>
s = 'Hello World!'
print (len(s))	# -> 12

print (s)          # Prints complete string -> 'Hello World!'
print (s[0])       # Prints first character of the string -> 'H'
print (s[2:5])     # Prints characters starting from 3rd to 5th -> 'llo'
print (s[2:])      # Prints string starting from 3rd character -> 'llo World!'
print (s[:4])      # Prints string starting from index 0 character to 4th character-> 'Hell'
print (s * 2)      # Prints string two times -> 'Hello World!Hello World!'
print (s + "TEST") # Prints concatenated string

print (s[-1])	   # last char off the end of string -> '!'
print (s[-2])	   # second char off the end of string -> 'd'
print ("apple pie"[-9:-4])	# using slice with negative indices -> 'apple'
</pre>

### String Methods

<pre>
a = "   \t\tFRED   \n"
b = 'HELLO world'
c = '**awesome**'
d = "one,two,three"

print (a.strip())	# -> 'FRED'
print (b.lower())	# -> 'hello world'
print (b.upper())	# -> 'HELLO WORLD'
print (b.endswith('orld'))	# -> True
print (b.startswith('HEL'))	# -> True
print (c.strip('*'))	# -> 'awesome'
print (c.lstrip('*'))	# -> 'awesome**'
print (c.rstrip('*'))	# -> '**awesome'
print (d.split(','))	# returns a list -> ['one', 'two', 'three']
print (d.replace('one', 'uno'))	# replace all occurences in string -> 'uno,two,three'
print (d.count('o'))	# count the number of occurrences -> 2
print ('--'.join(['one', 'two', 'three']))	# join the sequence using separator -> 'one--two--three'

# formatting strings with variables
"My name is {0} and your name is {1}".format('Fred', "Ted")
</pre>

[Python 3 String methods reference](https://docs.python.org/3/library/stdtypes.html#string-methods)

[Advanced String formatting](https://www.python.org/dev/peps/pep-3101/)


### Lists

* Lists are the most versatile of python's compound data types.
* We use [ ] to define a list.
* all items in a list may be different data types
* sublists use the slice operator [ ]

<pre>
a = [1, {3,5,7,11}, 5.9, "john", 3+2j]
print (a) 

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
empty = []
empty += [1]  # add item to empty list


print (list)          # Prints complete list
print (list[0])       # Prints first element of the list -> 'abcd'
print (list[1:3])     # Prints elements starting from 2nd till 3rd -> [786, 2.23]
print (list[2:])      # Prints elements starting from 3rd element -> [2.23, 'john', 70.2]
print (tinylist * 2)  # Prints list two times  -> [123, 'john', 123, 'john']
print (list + tinylist) # Prints concatenated lists  -> ['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
print (list[-1])      # last item off the back of the list -> 70.2
print (list[-2])      # second to last item off the back of the list -> 'john'
list[0] = "frank"   # assignment
print ('john' in list)      # -> True
print ('sebastian' not in list) # -> True
</pre>

### Tuples

* Unlike lists, however, tuples are enclosed within parentheses.
* Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed 
* Tuples are enclosed in parentheses ( ( ) ) and cannot be updated. 
* Tuples can be thought of as read-only lists.

<pre>
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )

print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element

tinytuple = (123, 'john')

print (tinytuple * 2)     # Prints tuple two times -> (123, 'john', 123, 'john')
print (tuple + tinytuple) # Prints concatenated tuples -> ('abcd', 786, 2.23, 'john', 70.2, 123, 'john')
tuple[0] = 1     # error: TypeError: 'tuple' object does not support item assignment
</pre>

### Dictionary

* Python's dictionaries are kind of hash table type. 
* They work like associative arrays or hashes found in Perl and consist of key-value pairs. 
* A dictionary key can be almost any Python type, but are usually numbers or strings. 
* Values, on the other hand, can be any arbitrary Python object including other dictionaries.

* Dictionaries are enclosed by curly braces ({ }) 
* Dictionary values can be assigned and accessed using square braces ([ ]).
* Dictionaries have no concept of order among elements.

<pre>
# NOTE: Both keys and values can be variables.  For example
a=1
b=2
c = {a:b, b:a}
print c    # ->  {1: 2, 2: 1}

dict = {}
dict['one'] = "This is one"  # add to dict
dict[2]     = "This is two"  # add to dict

print (dict)     # we get -> {2: 'This is two', 'one': 'This is one'}
print (dict['one'])       # Prints value for 'one' key -> 'This is one'
print (dict[2])           # Prints value for 2 key -> 'This is two'

tinydict = {'name': 'john','code': 6734, 'dept': 'sales'}
anotherdict = {  "a": 1, "b": tinydict}		
print (anotherdict) 	  # Prints  {'a': 1, 'b': {'name': 'john', 'code': 6734, 'dept': 'sales'}}

print (tinydict)          # Prints complete dictionary: {'dept': 'sales', 'code': 6734, 'name': 'john'}
print (tinydict.keys())   # Prints all the keys: ['dept', 'code', 'name']
print (tinydict.values()) # Prints all the values: ['sales', 6734, 'john']

data = {"sample1": 356, "sample2": 34, "sample3": 59, "sample4": 78, "sample5": 602, "sample6": 143}

print (max(data, key=data.get))  	# prints the key with the max value;  sample5
print (data[max(data, key=data.get)])   # prints the max value of the key with the max value: 602

print (min(data, key=data.get))  	# prints the key with the min value;  sample2
print (data[min(data, key=data.get)])   # prints the min value of the key with the min value: 34
</pre>

### Set

* A set is like a dict with keys but no values, and they're both implemented using a hash table. 
* It's a little annoying that the {} notation denotes an empty dict rather than an empty set, but that's a historical artifact.

<pre>
a = {4, 4, 5, 6, 6, 4, 3, 4, 4, 4}   # obviously we have duplicate values
print (a) 		# -> {3, 4, 5, 6}
a[0]       # Error -> TypeError: 'set' object does not support indexing
a + a      # Error -> TypeError: unsupported operand type(s) for +: 'set' and 'set'

b = {4, 2, 17, 5}
print (a.union(b))   # sets can be unioned together. -> {2, 3, 4, 5, 6, 17}
print (a.intersection(b))  # intersection is all common elements.  -> {4, 5}
print (a.difference(b))    # remove b elments from a.  -> {3, 6}

print ({4,2}.issubset(b))  # is subset of.  -> True
print (b.issubset(b))      # b is a subset of itself. -> True

print ({17, 2, 4, 5, 6}.issuperset(b))  # is superset of.  -> True
print (b.issuperset(b))    # b is a superset of itself. -> True

print (3 in a)             # membership.  -> True
print (56 not in a)        # non-membership.  ->  True
print (len(a))             # number of elements in set a. -> 4
print (type(a))            # datatype of a.  ->  &lt;class 'set'&gt;

engineers = set(['John', 'Jane', 'Jack', 'Janice'])

engineers.add('Bob')    # add element to set
engineers.discard('Jack')  # removes element from set if present

print (engineers)   # -> {'Jane', 'Janice', 'Bob', 'John'} 

d = {1, 2, "key": "val"}	# syntax error because d is neither a set nor a dictionary.  It has to be one or the other.
</pre>
	
### Data Type Conversion

<pre>
print (type(3.0))    # -> &lt;class 'float'&gt;
print (float(3))     # -> 3.0

print (long(5.0))    # -> 5L  NOTE:  only in python 2.  Use int() in python 3 
# All integers are long in python 3 and call to convert is just int( )

print (hex(255))     # -> '0xff'
print (type(3))      # -> &lt;class 'int'&gt;
print (int(1.000))   # -> 1
print (list("fred")) # -> ['f', 'r', 'e', 'd']
print (str(10) + str(3.4)) # -> 103.4   (not 13.4)
print (type({1,2,3})) # -> &lt;class 'set'&gt;
print (set(list("hello")))  # -> list to set: {'o', 'h', 'l', 'e'}
</pre>

### Operator Precedence

<pre>
** 		# exponentiation
~ + -   	# unary not, unary positive and unary negative
* / % //	# multiply, divide, modulo and floor
+ -		# addition and subtraction
>> <<		# right and left bitwise shift
&		# bitwise and
^ |		# bitwise exclusive or and regular or
<= <> >=	# comparison operators
< > == !=	# equality operators: less, greater, equal and not equal
= %= /= //= -= += *= **= 	# assignment operators
is, is not	# identity operators
in, not in	# membership operators
not or and	# logical operators
</pre>

### If Statement

* The Python programming language assumes 1 decimal or 1.0 float values as True
* If a value is anything other than a boolean True, 1 or 1.0 it is assumed as a False in a comparision operation

Some examples:
<pre>
print( True == True)   	# True
print( 1 == True)   	# True
print (1.0 == True) 	# True

print (TRUE == True)	# NameError: name 'TRUE' is not defined
print (true == True)	# NameError: name 'true' is not defined

print ( "1" == True) 	# False
print( -1 == True)   	# False
print( 0 == True)   	# False
print (2 == True)   	# False
print ("True" == True)	# False
print ( 'true' == True)	# False
</pre>

### Single line If
<pre>
var = 100
if ( var  == 100 ) : print ("Value of expression is 100")

if var == 100:  print('yep it is 100')			# parens are optional
</pre>

### Multiline If

<pre>
name = 'fred'
if (name == 'fred') :
	print ("i like "+name)
	print ('nice guy')
elif (name == 'jim') :
	print ("i don't like "+name)
	print ('not a very nice guy')
else:
	print ("who is "+name)
	print ("I don't know "+name)
</pre>

### Looping For and While

<pre>
for x in range(1,10):
	print (x)

for x in range(1,100,5):
	print (x)
	
for i in list(str("hello world")):
	print (i)

x=1
while x<10:
	print (x)
	x +=1
</pre>	
	
### Classes

<pre>
class Parent:        # define parent class
	parentAttr = 100
	def _init_(self):
		print ("Calling parent constructor")
		
	def parentMethod(self):
		print ('Calling parent method')
		
	def setAttr(self, attr):
		Parent.parentAttr = attr
		
	def getAttr(self):
		print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
	def _init_(self):
		print ("Calling child constructor")
		
	def childMethod(self):
		print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
</pre>

### User Defined Functions
* Use the def keyword to define a new function
* Function parameters may have default values
* Functions may have a variable number of parameters
* return is optional if nothing is returned

<pre>
def defaultArg( name, msg = "Hello!"):
	print(msg, name)

# When we call the function we don't supply the second argument
defaultArg("Fred")	# prints "Hello! fred"

# Using named parameters we can change the order of the parameters
defaultArg(msg = "Bye", name = "Tom")		# prints "Bye Tom"

def varArgs(*list):
    for i in list:
            print(i)
	   
varArgs(1)		# prints 1
varArgs(1, "jack", [ 1,2,3])	# prints each item on its own line
</pre>

### Import Libraries

<pre>
import math
print (math.sqrt(10))
</pre>

### Throwing Exceptions
<pre>
if a != 1 :	raise Exception("a was not equal to 1")		# Exception: a was not equal to 1
</pre>
