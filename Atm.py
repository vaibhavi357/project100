class Atm(object):
	def __init__(self, cardNumber, pinNumber):
		self.cardNumber = cardNumber
		self.pinNumber = pinNumber

	def CashWithdrawl(self):
		print("cash withdrawn")	
	def BalanceEnquiry(self):
		print("balance enquiry")	

atm = Atm("cardNo.- 123456*********", "pinNo.- 491335")	
atm.BalanceEnquiry()	
print(atm.cardNumber)
print(atm.pinNumber)
atm.CashWithdrawl()
