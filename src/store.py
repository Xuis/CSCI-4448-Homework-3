# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer 
# Store tracks Rentals (invoices) and Inventory
# =============================================================================


class Store:
	def open(self, day):
		for customer in self.customerList:
			customer.returnTool(day)
			shopping = customer.shop_today()
			if shopping:
				payment, tools, dayDue = customer.requestRental(self.inventory, day)
				self.createRental(day, customer.name, tools, rentalTotal, dayDue)

# -------------------- New UML Methods -------------------
	def __init__(self, catalog, client):
		self.customerList = client.getCustomerList()
		self.inventory = catalog
		self.month = [i for i in range(35)]
		self.rentals = {}
	
	def createRental(self, day, customerName, toolsRented, rentalTotal, dayDue):#TODO this needs to create a RentalRecord object instead of put it into a dictionary
        #I like the dictionary method but since we have a class RentalRecord, it should be instantiated here 
		self.rentals[day] = {"Customer Name": customerName, "Tools": toolsRented, "Payment": rentalTotal, "Day Rented": dayRented, "Due Date": dayDue}
		
	def requestPayment(self):
		return -1

	def getInventory(self):
		return self.inventory

	def getRentals(self):
		return self.rentals