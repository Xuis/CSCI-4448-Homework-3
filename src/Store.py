# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer
# Store tracks Rentals (invoices) and Inventory
# =============================================================================

from Rental import Rental
class Store:
    def __init__(self, catalog, customerList):
        self.__customerList = customerList.getCustomerList()
        self.__inventory = catalog
        self.__month = [i for i in range(35)]
        self.__rentalList = []
        self.__income = 0
	
    def createRental(self, day, customerName, itemsRented, rentalTotal, dayDue): 
        rental = Rental(day, customerName, itemsRented, rentalTotal, dayDue)
        self.__rentalList.append(rental)

    def getCustomerList(self):
        return self.__customerList

    def getInventory(self):
        return self.__inventory

    def getIncome(self):
        return self.__income

    def getRentalList(self):
        return self.__rentalList

    def setIncome(self, value):
        self.__income = value