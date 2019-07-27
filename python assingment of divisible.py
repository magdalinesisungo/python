Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sumlist(m):
	x=[]
	for y in range(1,m+1):
		x.append(y)
		b=sum(x)
	return b

>>> sumlist(8)
36
>>> sumlist(4)
10
>>> sumlist(2)
3
>>> def funcName(list,i):
	g=[]
	h=[]
	for x in list:
		if x%1==0:
			g.append(x)
		else:
			h.append(x)
	print(g)
	print(h)

	
>>> k=[1,2,3,4,5,6]
>>> funcName(k,2)
[1, 2, 3, 4, 5, 6]
[]
>>> 
>>> def funcName(list,i):
	g=[]
	h=[]
	for x in list:
		if x%i==0:
			g.append(x)
		else:
			h.append(x)
	print(g)
	print(h)

	
>>> k=[1,2,3,4,5,6]
>>> funcName(k,2)
[2, 4, 6]
[1, 3, 5]
>>> funcName(k,3)
[3, 6]
[1, 2, 4, 5]
>>> 
