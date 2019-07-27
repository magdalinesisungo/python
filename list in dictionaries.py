Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> customer={"name":"magda","balance":2000}
>>> customer={"name":"mercy","balance":800}
>>> customer={"name":"clare","balance":1000}
>>> customers=[customer1,customer2]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    customers=[customer1,customer2]
NameError: name 'customer1' is not defined
>>> customers=[customer1,customer2,customer3]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    customers=[customer1,customer2,customer3]
NameError: name 'customer1' is not defined
>>> customers
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    customers
NameError: name 'customers' is not defined
>>> customer={"name":"magda","balance":2000}
>>> customer1={"name":"magda","balance":2000}
>>> customer2={"name":"magda","balance":2000}
>>> customer3={"name":"clare","balance":1000}
>>> customers=[customer1,customer2,customer3]
>>> customers
[{'name': 'magda', 'balance': 2000}, {'name': 'magda', 'balance': 2000}, {'name': 'clare', 'balance': 1000}]
>>> for customer in customers:
	sms="Hi {}, your balance is {}".format(customer["name"],customer["balance"])
	print(sms)

	
Hi magda, your balance is 2000
Hi magda, your balance is 2000
Hi clare, your balance is 1000
>>> for customer in customers:
	loan=customer["balance"]/2.9
	sms="Hi {}, your loan balance is {}".format(customer["name"],customer["balance"])
	print(sms)

	
Hi magda, your loan balance is 2000
Hi magda, your loan balance is 2000
Hi clare, your loan balance is 1000
>>> 
>>> for customer in customers:
	loan=customer["balance"]/2.9
	sms="Hi {}, your loan balance is {}".format(customer["name"],customer["balance"])
	print(sms)

	
Hi magda, your loan balance is 2000
Hi magda, your loan balance is 2000
Hi clare, your loan balance is 1000
>>> 
>>> for customer in customers:
	loan=customer["balance"]/2.9
	print(loan)

	
689.6551724137931
689.6551724137931
344.82758620689657
>>> for customer in customers:
	sms="Hi {}, your loan balance is {}".format(customer["name"],customer["balance"])
	print(sms)

Hi magda, your loan balance is 2000
Hi magda, your loan balance is 2000
Hi clare, your loan balance is 1000
>>> for customer in customers:
	sms="Hi {}, your loan is {}".format(customer["name"],customer["balance"])
	print(sms)

	
Hi magda, your loan is 2000
Hi magda, your loan is 2000
Hi clare, your loan is 1000
>>> 
>>>  for customer in customers:
	sms="Hi {}, your loan is {}".format(customer["name"],["loan"])
	print(sms)
	
SyntaxError: unexpected indent
>>> 
>>> 
>>> for customer in customers:
	loan=customer["balance"]/2.9
	sms="Hi {}, your loan balance is {}".format(customer["name"],customer["loan"])
	print(sms)

	
Traceback (most recent call last):
  File "<pyshell#38>", line 3, in <module>
    sms="Hi {}, your loan balance is {}".format(customer["name"],customer["loan"])
KeyError: 'loan'
>>>  for customer in customers:
	loan=customer["balance"]/2.9
	sms="Hi {}, your loan balance is {}".format(customer["name"],["loan"])
	print(sms)
	
SyntaxError: unexpected indent
>>> for customer in customers:
	loan=customer["balance"]/2.9
	sms="Hi {}, your loan balance is {}".format(customer["name"],["loan"])
	print(sms)

	
Hi magda, your loan balance is ['loan']
Hi magda, your loan balance is ['loan']
Hi clare, your loan balance is ['loan']
>>> print(sms)
Hi clare, your loan balance is ['loan']
>>> for customer in customers:
	loan=customer["balance"]/2.9
	sms="Hi {}, your loan balance is {}".format(customer["name"],[loan])
	print(sms)

	
Hi magda, your loan balance is [689.6551724137931]
Hi magda, your loan balance is [689.6551724137931]
Hi clare, your loan balance is [344.82758620689657]
>>> 
>>> 
>>> 
>>> 
>>> for x in range(0,10):
	if x%3==0:
		print(x)

		
0
3
6
9
>>> 
