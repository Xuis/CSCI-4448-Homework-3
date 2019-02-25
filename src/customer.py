# =============================================================================
# There are 10 customers in 3 categories each with a unique name
# Customers can rent a max of 3 tools for 7 nights
# Business customers always rent 3 tools for 7 nights
# Casual customers rent 1-2 tools for 1-2 nights
# Regular customers rent 1-3 tools for 3-5 nights
# Customers interact with Store through renting and returning of tools and 
# paying for the tools.
# =============================================================================

import numpy as np


class Customer:
	def __init__(self, name):
		self.name = name
		self.toolbox = []
		self.maxNumTools = 3
		self.minNumTools = 0
		self.minNights = 0
		self.maxNights = 7
		self.currentNumTools = len(self.toolbox)

	def shop_today(self):
		# probability to shop based on # of tools in toolbox
		if self.currentNumTools == 3:
			return 0
		else:
			shopping = np.random.choice([1, 0], 1, p=[.5/self.currentNumTools, 1-(.5/self.currentNumTools)])
			return shopping
		
	def getNumNightsDesired(self):
		numNightsDesired = np.random.choice(range(self.minNights, self.maxNights))
		return numNightsDesired
		
	def getNumToolsDesired(self):
		numToolsDesired = np.random.choice(range(self.minNumTools, self.maxNumTools- self.currentNumTools))
		return numToolsDesired

	
	def rentTool(self, inventory, day):
		#a customer will only rent a tool if enough tools are available
		#and customers can only have 3 at a time
		nights = self.getNumNightsDesired()
		numToday = self.getNumToolsDesired()
		if len(inventory) >= numToday:
			for index in range(numToday):
				rentedTool = np.random.choice(inventory)
				rentedTool.day = day
				rentedTool.due = day + self.getNumNightsDesired
				self.toolbox.append(np.random.choice(inventory))
				inventory.rentTool(rentedTool)
					#the store needs to keep the rental info and we need to know on which day this was rented, so we can calculate which day it goes back
					# for instance, if this runs on Day 5 and the maxNights is 5, the tools go back on Day 10
					# so we do the check (if day 10, customer.ReturnTool() like that
				
		#Store.Income.acceptPayment(paymentOwed)
		#Store.Rental.newRental(
		
		return self.toolbox;
		
	def payStore(self, toolbox):
		paymentOwed = 0.0
		for tool in toolbox:
			paymentOwed = paymentOwed + tool.pricePerDay
		
		return paymentOwed;

		
	def returnTool(self, inventory, Store):
		
		return -1;
		
class CasualCustomer(Customer):
	def __init__(self, name):
		Customer.__init__(self, name)
		self.maxNights = 2
		self.minNights = 1
		self.maxNumTools = 2
		
class BusinessCustomer(Customer):
	def __init__(self, name):
		Customer.__init__(self, name)
		self.maxNights = 5
		self.minNights = 5
		
	def getNumToolsDesired(self):
		return 3;

class RegularCustomer(Customer):
	def __init__(self, name):
		Customer.__init__(self, name)
		self.maxNights = 5
		self.minNights = 3
		self.maxNumTools = 3
		self.minNumTools = 1

class ToolOrder:

    def getOrder(type):
        if type == 'business':
            return 3, 7
        if type == 'casual':
            return random.randint(1,2), random.randint(1,2)
        if type == 'regular':
            return random.randint(1,3), random.randint(3,5)