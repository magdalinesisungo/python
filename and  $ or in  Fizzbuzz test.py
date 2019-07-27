Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for x in range(0,10):
	if x%3==0:
		print(x)

		
0
3
6
9
>>> for x in range(0,10):
	if x%3!=0:
		print(x)

		
1
2
4
5
7
8
>>> for x in range(0,10):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	else:
		print("{} is not divisible by 3".format(x))

		
0 is divisible by 3
1 is not divisible by 3
2 is not divisible by 3
3 is divisible by 3
4 is not divisible by 3
5 is not divisible by 3
6 is divisible by 3
7 is not divisible by 3
8 is not divisible by 3
9 is divisible by 3
>>> 
>>> 
>>> for x in range(0,20):
	if x%3==0:
		print("{} is divisible by 3".format(x))

		
0 is divisible by 3
3 is divisible by 3
6 is divisible by 3
9 is divisible by 3
12 is divisible by 3
15 is divisible by 3
18 is divisible by 3
>>> for x in range(0,20):
	if x%3==0:
		print("{} is divisible by 3".format(x))
	elif x%5==0:
		print("{} is divisible by 5".format(x))
	else:
		print("{} is not divisible by 3 or 5".format(x))

		
0 is divisible by 3
1 is not divisible by 3 or 5
2 is not divisible by 3 or 5
3 is divisible by 3
4 is not divisible by 3 or 5
5 is divisible by 5
6 is divisible by 3
7 is not divisible by 3 or 5
8 is not divisible by 3 or 5
9 is divisible by 3
10 is divisible by 5
11 is not divisible by 3 or 5
12 is divisible by 3
13 is not divisible by 3 or 5
14 is not divisible by 3 or 5
15 is divisible by 3
16 is not divisible by 3 or 5
17 is not divisible by 3 or 5
18 is divisible by 3
19 is not divisible by 3 or 5
>>> for x in range(0,100):
	if x%7==0:
		print("{} is divisible by 7".format(x))

		
0 is divisible by 7
7 is divisible by 7
14 is divisible by 7
21 is divisible by 7
28 is divisible by 7
35 is divisible by 7
42 is divisible by 7
49 is divisible by 7
56 is divisible by 7
63 is divisible by 7
70 is divisible by 7
77 is divisible by 7
84 is divisible by 7
91 is divisible by 7
98 is divisible by 7
>>> 
>>> for x in range(0,20):
	if x%3==0 and x%5==0:
		print(x)

		
0
15
>>> 
>>> for x in range(0,20):
	if x%3==0 or x%5==0:
		print(x)

		
0
3
5
6
9
10
12
15
18
>>> true and true
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    true and true
NameError: name 'true' is not defined
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> True or True
True
>>> False or True
True
>>> True or False
True
>>> False or False
False
>>> 
>>> for x in range(900,950):
	if x%3==0 and x%5==0:
		print(x)

		
900
915
930
945
>>> for x in range(900,950):
	if x%3==0 and x%5==0:
		print("fizzbuzz")
	elif x%3==0:
		print("buzz")
	elif x%5==0:
		print("fizz")
	else:
		print(x)

		
fizzbuzz
901
902
buzz
904
fizz
buzz
907
908
buzz
fizz
911
buzz
913
914
fizzbuzz
916
917
buzz
919
fizz
buzz
922
923
buzz
fizz
926
buzz
928
929
fizzbuzz
931
932
buzz
934
fizz
buzz
937
938
buzz
fizz
941
buzz
943
944
fizzbuzz
946
947
buzz
949
>>> 
