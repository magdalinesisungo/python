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
		self.deposits.append(amount)
		sms1 ="hello {}, you have deposited {} your balance is {}".format(self.name,amount,self.balance)
		print(sms1) 
		

	def withdraw(self, amount):
		if amount<self.balance:
			self.balance =  self.balance-amount
			self.withdraws.append(amount)
			sms2= "hello {}, you have withdrawn {} your balance is {}".format(self.name,amount,self.balance)
			print (sms2)
		else:
			print("insufficient balance")	
			

	def check_balance(self):
		sms3="hello {}, your current balance is {}".format(self.name, self.balance)
		print(sms3)

	def my_deposits(self):
		for k in self.deposits:
			print(k)

	def my_withdraws(self):
		for s in self.withdraws:
			print(s)

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
			print("you have paid your all your loan")
		elif amount>self.loan:
			more=amount-self.loan
			self.balance= more+self.balance
			self.loan=amount-self.loan-more
			print("Hello {} you have paid more than is required, your new balance is{}".format(self.name,self.balance))
		
			

















