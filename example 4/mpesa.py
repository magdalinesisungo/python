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
		if 
		
			

