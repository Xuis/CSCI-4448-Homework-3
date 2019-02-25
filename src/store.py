# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer 
# Store tracks Rentals (invoices) and Inventory
# =============================================================================

# from src.tool import Tool, ConcreteTool, PaintingTool, PlumbingTool, WoodworkTool, YardworkTool
# from src.customer import Customer
from src.catalog import Catalog, Client
class Store:
	def __init__(self):
<<<<<<< HEAD
		self.customerList = Client.List
		self.inventory = Catalog.onhand
		self.day = [i for i in range(35)]
		self.rentals = []
=======
		self.CustomerList = Client.List
		self.Inventory = Catalog
		self.month = [i for i in range(35)]
		self.Rentals = []
>>>>>>> ec7845bc13c8e947c9dcba252692fcbd60b7bdbb
	
		
	def open(self, day):
		#need a random  number of customers daily
        # updating so that customers choose when to come in based on number of tools in toolbox.
		# TODO this should occur after returns.
		for customer in self.customerList:
			shopping = customer.shop_today()
			if shopping:
				customer.rentTool(self.Inventory, day)

		
		dailyProfit = 0
		for customer in range(numCustomers):
			if customer.toolBox.tool.isDue():
				customer.toolBox.tool.returnTool()
		#this logic is wrong. They may accidentally pay twice for the same tool
		#because of this, I need to call customer.paystore at a different time
		#but I don't quite want to go that far yet
		for customer in customerList:
			customer.rentTool()			
			dailyProfit += customer.payStore()
		
	def createRental(customerName, toolsRented[], rentalTotal, dayRented, dayDue):
		rental = new Rental(customerName, toolsRented[], rentalTotal, dayRented, dayDue)
		self.rentals.append(rental)
		return self.rentals
		