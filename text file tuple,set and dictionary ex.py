Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> a=(1,2,3,4)
>>> b=('a','b','c','d')
>>> Append
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Append
NameError: name 'Append' is not defined
>>> a.append(5)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> b.remove('b')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b.remove('b')
AttributeError: 'tuple' object has no attribute 'remove'
>>> b
('a', 'b', 'c', 'd')
>>> for x in a:
	print(x)

	
1
2
3
4
>>> c=list(a)
>>> c
[1, 2, 3, 4]
>>> d=[x for x in a]
>>> d
[1, 2, 3, 4]
>>> f=a+b
>>> f
(1, 2, 3, 4, 'a', 'b', 'c', 'd')
>>> a*3
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> "b" in b
True
>>> "e" in b
False
>>> s in a
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s in a
NameError: name 's' is not defined
>>> "s" in a
False
>>> "i"in a
False
>>> x=[1,2,3,4]
>>> y=(x)
>>> y
[1, 2, 3, 4]
>>> y=(z for z in x)
>>> y
<generator object <genexpr> at 0x0184C8F0>
>>> a=[1,2,3,4,5,6,7,8,9]
>>> b=set(a)
>>> b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> c={"a","b","a","c","c"}
>>> c
{'a', 'c', 'b'}
>>> d={"a","A","b","B"}
>>> d
{'a', 'B', 'b', 'A'}
>>> d={"a","A","b","B","a","B"}
>>> D
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    D
NameError: name 'D' is not defined
>>> d
{'a', 'B', 'b', 'A'}
>>> s1={1,2,3,4}
>>> s2={3,4,5,6}
>>> s2.add(7)
>>> s2
{3, 4, 5, 6, 7}
>>> s2.remove(7)
>>> s2
{3, 4, 5, 6}
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s1.difference(s2)
{1, 2}
>>> s2.difference(s1)
{4, 5, 6}
>>> s1.intersection(s2)
{3}
>>> s2.intersection(s1)
{3}
>>> s2.union(s1)
{1, 2, 3, 4, 5, 6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> s2.update({10,11,12})
>>> s2
{3, 4, 5, 6, 10, 11, 12}
>>> codes=["Kenya":254, "Uganda":256, :"Tanzania":255}
SyntaxError: invalid syntax
>>> codes
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    codes
NameError: name 'codes' is not defined
>>>  codes= "Kenya":254, "Uganda":256, :"Tanzania":255}
SyntaxError: unexpected indent
>>> 
>>> 
>>> 
>>> codes={'Kenya';254, 'Uganda':256, 'Tanzania':255}
SyntaxError: invalid syntax
>>> codes={'Kenya':254, 'Uganda':256, 'Tanzania':255}
>>> code["Kenya"]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    code["Kenya"]
NameError: name 'code' is not defined
>>> codes['kenya']
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    codes['kenya']
KeyError: 'kenya'
>>> codes['Kenya']
254
>>> codes['Kenya']=250
>>> codes
{'Kenya': 250, 'Uganda': 256, 'Tanzania': 255}
>>> codes['Rwanda']=252
>>> codes
{'Kenya': 250, 'Uganda': 256, 'Tanzania': 255, 'Rwanda': 252}
>>> codes.pop('Rwanda')
252
>>> codes
{'Kenya': 250, 'Uganda': 256, 'Tanzania': 255}
>>> codes.values()
dict_values([250, 256, 255])
>>> for x in codes.keys():
	print(x)

	
Kenya
Uganda
Tanzania
>>> for x in codes.values():
	print(x)

	
250
256
255
>>> m=dict()
>>> m["a"]=10
>>> m["b"]=20m
SyntaxError: invalid syntax
>>> m["b
      
SyntaxError: EOL while scanning string literal
>>> m["b"]=20
      
>>> m
      
{'a': 10, 'b': 20}
>>> 
      
>>> 
      

>>> 
      

>>> 
      
>>> 
      
>>> 
      
>>> a=range(0,10)
      
>>> a
      
range(0, 10)
>>> for n in a:
      print(n)
      y=[n*n for n in a]

      
0
1
2
3
4
5
6
7
8
9
>>> y
      
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> for b in y.keys():
      print(b)

      
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    for b in y.keys():
AttributeError: 'list' object has no attribute 'keys'
>>> for b in y.keys():
      print{b}
      
SyntaxError: invalid syntax
>>> print b
      
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(b)?
>>> 'print'(b)
      
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    'print'(b)
TypeError: 'str' object is not callable
>>> for b in y.values():
      print(b)

      
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    for b in y.values():
AttributeError: 'list' object has no attribute 'values'
>>> for y in a values():
      
SyntaxError: invalid syntax
>>> for y in a.values():
      print(y)

      
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    for y in a.values():
AttributeError: 'range' object has no attribute 'values'
>>> for b in a.values():
      print(b)

      
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    for b in a.values():
AttributeError: 'range' object has no attribute 'values'
>>> for key in a.keys():
      print(key)

      
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    for key in a.keys():
AttributeError: 'range' object has no attribute 'keys'
>>> for keys in a.values():
      print(keys)

      
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    for keys in a.values():
AttributeError: 'range' object has no attribute 'values'
>>> for key in  range.values():
      print(key)

      
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    for key in  range.values():
AttributeError: type object 'range' has no attribute 'values'
>>> for key in keys():
      print(key)

      
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    for key in keys():
NameError: name 'keys' is not defined
>>> 
      
>>> a
      
range(0, 10)
>>> y
      
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> {"a"+"y"}
      
{'ay'}
>>> y=dict()
      
>>> s[y]=y*y
      
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    s[y]=y*y
TypeError: unsupported operand type(s) for *: 'dict' and 'dict'
>>> s=dict()
      
>>> a=range(0,10)
      
>>> a=dict()
      
>>> a[2]=2*2
      
>>> a
      
{2: 4}
>>> a=dict()
      
>>> for m in range(10):
      a[m]=a*a
      print(m)

      
Traceback (most recent call last):
  File "<pyshell#140>", line 2, in <module>
    a[m]=a*a
TypeError: unsupported operand type(s) for *: 'dict' and 'dict'
>>> a=range(0,10)
      
>>> y=dict()
      
>>> for y in range(10):
      y[d]=d*d

      
Traceback (most recent call last):
  File "<pyshell#145>", line 2, in <module>
    y[d]=d*d
TypeError: unsupported operand type(s) for *: 'set' and 'set'
>>> b=dict
      
>>> for p in range(10):
      m[p]=p*p

      
Traceback (most recent call last):
  File "<pyshell#149>", line 2, in <module>
    m[p]=p*p
TypeError: 'int' object does not support item assignment
>>> b=dict()
      
>>> for p in range(10):
      m[p]=p*p

      
Traceback (most recent call last):
  File "<pyshell#153>", line 2, in <module>
    m[p]=p*p
TypeError: 'int' object does not support item assignment
>>> m
      
0
>>> m=dict()
      
>>> for p in range(10):
      m[p]=p*p

      
>>> print(m)
      
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> 
      
>>> fruits=["melon","apple","orange","mango","pears","avocado","banana","passion","kiwi","peach"]
      
>>> m=dict()
      
>>> for a in fruits:
      m[a]=len(a)

      
>>> print(m)
      
{'melon': 5, 'apple': 5, 'orange': 6, 'mango': 5, 'pears': 5, 'avocado': 7, 'banana': 6, 'passion': 7, 'kiwi': 4, 'peach': 5}
>>> 
