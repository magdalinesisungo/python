
from datetime import datetime
class MpesaAccount:
	def __init__(self, name, phone_number):
		self.name = name
		self.phone_number = phone_number
		self.balance = 0
		self.deposits = []
		self.withdraws = []
		self.loan = 0
		 
	def deposit(self,amount):
		self.balance =  amount + self.balance
		now = datetime.now()
		object= {"time":now,"amount":amount}
		self.deposits.append(object)
		sms1 ="hello {}, you have deposited {} your balance is {}".format(self.name,amount,self.balance)
		print(sms1) 
		

	def withdraw(self, amount):
		if amount<self.balance:
			self.balance =  self.balance-amount
			now = datetime.now()
			object= {"time":now,"amount":amount}
			self.withdraws.append(object)
			sms2= "hello {}, you have withdrawn {} your balance is {}".format(self.name,amount,self.balance)
			print (sms2)
		else:
			print("insufficient balance")	
			

	def check_balance(self):
		sms3="hello {}, your current balance is {}".format(self.name, self.balance)
		print(sms3)

	def my_deposits(self):
		for deposit in self.deposits:
			time = deposit["time"].strftime("%A %B %d %Y")
			amount = deposit["amount"]
			print("hello {}, on date {} you deposited {}".format(self.name,time,amount))

	def my_withdraws(self):
		for withdraw in self.withdraws:
			time = withdraw["time"].strftime("%A %B %d %Y")
			amount = withdraw["amount"]
			print("hello {}, on date {} you withdrew {}".format(self.name,time,amount))

	def give_loans(self,amount):
		if len(self.deposits)>=5 and amount<1/3*sum(self.deposits) and self.loan==0:
			self.loan=self.loan+amount
			print ("Hello {}, you have get {}".format(self.name, amount))
		else:
			print("Hello {}, you cannot afford the loan".format(self.name))

	def pay_loan(self,amount):
		if self.loan==0:
			print("you do not have a loan")
		elif amount<self.loan:
			self.loan=self.loan-amount
			print("Hello {}you have paid part of your loan,{}. your remaining balance is {}".format(self.name ,amount,self.loan))
		elif amount==self.loan:
			self.loan=self.loan-amount
			print("you have paid all your loan")
		elif amount>self.loan:
			more=amount-self.loan
			self.balance= more+self.balance
			self.loan=amount-self.loan-more
			print("Hello {} you have paid more than is required, your new balance is{}".format(self.name,self.balance))

	def statement(self):
		for b in self.withdraws:
			time=b["time"].strftime("%c")
			amount=b["amount"]
			print("on {} you withdrew{}".format(time,amount))
			
		for x in self.deposits:
			time=x["time"].strftime("%c")
			amount=x["amount"]
			print("on {} you deposited{}".format(time,amount))

		
			

















