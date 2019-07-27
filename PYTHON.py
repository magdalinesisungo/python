Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  a=2
SyntaxError: unexpected indent
>>> a=2
>>> b=3
>>> a
2
>>> c="boy"
>>> d="girl"
>>> c
'boy'
>>> b
3
>>> d
'girl'
>>> a+b
5
>>> 
>>> e=a**b
>>> e
8
>>> f=c**d
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    f=c**d
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
>>> (a)
2
>>> (b)
3
>>> (d)
'girl'
>>> (c)
'boy'
>>> (e)
8
>>> type(a)
<class 'int'>
>>> 2
2

>>> 
>>> 
>>> 
>>> 
>>> 
>>> f=10/b
>>> 
>>> f=10//b
>>> 
>>> f=10//b
>>> 
>>> f=10/b
>>> 
>>> f
3.3333333333333335

>>> 2f=10/b
SyntaxError: invalid syntax
>>> g=10/b
>>> f
3.3333333333333335
>>> g
3.3333333333333335
>>> f=10//b
>>> f
3
>>> str(a)
'2'
>>> h=str(b)
>>> h
'3'
>>> type(h)
<class 'str'>
>>> int(b)
3
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'girl'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> i='123"
SyntaxError: EOL while scanning string literal
>>> j=int(i)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    j=int(i)
NameError: name 'i' is not defined
>>> j=int(i)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    j=int(i)
NameError: name 'i' is not defined
>>> i="123"
>>> i
'123'
>>> j=int(i)
>>> j
123
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print("hello akirachix")
hello akirachix
>>> print("hello akirachix in 22019")
hello akirachix in 22019
>>> print ("hello Akirachix \n 2019")
hello Akirachix 
 2019
>>> print("my name is: \n James \n Mwai")
my name is: 
 James 
 Mwai
>>> \a print("hahaha")
SyntaxError: unexpected character after line continuation character
>>> print("hahaha\a")
hahaha
>>> print("hello \t akirachix")
hello 	 akirachix
>>>  print("hello \v akirachix")
SyntaxError: unexpected indent
>>> print("hello \v akirachix")
hello  akirachix
>>>  school = "akirachix"
SyntaxError: unexpected indent
>>> school.upper()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    school.upper()
NameError: name 'school' is not defined
>>> school = "Akirachix"
>>> school.upper()
'AKIRACHIX'
>>> school = "akirachix"
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s=s' LOVE AKIRACHIX'
SyntaxError: invalid syntax
>>> s = s "i love me'
SyntaxError: EOL while scanning string literal
>>> S.UPP
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    S.UPP
NameError: name 'S' is not defined
>>> s = "i love akirachix"
>>> s
'i love akirachix'
>>> s.upper()
'I LOVE AKIRACHIX'
>>> s.lower()
'i love akirachix'
>>> s.capitalize()
'I love akirachix'
>>> s.numeric()
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    s.numeric()
AttributeError: 'str' object has no attribute 'numeric'
>>> 

>>> 
>>> 
>>> a="AKIRACHIX"
>>> b="akirachix"
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>>  print
SyntaxError: unexpected indent
>>> print ("Hello{}{},welcome to {}".format(first,last,school)









	   )
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    print ("Hello{}{},welcome to {}".format(first,last,school)
NameError: name 'first' is not defined
>>> 
	   
>>> 
	   
>>> 
	   
>>> 
	   
>>> 
	   
>>> 
	   
>>> first=Mag
	   
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    first=Mag
NameError: name 'Mag' is not defined
>>> first="Mag"
	   
>>> last="Rubby"
	   
>>> school="akirachix"
	   
>>> print("hello {}{} welcome to {}".format(first,last,school))
	   
hello MagRubby welcome to akirachix
>>> year=1999
	   
>>> fast=Mag
	   
Traceback (most recent call last):
  File "<pyshell#260>", line 1, in <module>
    fast=Mag
NameError: name 'Mag' is not defined
>>> 
	   
>>> 
	   
>>> fast="Mag"
	   
>>> year=1999
	   
>>> age=20
	   
>>> print("hello {}, you are {}years old".format(fast,age))
	   
hello Mag, you are 20years old
>>> hello Mag, you are 20years old
	   
SyntaxError: invalid syntax
>>> 
	   
>>> 
	   
>>> 
	   

>>> 
	   
>>> fast="Mag"
	   
>>> year=1999
	   
>>> print("hello {}, you are {}years old".format(fast,age))
	   
hello Mag, you are 20years old
>>> 
	   

>>> 
	   
>>> 
	   
>>> 
	   
>>> 
	   
>>> 
	   
>>> 
	   
>>> 
	   

>>> 
	   
>>> 
	   
>>> 
	   
>>> c1="Kenya"
	   
>>> c2="Uganda"
	   
>>> c3="Tanzania"
	   
>>> ke-code="254"
	   
SyntaxError: can't assign to operator
>>> ke_code="254"
	   
>>> ug_code="256"
	   
>>> tz_code="255"
	   
>>> c1
	   
'Kenya'
>>> c2
	   
'Uganda'
>>> c3
	   
'Tanzania'
>>> ke_ode
	   
Traceback (most recent call last):
  File "<pyshell#296>", line 1, in <module>
    ke_ode
NameError: name 'ke_ode' is not defined
>>> ke_code
	   
'254'
>>> ug_code
	   
'256'
>>> tz_code
	   
'255'
>>> ("{} code is {}".format(c1,ke_code))
	   
'Kenya code is 254'
>>> print("[] code is {}".format(c1,ke_code))
	   
[] code is Kenya
>>> print("[] code is {}".format(c1,ke_code))[] code is Kenya
	   
SyntaxError: invalid syntax
>>> 
	   
>>> 
	   
>>> 
	   
>>> print("{} code is {}".format(c1,ke_code))
	   
Kenya code is 254
>>> print("{} code is {}".format(c2,ug_code))
	   
Uganda code is 256
>>> prit("{} code is {}".format(c3,tz_code))
	   
Traceback (most recent call last):
  File "<pyshell#318>", line 1, in <module>
    prit("{} code is {}".format(c3,tz_code))
NameError: name 'prit' is not defined
>>> print("{} code is {}".format(c3,tz_code))

	   
Tanzania code is 255
           



x





           




           

































           

           




















