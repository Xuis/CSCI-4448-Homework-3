# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer 
# Store tracks Rentals (invoices) and Inventory
# =============================================================================

# from src.tool import Tool, ConcreteTool, PaintingTool, PlumbingTool, WoodworkTool, YardworkTool
# from src.customer import Customer
# from src.catalog import Catalog
class Store():
	def __init__(self, name, CustomerList[], ToolsList[]):
		self.name = name
		self.CustomerList = CustomerList
		self.Inventory = ToolsList
		self.day = [i for i in range(36)]
		self.Rentals = []
	
		
	def open(self):
		#need a random  number of customers daily
		numCustomers = random.choice(range(11)
		
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
		