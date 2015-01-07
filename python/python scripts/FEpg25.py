Python 2.4.6 (#1, Aug  3 2009, 17:05:16) 
[GCC 4.0.1 (Apple Inc. build 5490)] on darwin
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 1.1.6      
>>> for i in range([1.1,2.1})
SyntaxError: invalid syntax
>>> for i in range({1.1,2.1])
SyntaxError: invalid syntax
>>> for i in range([1.1,2.1])
SyntaxError: invalid syntax
>>> for i in range([1.1,2.1]):
	print i

	

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in -toplevel-
    for i in range([1.1,2.1]):
TypeError: range() integer end argument expected, got list.
>>> total = 0
>>> for i in [1.1,2.1]
SyntaxError: invalid syntax
>>> total = 0
>>> for i in '1.1,2.1':
	total = total + float(i)
print total
SyntaxError: invalid syntax
>>> print total
0
>>> total = 0
>>> for i in [1.1,2.1]:
	total = total + float(i)

	
>>> print total
3.2
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/robflynn/Documents/tests.py", line 8, in -toplevel-
    total = total + float(i)
ValueError: invalid literal for float(): 1.23,2.4,3.123
>>> ================================ RESTART ================================
>>> 
6.723
>>> ================================ RESTART ================================
>>> 
6.723
>>> t
['1.23,2.4,3.123']
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/robflynn/Documents/tests.py", line 7, in -toplevel-
    t = float[s]
TypeError: unsubscriptable object
>>> ================================ RESTART ================================
>>> 
6.723
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/robflynn/Documents/tests.py", line 8, in -toplevel-
    total = total + float([i])
TypeError: float() argument must be a string or a number
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):

  File "/Users/robflynn/Documents/tests.py", line 8, in -toplevel-
    total = total + float([i])
TypeError: float() argument must be a string or a number
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/robflynn/Documents/tests.py", line 7, in -toplevel-
    for i in float([s]):
TypeError: float() argument must be a string or a number
>>> total
0
>>> i

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in -toplevel-
    i
NameError: name 'i' is not defined
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/robflynn/Documents/tests.py", line 8, in -toplevel-
    total = total + i
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/robflynn/Documents/tests.py", line 8, in -toplevel-
    total = total + int(i)
ValueError: invalid literal for int(): 1.23,2.4,3.123
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/robflynn/Documents/tests.py", line 8, in -toplevel-
    total = total + float(i)
ValueError: invalid literal for float(): 1.23,2.4,3.123
>>> total
0
>>> s
'1.23,2.4,3.123'
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/robflynn/Documents/tests.py", line 7, in -toplevel-
    x = float([s])
TypeError: float() argument must be a string or a number
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):

  File "/Users/robflynn/Documents/tests.py", line 7, in -toplevel-
    x = float[s]
TypeError: unsubscriptable object
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/robflynn/Documents/tests.py", line 7, in -toplevel-
    x = float('1.1,2.1')
ValueError: invalid literal for float(): 1.1,2.1
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/robflynn/Documents/tests.py", line 7, in -toplevel-
    x = float(['1.1,2.1'])
TypeError: float() argument must be a string or a number
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/robflynn/Documents/tests.py", line 7, in -toplevel-
    x = float([1.1,2.1])
TypeError: float() argument must be a string or a number
>>> ================================ RESTART ================================
>>> 
6.753
>>> 
