# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer
# Store tracks Rentals (invoices) and Inventory
# =============================================================================

from rental import Rental
class Store:
    def open(self, day):
        for customer in self.customerList:
            customer.returnTool(day)
            shopping = customer.shop_today()
            if shopping:
                payment, tools, dayDue = customer.requestRental(self.inventory, day)
                self.createRental(day, customer.name, tools, payment, dayDue)

# -------------------- New UML Methods -------------------
    def __init__(self, catalog, client):
        self.customerList = client.getCustomerList()
        self.inventory = catalog
        self.month = [i for i in range(35)]
        self.rentalList = []
	
    def createRental(self, day, customerName, toolsRented, rentalTotal, dayDue): 
        rental = Rental(day, customerName, toolsRented, rentalTotal, dayDue)
        self.rentalList.append(rental)
		
        
    def getInventory(self):
        return self.inventory

    def getRentals(self):
        return self.rentals