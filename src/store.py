# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer
# Store tracks Rentals (invoices) and Inventory
# =============================================================================

from rental import Rental
class Store:
    def __init__(self, catalog, customerList):
        self.customerList = customerList.getCustomerList()
        self.inventory = catalog
        self.month = [i for i in range(35)]
        self.rentalList = []
        self.income = 0
	
    def createRental(self, day, customerName, toolsRented, rentalTotal, dayDue): 
        rental = Rental(day, customerName, toolsRented, rentalTotal, dayDue)
        self.rentalList.append(rental)
		
        
    def getInventory(self):
        return self.inventory

    def getRentals(self):
        return self.rentals
