# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer 
# Store tracks Rentals (invoices) and Inventory
# =============================================================================

class Store:
	def __init__(self, catalog, client):
		self.customerList = client.List
		self.inventory = catalog
		self.month = [i for i in range(35)]
		self.rentals = []
	
		
    def open(self, day):
        for customer in self.customerList:
            customer.returnTool(day)
            shopping = customer.shop_today()
            if shopping:
                customer.rentTool(self.Inventory, day)

		
		dailyProfit = 0
		for customer in range(numCustomers):
			if Customer.toolBox.tool.isDue():
				Customer.toolBox.tool.returnTool()
		#this logic is wrong. They may accidentally pay twice for the same tool
		#because of this, I need to call customer.paystore at a different time
		#but I don't quite want to go that far yet
		for Customer in CustomerList:
			Customer.rentTool()			
			dailyProfit += Customer.payStore()
		
	def createRental(customerName, toolsRented[], rentalTotal, dayRented, dayDue):
		rental = new Rental(customerName, toolsRented[], rentalTotal, dayRented, dayDue)
		self.Rentals.append(rental)
		return self.Rentals;
		