class Mpesa:

	def __init__(self,full_name,phone_number,balance):
		self.full_name = full_name
		self.phone_number = phone_number
		self.balance = balance

	def deposit_amount(self,m):
		deposit_amount = m + self.balance
		self.balance = self.balance + m
        sms1= "Dear {} you have deposited {} ksh, your current balance is {} ksh".format(self.full_name,m,self.balance)
        print (sms1)

	def withdraw(self,m):
		withdraw = self.balance - m
		sms2= "Dear {} you have withdrawn{} ksh, your curent balance is {} ksh".format(self.full_name,m,self.balance)
		print (sms2)

	def check_balance(self):
		check_balance = balance
		sms3= "Dear {} your current balance is {} ksh".format(self.full_name,m,self.balance)
		print (sms3)
